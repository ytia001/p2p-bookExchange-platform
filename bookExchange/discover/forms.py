from django import forms 
from .models import Post, Image, Trade
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import cloudinary
import cloudinary.uploader

class PostForm(forms.ModelForm):
  # CHOICES = [(i,str(i)) for i in range(11)]
  # rating = forms.ChoiceField(choices=CHOICES,required=True)
  
  class Meta:
    model = Post
    fields = ['title','description','author','publisher', 'years']
    
    #Customize lables in form
    labels = {
      'title': 'Book Title',
      'description': 'Summary',
      'author': 'Author(s)',
      'years' : 'Duration of Book Ownership'
    }
    
    #Customize widgets for better UX 
    widgets = {
        #'country': forms.Select(attrs={'class': 'form-control'}),
        # 'rating': forms.Select(attrs={'class':'form-control'})
    }
    
  
# image submission Form, ONLY forms.ModelForm have save(), forms.Form do not have save()
class ImageForm(forms.ModelForm):
  image_url = forms.FileField(
      required=True,
      label='Upload Picture(s) of the Book',
      widget= forms.TextInput(attrs={
        "type":"File",
        "class":"form-control",
        "multiple": "True",
        #"accept" : "image/*"
      })
    )
  
  class Meta:
    model = Image
    fields = ['image_url']
  
# Registration Form 
class RegisterForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','password1','password2']
    
# Trade Form 
class TradeForm(forms.ModelForm):

  class Meta:
    model = Trade
    fields = ['requester','offerer_book','offerer']
    
    #Customize lables in form
    labels = {
    }


    