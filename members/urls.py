from django.urls import path
from . import views


#URL CONFIGURATION 
urlpatterns = [
    path('home/', views.members),
    path('test/',views.test ),
    path('Add/',views.AddMember ),
    path('display/',views.DisplayMemebrs ),
    path('update/<int:id>/', views.UpdateMemebers, name='update'),
    path('delete/<int:id>/', views.DeleteMember, name='delete'),
]


