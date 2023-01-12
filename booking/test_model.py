from django.test import TestCase
from django.contrib.auth.models import User
from pt_bookings.models import Booking_class
# Create your tests here.


class TestBookingClassModel(TestCase):
    """
    Testing Model
    """
    def start(self):
        """
        Create user, trainer and book
        """
    test_trainer = User.objects.create_user(
        username='test_trainer', password='treiner', is_staff=True
    )

    test_user = User.objects.create_user(
            username='test', password='First123')

    self.booking = Booking_class(
        user=test_user,
        staff=test_staff.username,
        requested_time='11:00',
        status='In progress',
        requested_date='2022-01-15',
    )

    def test_create_booking(self):
        """
        This test tests the booking of a PT session
        """
        self.assertEqual(self.booking.user.username, 'tester')
        self.assertEqual(self.booking.staff, 'test_staff')
        self.assertEqual(self.booking.requested_date, '2022-01-15')
        self.assertEqual(self.booking.requested_time, '10:00')
        self.assertEqual(self.booking.status, 'In progress')
