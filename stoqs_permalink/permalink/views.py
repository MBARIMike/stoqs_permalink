# permalink/views.py
from rest_framework.generics import CreateAPIView
from django.views.generic import CreateView

from .models import Permalink
from braces.views import LoginRequiredMixin

class PermalinkActionMixin(object):
    fields = ('parameters', )
    
class PermalinkCreateView(LoginRequiredMixin, CreateView):
    model = Permalink
    fields = ('parameters', )

##class PermalinkUpdateCreateView(ListCreateAPIView):
##    model = Permalink

 
