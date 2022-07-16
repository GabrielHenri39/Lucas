from django.contrib import admin
from .models import User
from django.contrib.auth import admin as admin_auth_d
from .forms import UserChangeForm,UserCreationForm

# Register your models here.

@admin.register(User)
class UserAdmin(admin_auth_d.UserAdmin):
    form = UserChangeForm
    add_form: UserCreationForm
    model = User
