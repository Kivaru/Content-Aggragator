from django.db import models
 
# Create your models here.
class PyContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  class Meta:
    app_label = 'PyContent'
  def __str__(self):
    return self.headline

 
class ProgContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  class Meta:
    app_label = 'ProgContent'
  def __str__(self):
    return self.headline

 
class HiringContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  class Meta:
    app_label = 'HiringContent'
  def __str__(self):
    return self.headline
 
class CovidContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  class Meta:
    app_label = 'CovidContent'
  def __str__(self):
    return self.headline

  