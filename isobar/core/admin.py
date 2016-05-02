from django.contrib import admin
from core.models import Article

class ArticleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticleAdmin)