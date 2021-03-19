from django.forms import ModelForm
from pools.models import *

class Form_Register(ModelForm):
    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(Form_Register, self).__init__(*args, **kwargs)

    class Meta():
        model = User
        fields = '__all__'
        widgets = {
            # 'password': forms.PasswordInput(),
        }