from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Task


class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.task = Task.objects.create(title='Test task',
                                        description='Test description',
                                        user=self.user)
        self.url = reverse('tasks-list')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_create_task(self):
        data = {'title': 'New task', 'description': 'New description', 'user': self.user.id}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=2).title, 'New task')

    def test_update_task(self):
        data = {'title': 'Updated task',
                'description': 'Updated description'}
        response = self.client.put(reverse('tasks-detail',
                                           args=[self.task.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task.id).title, 'Updated task')

    def test_delete_task(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('tasks-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
