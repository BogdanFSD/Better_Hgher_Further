from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Booking_class
from .forms import Booking_class_form
# import login_required
import datetime
# Create your views here.

# @login_required


def check_if_available(user_requested_trainers, user_requested_date,
                       user_requested_time):
    booking_slot = len(Booking_class.objects.filter(
        trainers=user_requested_trainers, requested_date=user_requested_date,
        requested_time=user_requested_time))

    return booking_slot


def booking_training(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            booking_class = Booking_class_form()
        else:
            messages.add_message(
                request, messages.ERROR,
                "In order to book training you need to log in."
                "Login here.")
            url = reverse('account_login')
            return HttpResponseRedirect(url)

        return render(request, "booking/booking.html", {'Booking_class_form':
                                                        Booking_class_form})
    else:
        if request.method == 'POST':
            booking_class_form = Booking_class_form(data=request.POST)
            if booking_class_form.is_valid():
                user_requested_trainers = request.POST.get('trainers')
                user_requested_date = request.POST.get('requested_date')
                user_requested_time = request.POST.get('requested_time')

                # date_format = datetime.datetime.strptime(user_requested_time,
                #  "%m/%d/%Y").strftime("%Y/%m/%d")

                bookin_available = check_if_available(user_requested_trainers,
                                                      user_requested_date,
                                                      user_requested_time)

                if bookin_available > 0:
                    messages.add_message(
                        request, messages.ERROR,
                        "This time and date already booked"
                        f"{user_requested_time} on {user_requested_date}.")

                    return render(request, 'booking/booking.html',
                                  {'Booking_class_form': Booking_class_forms})

                else:
                    booking_data = Booking_class_form().save(commit=False)
                    booking_data.user = request.user
                    booking_data.save()

                    messages.add_message(
                        request, messages.SUCCESS,
                        f"Your booking with {user_requested_trainers} "
                        f"on {user_requested_date} at {user_requested_time}"
                        f" has been submitted.")
                    url = reverse('booking')

                    return HttpResponseRedirect(url)

            else:
                messages.add_message(
                    request, messages.ERROR,
                    "Sorry, something was not quite right. "
                    "Please try again.")
            return render(
                        request,
                        'pt_bookings/bookings.html',
                        {'booking_form': booking_form})
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, something was not quite right. "
                "Please try again.")
            url = reverse('bookings')
            return HttpResponseRedirect(url)


def check_booked_classes(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            booked_classes = Booking_class.objects.filter(
                trainers=request.user).order_by(requested_date)
            booked_classes_count = Booking_class.objects.count()
            if booked_classes_count == 0:
                messages.add_message(request, messages.ERROR,
                                     "Nothing booked.")
            url = reverse('home')
            return HttpResponseRedirect(url)
        else:
            booked_classes = BookPTSession.objects.filter(
                                user=request.user).order_by('requested_date')
            booked_classes_count = BookPTSession.objects.count()
            if booked_classes_count == 0:
                messages.add_message(
                    request, messages.ERROR,
                    "Nothing booked yet. Please book your training.")
                url = reverse('booking')
                return HttpResponseRedirect(url)
        template = 'pt_bookings/booked_classes.html'
        context = {
            'classes': booked_classes
        }

        return render(request, template, context)
