from django.forms import ModelForm
from .models import Profile
from phonenumber_field.modelfields import PhoneNumber


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'user_pic', 'email', 'birthday')
        labels = {
            'name': 'ФИО',
            'user_pic': 'Фото',
            'email': 'Электронная почта',
            'birthday': 'Дата рождения',
        }


