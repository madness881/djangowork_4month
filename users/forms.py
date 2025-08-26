from django import forms

class RegisterForm(forms.Form):
    avatar = forms.ImageField(required=False)
    age = forms.IntegerField(required=False)
    username = forms.CharField( max_length=150, required=True)
    password = forms.CharField(required=True)
    password_confirm = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    
class LoginForm(forms.Form):
        username = forms.CharField(max_length=150, required=True)
        password = forms.CharField(required=True, widget=forms.PasswordInput)