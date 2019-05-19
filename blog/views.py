from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
#import the post from models.py
from .models import Provider
from .serializers import providerSerializer
from django.http import JsonResponse
from rest_framework import viewsets



def ProvidersView(request):
    providers = Provider.objects.all()

    serializer = providerSerializer(providers, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return render(request, 'blog/ProvidersView.html', {'providers': providers})


class providers(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = providerSerializer
    queryset = Provider.objects.all()
    

"""
class providers(APIView):

	def get(self, request):
		
		content = {'message': 'Hello Ben, Below is Providers Database:'}
		return Response(content)
"""