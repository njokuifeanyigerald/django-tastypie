from django.urls import path, include
from .api import myway_resource, user_rescource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(myway_resource)
api.register(user_rescource)



urlpatterns = [
    # The normal jazz here...
    path('api/', include(api.urls)),
]
