# The models tab provides the objects that are used inside of the website. Each object inherits from the model class
from django.db import models
from django.contrib.auth.models import User


class Experience(models.Model):
    cover_image = models.ImageField(upload_to='images/', null=True)
    images = models.ManyToManyField('Image')
    title = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    location = models.CharField(max_length=100)
    summary = models.CharField(max_length=100, null=True)
    description = models.TextField()
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.title


class Education(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    institution = models.CharField(max_length=100)
    degreeName = models.CharField(max_length=100)
    degreeTitle = models.CharField(max_length=15)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    description = models.TextField()

    class Meta:
        # Meta allows for MetaData to be added to a class, including plural and singular forms of words
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.institution


class Cert(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    issueDate = models.DateField()
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return self.title


class Activity(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    field = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.title


class Project(models.Model):
    cover_image = models.ImageField(upload_to='images/', null=True)
    images = models.ManyToManyField('Image')
    title = models.CharField(max_length=100)
    skills = models.ManyToManyField('Skill')
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    description = models.TextField()
    summary = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title


class Award(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    issueDate = models.DateField()
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Awards'

    def __str__(self):
        return self.title

