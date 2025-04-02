from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('import/', views.add_teams, name='import'),
    path('edit/<int:team_id>/', views.edit_team, name='edit_team')
]
