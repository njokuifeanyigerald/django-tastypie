from django.urls import path, include
from .api import tastypie_resource

# entry_resource = EntryResource()

urlpatterns = [
    # The normal jazz here...
    path('api/', include(tastypie_resource.urls)),
]
