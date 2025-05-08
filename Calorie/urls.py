from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views  # Import the views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('index/', views.index, name='index'),
    path('delete/<int:id>/',views.delete_consume,name="delete"),  # Add this line to include the index view
    path('add_item/', views.add_item, name='add_item'),
    path('set_goal/', views.set_goal, name='set_goal'),
    path('food_list/', views.food_list, name='food_list'),
    path('food_delete/<int:id>/', views.delete_food, name='food_delete'),
    path('food_update/<int:id>/', views.update_food, name='food_update'),
    path('report/', views.report, name='report'),
    path('report/pdf/', views.report_pdf, name='report_pdf'),

    # Authentication URLs
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
]
