from django import forms
from thurs.models import *

class Topicmodelforms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpagemodelforms(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'


class Accessrecordsmodelforms(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'




