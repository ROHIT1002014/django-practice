from django.contrib import admin
from .models import Account

# to show fileds on admin
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
  list_display = ['email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_superuser', 'is_staff']
  search_fields = ['email', 'username']
  readonly_fields = ('date_joined', 'last_login')

  filter_horizontal = ()
  list_filter = ()
  fieldsets = ()

admin.site.register(Account, AccountAdmin)