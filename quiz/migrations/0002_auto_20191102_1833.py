# Generated by Django 2.2.1 on 2019-11-02 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsub',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='user.Item', verbose_name='도구'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quizSub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizSubs', to='quiz.QuizSub', verbose_name='퀴즈주제'),
        ),
        migrations.AddField(
            model_name='myquiz',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizs', to='quiz.Quiz', verbose_name='퀴즈'),
        ),
        migrations.AddField(
            model_name='myquiz',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myQuizs', to=settings.AUTH_USER_MODEL, verbose_name='회원'),
        ),
        migrations.CreateModel(
            name='QuizCorrect',
            fields=[
            ],
            options={
                'verbose_name': '문제 정답률',
                'verbose_name_plural': '문제 정답률',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('quiz.quiz',),
        ),
    ]
