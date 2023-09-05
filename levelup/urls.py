from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from levelupapi.views import GameTypeView, GameView, EventView, GamerView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')
router.register(r'gamers', GamerView, 'gamer')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

""" # Requests to http://localhost:8000/register will be routed to the register_user function
path('register', register_user)
# Requests to http://localhost:8000/login will be routed to the login_user function
path('login', login_user) """
