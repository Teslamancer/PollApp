import datetime

from django.utils import timezone
from django.test import TestCase
from polls.models import Question

class myTestClass(TestCase):
    
    def testMethod(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
        