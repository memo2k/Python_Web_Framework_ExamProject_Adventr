from django.contrib import admin

from posts.models import Post, Like


class LikeInline(admin.TabularInline):
    model = Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'description')
    list_filter = ('location',)
    inlines = [
        LikeInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
