from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_national_code(self):
        national_code = self.cleaned_data['national_code']
        if len(national_code) != 10:
            raise forms.ValidationError("invalid national code")

        return national_code

    def clean_full_name(self):
        name = self.cleaned_data['full_name'].split()

        if len(name) != 2:
            raise forms.ValidationError('We need both')
        else:
            first_name = name[0]
            last_name = name[1]

            if not first_name.istitle() or not last_name.istitle():
                raise forms.ValidationError('is not title')
            
        return name