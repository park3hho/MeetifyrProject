from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class FeeddAPITestCase(APITestCase):
    # 각 테스트 메소드가 실행되기 전에 호출되는 메소드
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.feed1 = Feed.objects.create(user=self.user, title='Title1')
        self.feed2 = Feed.objects.create(user=self.user, title='Title2')
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token.access_token))
    def test_get_all_feeds(self):
        url = reverse('feed-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),2) # 피드가 2개 생성되었으므로 2개가 반환되어야 함

    def test_get_feed_detail(self):
        url = reverse('feed-detail', kwargs={'feed_id':1})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 7)  # 피드 상세 정보는 4개의 필드를 포함해야 함
        self.assertEqual(res.data['content'], self.feed1.content)  # 피드 제목이 일치해야 함

    def test_create_feed(self):
        # self.client.login(username='testuser', password='password')
        url = reverse('feed-list')
        data = {
            'title': 'New Feed',
            'content': 'This is a new feed content.'
        }
        res = self.client.post(url, data, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feed.objects.count(), 3)  # 피드가 하나 더 생성되어야 함
        self.assertEqual(Feed.objects.last().content, 'New Feed')    