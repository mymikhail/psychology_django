from django.db import models

class Test(models.Model):
    test_id = models.AutoField(max_length=10)
    title = models.CharField(max_length=250)
    description = models.CharField()

class AnalyzingTest(models.Model):
    test_id = models.ForeignKey(Test)
    num1 = models.IntegerField(max_length=5)
    num2 = models.IntegerField(max_length=5)
    description = models.CharField()

class Question(models.Model):
    question_id = models.AutoField(max_length=10)
    description = models.CharField(max_length)
    order = models.IntegerField(max_length=3)
    test_id = models.ForeignKey(Test)

class Variation(models.Model):
    variation_id = models.AutoField(max_length=10)
    question_id = models.ForeignKey(Question)
    variation = models.CharField(max_length=255)
    value = models.IntegerField(max_length=4)

class User(models.Model):
    user_id = models.AutoField(max_length=10)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.CharField()
    email = models.CharField(max_length=100)

class Testing(models.Model):
    testing_id = models.AutoField(max_length=10)
    test_id = models.ForeignKey(Test)
    user_id = models.ForeignKey(User)
    date_created = models.DateTimeField()

class UserTesting(models.Model):
    testing_id = models.ForeignKey(Testing)
    variation_id = models.ForeignKey(Variation)

