from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','phone','city','birth_date','experience','programming_lang','current_ctc','expect_ctc','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'birth_date': forms.TextInput(attrs={'class':'form-control'}),
            'experience': forms.TextInput(attrs={'class':'form-control'}),
            'programming_lang': forms.TextInput(attrs={'class':'form-control'}),
            'current_ctc': forms.TextInput(attrs={'class':'form-control'}),
            'expect_ctc': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }