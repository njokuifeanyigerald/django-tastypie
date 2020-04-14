from tastypie.resources import ModelResource
from .models import Myway
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import BasicAuthentication,ApiKeyAuthentication
from tastypie.models import create_api_key
from django.db.models import signals
from tastypie.authorization import DjangoAuthorization

signals.post_save.connect(create_api_key, sender=User)

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password','is_active', "is_staff", "is_superuser",'email']
        allowed_methods = ['get']
        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()


class MywayRescource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Myway.objects.all()
        resource_name = "myway"
        
        authentication = ApiKeyAuthentication()



user_rescource =  UserResource()
myway_resource = MywayRescource()


