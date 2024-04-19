from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Post, Image, Trade
from .forms import PostForm, RegisterForm, ImageForm, TradeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
import cloudinary
import cloudinary.uploader
from django.conf import settings
from django.core.files import File

# Create your views here.

class DiscoverListView(ListView):
  model = Post
  template_name = 'discover/list.html'
  context_object_name = 'posts'

  
class PostCreateView(LoginRequiredMixin,CreateView):
  model = Post
  template_name = 'discover/post_form.html'
  success_url = reverse_lazy('discover:all')
  store_folder = 'bookExchange'
  
  def get(self,request):
    form1 = PostForm()
    form2 = ImageForm()
    return render(request,self.template_name,{'form1':form1 , 'form2':form2})
  
  def post(self,request):
    newForm = PostForm(request.POST)       # create form object
    newFormImg = ImageForm(request.FILES)  # create form object

    if newForm.is_valid() and newFormImg.is_valid():
      posting = newForm.save(commit=False)  #PostForm object with save function gives back model object
      posting.owner = self.request.user
      posting.save() # save post model object into database
      
      # request.FILES.getlist('image_url') gives UploadedFile objects, newFormImg.cleaned_data['image_url'] gives InMemoryUploadedFile objects
      # working with UploadedFile object more straightforward, InMemoryUploadedFile might access binary content without explicitly calling read()
      for image in request.FILES.getlist('image_url'):
        # Handle Cloudinary upload
        uploaded_image_url = cloudinary.uploader.upload(
          file = image,
          folder = self.store_folder
        )
        
        instance = Image(
          owner=self.request.user, 
          post= posting,
          image_url = uploaded_image_url['secure_url'],
          image_public_id = uploaded_image_url['public_id'],
        )
        
        instance.save()
      
      return redirect(self.success_url)
    else:
      return render(request,self.template_name,{'form1':newForm,'form2':newFormImg})
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
  model = Post
  template_name = 'discover/delete_form.html'
  success_url = reverse_lazy('discover:all')
  
  def get_queryset(self):
    qs = super(PostDeleteView,self).get_queryset()
    return qs.filter(owner=self.request.user)
  
  def post(self,request,pk):
    # Get the object to delete
    post_instance = self.get_object()
    # public_id = post_instance.image_public_id

    # Delete the photo from Cloudinary
    for image in post_instance.image.all():
      cloudinary.uploader.destroy(image.image_public_id)
      image.delete()

    return super(PostDeleteView,self).post(request,pk)
  
class PostEditView(LoginRequiredMixin,UpdateView):
  model = Post
  template_name = 'discover/post_form.html'
  success_url = reverse_lazy('discover:all')
  
  def get(self,request,pk):
    post = get_object_or_404(Post, id=pk, owner=self.request.user)
    form1 = PostForm(instance=post)
    return render(request,self.template_name,{'form1':form1})
  
  def post(self,request,pk=None):
    old_post = get_object_or_404(Post,id=pk,owner=self.request.user)

    form1 = PostForm(request.POST,request.FILES,instance=old_post)
    
    if not form1.is_valid():
      return render(request,self.template_name,{'form1':form1 })
    
    # if 'image_url' in form.changed_data:
    #   # destroy old pic
    #   cloudinary.uploader.destroy(old_post.image_public_id)
    #   new_post = form.save(commit=False,upload=True)
    # else:
    #   new_post = form.save(commit=False,upload=False) 
       
    # new_post.save()
    
    form1.save()
    
    return redirect(self.success_url)

class PostDetailView(DetailView):
  model = Post
  template_name='discover/detail.html'

# Account Register View
class RegisterView(View):
  success_url = reverse_lazy('login')
  template_name = 'registration/register.html'
  
  def get(self,request):
    form = RegisterForm()
    
    return render(request,self.template_name,{'form':form})
  
  def post(self,request):
    form = RegisterForm(request.POST)
    
    if not form.is_valid():
      return render(request,self.template_name,{'form':form})
    
    form.save()
    
    return redirect(self.success_url+"?next=" + reverse_lazy('discover:all'))
  
  
class TradeCreateView(LoginRequiredMixin,CreateView):
  model = Trade
  template_name = 'discover/trade_form.html'
  success_url = reverse_lazy('discover:all')
  
  def get(self,request,bookId):
    
    offererBook = get_object_or_404(Post, id=bookId)    
    
    form = TradeForm(initial={
      'offerer_book':offererBook,
      'offerer':offererBook.owner,
      'requester':request.user,
    })
    
    return render(request,self.template_name,{'form':form})
  
  def post(self,request,bookId = None):
    newForm = TradeForm(request.POST)       # create form object

    if newForm.is_valid():
      posting = newForm.save(commit=False)  #PostForm object with save function gives back model object
      posting.save() # save post model object into database
      
      return redirect(self.success_url)
    else:
      print(newForm.errors)
      return render(request,self.template_name,{'form':newForm })
    
    
# personal listing view
class MyListView(ListView):
  model = Post
  template_name = 'discover/myList.html'
  context_object_name = 'posts'
  
  def get_queryset(self):
    qs = super(MyListView,self).get_queryset()
    return qs.filter(owner=self.request.user)
  
# personal listing view
class RequestView(ListView):
  model = Trade
  template_name = 'discover/trades.html'
  context_object_name = 'trades'
  
  def get_queryset(self):
    qs = super(RequestView,self).get_queryset()
    return qs.filter(offerer=self.request.user)