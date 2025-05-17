from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
    email = form.EmailField(required=True)
    class Meta:
        model = User
        fields = '__all__'