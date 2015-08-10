from audioop import reverse
from datetime import timezone, datetime
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from app1.models import Rating


class RatingMethodTest(TestCase):

    def test_was_recently_published_old_rating(self):
        time = timezone.now() - datetime.timedelta(days=30)
        rating = Rating(rater=2, movie=44, rating=5, timestamp=time)

        self.assertFalse(rating.was_published_recently(), "Rating not recent")

    def test_was_recently_published_future_rating(self):
        time = timezone.now() + datetime.timedelta(days=10)
        rating = Rating(rater=2, movie=44, rating=5, timestamp=time)

        self.assertFalse(rating.was_published_recently(), "Rating not recent")


class RatingViewTests(TestCase):
    def test_detail_rater_404(self):
        url = reverse('detail_rater', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404, msg='not found')

    def test_detail_rater_return_new_rating(self):
        test_user = User.objects.create_user('test', 'test@test.com', 'pass')
        test_user.save()
        time = timezone.now()
        rating = Rating(rater=1, movie=3, rating=5, timestamp=time)
        rating.save()

        response = self.client.get(reverse('detail_rater', args=[rater.id]))
        self.assertContains(response, 'Testing')