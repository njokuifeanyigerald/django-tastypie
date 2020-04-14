from tastypie.resources import ModelResource
from .models import Myway
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password','is_active', "is_staff", "is_superuser",'email']
        allowed_methods = ['get']


class MywayRescource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Myway.objects.all()
        resource_name = "myway"

user_rescource =  UserResource()
myway_resource = MywayRescource()


