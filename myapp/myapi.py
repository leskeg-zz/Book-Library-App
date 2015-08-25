# tastypie resources.
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from myapp.models import *

class PublisherResource(ModelResource):
	class Meta:
		queryset = Publisher.objects.all()
		resource_name = 'publisher'
		authorization= Authorization()

class BookResource(ModelResource):
	publisher = fields.ForeignKey(PublisherResource, 'publisher', full='true')
	class Meta:
		queryset = Book.objects.all()
		resource_name = 'book'
		authorization= Authorization()
