from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:   
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist!')
                
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(label = 'Email Address')
    password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        #password = self.cleaned_data.get('password')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email has already been taken')
        
        return super(UserRegisterForm, self).clean(*args, **kwargs)
