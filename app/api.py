from tastypie.resources import ModelResource
from .models import Tastypie


class TastypieResource(ModelResource):
    class Meta:
        queryset = Tastypie.objects.all()
        resource_name = 'tastypie'

tastypie_resource = TastypieResource()