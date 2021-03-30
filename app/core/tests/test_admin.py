from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    #setup before running tests

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='admin@lomndonappdev.com',password='testpass123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='admin@londonappdev.com',password='testpassuser123',name='Sai')


    def tests_users_listed(self):
        url = reverse('admin:core_user_changelist') #defined in django admin doc
        res = self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)

    #not recommending testing features specific to framework
    def test_user_change_page(self):
        url = reverse('admin:core_user_change',args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
