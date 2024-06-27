
from django.test import TestCase
from django.urls import reverse

from test_task.models import Page, Worker



class TestTaskViewsTests(TestCase):
    def setUp(self):
        self.user = Worker.objects.create_user(
            username='testuser',
            password='<PASSWORD>',
        )
        self.page = Page.objects.create(
            title='Test Page',
            content='Test Page content',
            created_by=self.user,
        )

    def test_page_view(self):
        response = self.client.get(reverse("task_task:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get(reverse("task_task:page", args=[self.page.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.page.title)
        self.assertContains(response, self.page.content)
