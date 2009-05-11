from django.contrib import admin
from django_yaba.blog.forms import *
from django_yaba.blog.models import *

class PhotoInline(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

class LinksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}
    #list_display = ('label', 'site_link', 'url')
    list_filter = ('label', 'site_link')
    search_fields = ('label', 'site_link')

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}
    form = ArticleAdminModelForm

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}
    form = ArticleAdminModelForm

admin.site.register(Story, StoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
admin.site.register(Links, LinksAdmin)
admin.site.register(Article, ArticleAdmin)