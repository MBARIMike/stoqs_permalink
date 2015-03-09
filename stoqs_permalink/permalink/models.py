import uuid
from django.contrib.gis.db import models

class UUIDField(models.CharField) :
    '''
    Major classes in the model have been given a uuid field, which may prove helpful as web accessible resource identifiers.
    '''
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 32 )
        models.CharField.__init__(self, *args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if add :
            value = getattr(model_instance,self.attname)
            if not value:
                value = unicode(uuid.uuid4()).replace('-','')
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)


class Permalink(models.Model):
    '''
    A simple model for storing permalinks created by users.
    '''
    uuid = UUIDField(editable=False, primary_key=True)
    parameters = models.TextField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    usage_count = models.IntegerField(default=0)
    last_usage = models.DateTimeField(auto_now=True)
