from re import T
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.conf import settings
#from django_countries.fields import CountryField

# Create your models here.

class Post(models.Model):
  title = models.CharField(
    max_length = 100,
    validators = [MinLengthValidator(5, 'Book Title must be greator than 5 characters')]
  )
  description = models.TextField(
    max_length = 500,
    #validators = [MinLengthValidator(50, 'Minimum Description must be 50 words')],
    blank = True,
    null = True,
    default = '',
  )
  
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
  author = models.CharField(
    max_length = 100,
    validators = [MinLengthValidator(5, 'Author(s) must be greator than 5 characters')]
  )
  
  publisher = models.CharField(max_length=100, blank = True, null=True)
  
  years = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title
  
class Image(models.Model):
  owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="image")
  
  # stores multiple images urls as single string, seperate by ' '
  image_url = models.CharField(
    max_length = 255
  )
  
  image_public_id = models.CharField(
    max_length= 255,
    default=''
  )
  
class Trade(models.Model):
  STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
      )

  requester = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='requested_trades', on_delete=models.CASCADE)
  offerer_book = models.ForeignKey('Post', related_name='offered_trades', on_delete=models.CASCADE)
  offerer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='offered_trades', on_delete=models.CASCADE)
  
  status = models.CharField(
    max_length=20, 
    choices=STATUS_CHOICES, 
    default='pending'
  )

  def __str__(self):
      return f"Trade #{self.id}"
