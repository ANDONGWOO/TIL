from django.contrib.auth.forms import UserCreationForm,UserChangeForm#상속1/상속2

from django.contrib.auth import get_user_model

class CustomUserCreationFrom(UserCreationForm):#상속1

    class Meta:
        model = get_user_model()
        fields= ('username',)

class CustomUserChangeFrom(UserChangeForm):#상속2

    class Meta:
        model = get_user_model()
        fields =('first_name', 'last_name','email',)