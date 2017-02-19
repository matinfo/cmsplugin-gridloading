# -*- coding: utf-8 -*-
from django import forms
from django.template import TemplateDoesNotExist
from django.template.loader import select_template

from .models import GridloadingPlugin



class GridloadingPluginForm(forms.ModelForm):

    class Meta:
        fields = [
            'effect',
        ]
        model = GridloadingPlugin

#class GridloadingItemPluginForm(django.forms.ModelForm):
#
#    class Meta:
#        fields = ['image', 'content', 'link_text']
#        model = models.GridloadingItemPlugin

