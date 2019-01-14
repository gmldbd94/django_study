Django 공부

    ##Django Project
    django-admin startproject <project 이름>

    ##manage.py로 서버 작동
    python manage.py runserver



App

프로젝트의 구성 단위

    python manage.py startapp <app 이름>

app 이름으로 된 폴더

File

File

File

File



가상환경 들어가는 방법

    source ~/.virtualenvs/myvenv/bin/activate



Basic testing startegies

1. python manage.py shell
       >>> import datetime
       >>> from django.utils import timezone
       >>> from polls.models import Question
       >>> # create a Question instance with pub_date 30 days in the future
       >>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
       >>> # was it published recently?
       >>> future_question.was_published_recently()
       True


1. Create a test to expose the bug
       polls/tests.py¶
       import datetime

       from django.test import TestCase
       from django.utils import timezone

       from .models import Question


       class QuestionModelTests(TestCase):

           def test_was_published_recently_with_future_question(self):
               """
               was_published_recently() returns False for questions whose pub_date
               is in the future.
               """
               time = timezone.now() + datetime.timedelta(days=30)
               future_question = Question(pub_date=time)
               self.assertIs(future_question.was_published_recently(), False)
   https://docs.djangoproject.com/en/2.1/intro/tutorial05/ 참고할것
