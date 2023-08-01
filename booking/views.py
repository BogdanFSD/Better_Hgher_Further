from django.conf import settings
from django.utils import formats
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BookingClass
from .forms import Booking_class_form
from django.contrib.auth.decorators import login_required
import datetime


def check_if_available(user_requested_trainers, user_requested_date,
                       user_requested_time, booking_id=None):
    if booking_id:
        booking_slot = len(BookingClass.objects.filter(
            trainers=user_requested_trainers,
            requested_date=user_requested_date,
            requested_time=user_requested_time).exclude(booking_id=None))

    else:
        booking_slot = len(BookingClass.objects.filter(
            trainers=user_requested_trainers,
            requested_date=user_requested_date,
            requested_time=user_requested_time))

    return booking_slot

# @login_required#


@login_required
def booking_training(request):
    if request.method == 'GET':

        booking_class = Booking_class_form()

        return render(request, "booking/booking.html", {'Booking_class_form':
                                                        Booking_class_form})
    else:
        if request.method == 'POST':
            booking_class_form = Booking_class_form(data=request.POST)
            if booking_class_form.is_valid():
                user_requested_trainers = request.POST.get('trainers')
                user_requested_date = request.POST.get('requested_date')
                user_requested_time = request.POST.get('requested_time')

                bookin_available = check_if_available(user_requested_trainers,
                                                      user_requested_date,
                                                      user_requested_time)

                if bookin_available > 0:
                    messages.add_message(
                        request, messages.ERROR,
                        "This time and date already booked"
                        f"{user_requested_time} on {user_requested_date}.")

                    return render(request, 'booking/booking.html',
                                  {'Booking_class_form': Booking_class_form})

                else:
                    booking_data = Booking_class_form(data=request.
                                                      POST).save(commit=False)
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
                        'booking/booking.html',
                        {'Booking_class_form': Booking_class_form})
        else:
            messages.add_message(
                request, messages.ERROR,
                "Sorry, something was not quite right. "
                "Please try again.")
            url = reverse('booking')
            return HttpResponseRedirect(url)


@login_required
def check_booked_training(request):

    if request.user.is_superuser:
        booked_classes = BookingClass.objects.filter(
            trainers=request.user).order_by('requested_date')
        booked_classes_count = BookingClass.objects.count()
        if booked_classes_count == 0:
            messages.add_message(request, messages.ERROR,
                                 "Nothing booked.")
        url = reverse('home')
        return HttpResponseRedirect(url)
    else:
        booked_classes = BookingClass.objects.filter(
                            user=request.user).order_by('requested_date')
        booked_classes_count = BookingClass.objects.count()
        if booked_classes_count == 0:
            messages.add_message(
                request, messages.ERROR,
                "Nothing booked yet. Please book your training.")
            url = reverse('booking')
            return HttpResponseRedirect(url)
    template = 'booking/booked.html'
    context = {
        'trainings': booked_classes
    }

    return render(request, template, context)


@login_required
def edit(request, booking_id):

    training_edit = get_object_or_404(BookingClass, pk=booking_id,
                                      user=request.user)

    if request.method == 'POST':
        booking_form = Booking_class_form(data=request.POST,
                                          instance=training_edit)

        if booking_form.is_valid():
            user_requested_trainers = request.POST.get('trainers')
            user_requested_date = request.POST.get('requested_date')
            user_requested_time = request.POST.get('requested_time')

            bookin_available = check_if_available(user_requested_trainers,
                                                  user_requested_date,
                                                  user_requested_time)

            if bookin_available > 0:
                messages.add_message(
                    request, messages.ERROR,
                    "This time and date already booked"
                    f"{user_requested_time} on {user_requested_date}.")

                return render(request, 'booking/edit.html',
                              {'booking_form': Booking_class_form})
            else:
                booking_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Your booking has been updated")
                url = reverse('booked')
                return HttpResponseRedirect(url)

        else:
            messages.add_message(
                request, messages.ERROR, "Sorry, edit was not successful.")
            url = reverse('booked')
            return HttpResponseRedirect(url)
    else:
        booking_form = Booking_class_form(instance=training_edit)

        template = 'booking/edit.html'
        context = {
            'booking_form': Booking_class_form,
            'training': training_edit,
            }
    return render(request, template, context)


@login_required()
def delete_booking(request, booking_id):

    if not request.user.is_authenticated:
        messages.add_message(
            request, messages.ERROR,
            "Sorry, you are not logged in."
            "Please login here.")
        url = reverse('account_login')
        return HttpResponseRedirect(url)

    booking_to_delete = get_object_or_404(BookingClass, pk=booking_id,
                                          user=request.user)
    booking_to_delete.delete()
    messages.add_message(
            request, messages.SUCCESS,
            "Booking has been cancelled")
    url = reverse('booked')
    return HttpResponseRedirect(url)
