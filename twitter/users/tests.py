# from django.test import TestCase
# from .models import DocCustomUser, Education, Experience
# from datetime import date

# # Create your tests here.
# class DocUserTestCase(TestCase):
#     def setUp(self):
#         self.doc1 = DocCustomUser.objects.create(username='johndoe', email='johndoe', password='passsword')
#         self.doc2 = DocCustomUser.objects.create(
#             username='kimdee',
#             email ='kimdee@email.com',
#             password='passsword',
#             company = 'Kenyatta University',
#             website = 'www.johndoe.com',
#             location = 'Nairobi, Kenya',
#             skills = 'mental health, consultation',
#             bio = 'I am a doctor'
#             )
        
#     def test_docuser(self):
#         self.assertEqual(self.doc1.username, 'johndoe')
#         self.assertEqual(self.doc2.company, 'Kenyatta University')

# class EducationTestCase(TestCase):
#     def setUp(self):
#         self.doc1 = DocCustomUser.objects.create(
#             username='kimdee',
#             email ='kimdee@email.com',
#             password='passsword',
#             company = 'Kenyatta University',
#             website = 'www.johndoe.com',
#             location = 'Nairobi, Kenya',
#             skills = 'mental health, consultation',
#             bio = 'I am a doctor'
#             )
#         self.edu1 = Education.objects.create(
#             user = self.doc1,
#             title = "Kenyatta University",
#             company = "Kenyatta University",
#             location = "Medicine and Surgery",
#             from_date = date(2012, 12, 4),
#             to_date = date(2016, 12, 8),
#             current = False,
#             description = "Lorem Ipsum"
#         )

#     def test_experience(self):
#         self.assertEqual(self.edu1.title, 'Kenyatta University')
#         self.assertEqual(self.edu1.user.username, 'kimdee')

# class ExperienceTestCase(TestCase):
#     def setUp(self):
#         self.doc1 = DocCustomUser.objects.create(
#             username='kimdee',
#             email ='kimdee@email.com',
#             password='passsword',
#             company = 'Kenyatta University',
#             website = 'www.johndoe.com',
#             location = 'Nairobi, Kenya',
#             skills = 'mental health, consultation',
#             bio = 'I am a doctor'
#             )
#         self.edu1 = Experience.objects.create(
#             user = self.doc1,
#             school = "Kenyatta University",
#             degree = "Medicine and Surgery",
#             field_of_study = "Medicine",
#             from_date = date(2012, 12, 4),
#             to_date = date(2016, 12, 8),
#             current = False,
#             description = "Lorem Ipsum"
#         )

#     def test_experience(self):
#         self.assertEqual(self.edu1.degree, 'Medicine and Surgery')
#         self.assertEqual(self.edu1.user.username, 'kimdee')