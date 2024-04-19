from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


app_name = 'discover'
urlpatterns = [
    path('register',views.RegisterView.as_view(),name='register'),
    path('main/',TemplateView.as_view(template_name='discover/main.html'),name = 'main'),
    path('contact/',TemplateView.as_view(template_name='discover/contact.html'),name = 'contact'),
    path('about/',TemplateView.as_view(template_name='discover/main.html'), name='about'),
    path('rewards/',TemplateView.as_view(template_name='discover/rewards.html'),name = 'rewards'),
    
    path('', views.DiscoverListView.as_view(), name='all'),
    path('form/', views.PostCreateView.as_view(), name='submitForm'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='deleteForm'),
    path('update/<int:pk>',views.PostEditView.as_view(), name='editForm'),
    path('detail/<int:pk>',views.PostDetailView.as_view(), name='detail'),
    path('tradeForm/<int:bookId>',views.TradeCreateView.as_view(), name='tradeForm'),
    path('myListing/<int:myList>',views.MyListView.as_view(), name='myListing'),
    path('requests',views.RequestView.as_view(), name='myRequests'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defineds