from . import views
from django.urls import path
from hotel.views import IndexView, EmpView

urlpatterns = [
    path('',IndexView.as_view()),
    path('emp',EmpView.as_view()),


]