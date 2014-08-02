from django import forms
from django.forms import ModelForm

from logic.xml_parser import get_child_name
from models import Configuration


class ConfigurationForm(ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'username'}))
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'password'}))

    class Meta:
        model = Configuration
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'password'}),
            'username': forms.TextInput(attrs={'class': 'username'}),
            'pipeline_url': forms.TextInput(attrs={'class': 'url'}),
        }
        fields = ['pipeline_url', 'username', 'password']


def multi_choice_fields(build):
    return tuple([build, build])


def get_all_build_names(builds):
    build_names = map(get_child_name, builds)
    build_names = tuple(map(multi_choice_fields, build_names))
    return build_names


class BuildForm(forms.Form):
    def __init__(self, *args, **kwargs):
        build_names = get_all_build_names(kwargs.pop('all_builds'))
        super(BuildForm, self).__init__(*args, **kwargs)
        self.fields['builds'] = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
                                                          choices=build_names)