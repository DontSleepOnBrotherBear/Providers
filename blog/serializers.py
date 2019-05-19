from rest_framework import serializers
from .models import Provider, Address

class providerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Provider
		fields = ('firstName', 'lastName', 'PVaddress')
	