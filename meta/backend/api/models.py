from django.db import models


class Profile(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=1000, null=False, blank=False)
    name = models.CharField(max_length=50)
    photo = models.URLField()
    methods = models.ManyToManyField('Skills', related_name='skills')

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Launch(models.Model):
    update = models.DateTimeField(auto_now=True, db_index=True)
    data = models.TextField()


