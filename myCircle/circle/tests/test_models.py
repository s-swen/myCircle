from django.test import TestCase
from django.contrib.auth.models import User
from circle.models import Profile, Category, Contact

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, birthday='1990-01-01')

    def tearDown(self):  # Added tearDown method
        self.user.delete()
        self.profile.delete()

    def test_profile_creation(self):
        self.assertEqual(str(self.profile), "testuser's Profile")
        self.assertEqual(self.profile.birthday, '1990-01-01')

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Friend')

    def tearDown(self):  # Added tearDown method
        self.category.delete()

    def test_category_creation(self):
        self.assertEqual(str(self.category), 'Friend')

class ContactModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, birthday='1990-01-01')
        self.category = Category.objects.create(name='Professional')
        self.contact = Contact.objects.create(
            first_name='John', 
            last_name='Doe', 
            email='john@example.com',
            phone_number='123456789',
            birthday='1980-02-02',
            last_contact='2024-01-01',
            work='Software Engineer',
            note='Met at a conference',
            instagram_handle='@john',
            linkedin_url='https://www.linkedin.com/in/johndoe',
            category='professional',
            custom_category=self.category,
            user=self.profile
        )

    def tearDown(self):  # Added tearDown method
        self.contact.delete()
        self.category.delete()
        self.profile.delete()
        self.user.delete()

    def test_contact_creation(self):
        self.assertEqual(str(self.contact), 'John Doe')
        self.assertEqual(self.contact.email, 'john@example.com')
        self.assertEqual(self.contact.phone_number, '123456789')
        self.assertEqual(self.contact.work, 'Software Engineer')
        self.assertEqual(self.contact.note, 'Met at a conference')
        self.assertEqual(self.contact.instagram_handle, '@john')
        self.assertEqual(self.contact.linkedin_url, 'https://www.linkedin.com/in/johndoe')
        self.assertEqual(self.contact.get_category(), 'Professional')

    def test_default_category(self):
        contact_no_custom = Contact.objects.create(
            first_name='Jane', 
            last_name='Smith', 
            email='jane@example.com',
            user=self.profile
        )
        self.assertEqual(contact_no_custom.get_category(), 'Friend')  # Default category
        contact_no_custom.delete()  # Added clean-up for this contact
