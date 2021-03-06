from django.contrib import admin
from users_manage_api.models import UserProfile
# Register your models here.


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """
    This was made in order to manage the users permissions
    easily. Is the user admin.
    """
    list_display = ('pk', 'email',)
    list_display_links = ('pk', 'email',)

    search_fields = (
        'email',
    )

    list_filter = (
        'is_active',
        'is_staff',
    )
