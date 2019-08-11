from . import views
from django.urls import path
urlpatterns = [
        path('',views.income,name='income_home'),
         path('del/<int:id>', views.delete_income, name='income_del'),
        path('edit/<int:id>', views.income_edit, name='income_edit'),
        path('create/',views.create,name='income_create'),
]
