from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.utils.safestring import mark_safe
from .models import Profil, Comment, Test


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'profil', 'name', 'image')
    list_display_links = ('id', 'profil', 'name')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} weight="80" height="70"')


admin.site.register(User, UserAdmin)
admin.site.register(Comment)
admin.site.register(Test)
