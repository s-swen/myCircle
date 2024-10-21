from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from circle.models import Profile, Category, Contact
from datetime import date

class ProfileModelTest(TestCase):

    def test_profile_created_with_user(self):
        """Test if a Profile is automatically created when a User is created."""
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertTrue(Profile.objects.filter(user=user).exists())  # Check if the profile was created

    def test_profile_birthday(self):
        """Test setting and retrieving the birthday field in Profile."""
        user = User.objects.create_user(username='testuser2', password='12345')
        profile = Profile.objects.get(user=user)
        profile.birthday = date(1990, 1, 1)
        profile.save()

        # Ensure birthday is stored correctly
        self.assertEqual(profile.birthday, date(1990, 1, 1))


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        """Test creating a category and its string representation."""
        category = Category.objects.create(name='Professional')
        self.assertEqual(str(category), 'Professional')


class ContactModelTest(TestCase):

    def setUp(self):
        # Create a user and its profile
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.get(user=self.user)
        
        # Create a default category and a custom category
        self.default_category = 'friend'
        self.custom_category = Category.objects.create(name='Doctor')
        self.contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            user=self.profile,  # Link to the profile
            category=self.default_category
        )

    def test_contact_creation_default_category(self):
        """Test creating a Contact with a default category."""
        self.assertEqual(str(self.contact), 'John Doe')
        self.assertEqual(self.contact.get_category(), 'Friend')  # Default category

    def test_contact_creation_custom_category(self):
        """Test creating a Contact with a custom category."""
        contact = Contact.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane@example.com',
            user=self.profile,
            custom_category=self.custom_category
        )
        self.assertEqual(str(contact), 'Jane Smith')
        self.assertEqual(contact.get_category(), 'Doctor')  # Custom category takes precedence

    def test_get_absolute_url(self):
        '''Test the expected URL using reverse function'''
        expected_url = reverse('contact-detail', args=[str(self.contact.id)])
        self.assertEqual(self.contact.get_absolute_url(), expected_url)
