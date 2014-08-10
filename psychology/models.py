from django.db import models

class Test(models.Model):
    test_id = models.AutoField(max_length=10, primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title    

class AnalyzingTest(models.Model):
    test_id = models.ForeignKey(Test)
    num1 = models.IntegerField(max_length=5)
    num2 = models.IntegerField(max_length=5)
    description = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description

class Question(models.Model):
    question_id = models.AutoField(max_length=10, primary_key=True)
    description = models.TextField()
    order = models.IntegerField(max_length=3)
    test_id = models.ForeignKey(Test)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.description    

class Variation(models.Model):
    variation_id = models.AutoField(max_length=10, primary_key=True)
    question_id = models.ForeignKey(Question)
    variation = models.CharField(max_length=255)
    value = models.IntegerField(max_length=4)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.variation    

class User(models.Model):
    user_id = models.AutoField(max_length=10, primary_key=True)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.login    

class Testing(models.Model):
    testing_id = models.AutoField(max_length=10, primary_key=True)
    test_id = models.ForeignKey(Test)
    user_id = models.ForeignKey(User)
    date_created = models.DateTimeField()

class UserTesting(models.Model):
    testing_id = models.ForeignKey(Testing)
    variation_id = models.ForeignKey(Variation)