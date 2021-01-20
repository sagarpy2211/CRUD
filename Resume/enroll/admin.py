from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','city','birth_date','experience','programming_lang','current_ctc','expect_ctc','password')