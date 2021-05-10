from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

POWERS = (
  ('N', 'None'),
  ('B', 'Battery'),
  ('C', 'Corded'),
)

STAT = (
  ('N', 'Not Started'),
  ('I', 'In Progress'),
  ('C', 'Completed')
)

# Create your models here.
class Tool(models.Model):
  name = models.CharField(max_length=50)
  power = models.CharField(
    max_length=1,
    choices=POWERS,
    default=POWERS[0][0]
  )
  image = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('tools_detail', kwargs={'pk': self.id})


class Material(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=200)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('materials_detail', kwargs={'pk': self.id})


class Project(models.Model):
  title = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  budget = models.IntegerField('Budget ($ Dollars)')
  status = models.CharField(
    max_length=1,
    choices=STAT,
    default=STAT[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  tools = models.ManyToManyField(Tool)
  materials = models.ManyToManyField(Material)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('projects_detail', kwargs={'project_id': self.id})

