from django.contrib import admin
from .models import Post, Author, Category, Comment, PostCategory
from modeltranslation.admin import TranslationAdmin


class PostAdmin(TranslationAdmin):
    model = Post
    list_display = ["author", "change_news", "time_in", "head_news", "rate_news"]
    list_filter = ["author", "change_news", "time_in", "rate_news"]
    search_fields = ["author__authUser__username", "head_news", "rate_news"]

    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["authUser", "rateAuthor"]
    list_filter = ["rateAuthor"]
    search_fields = ["authUser__username", "rateAuthor"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "authUser", "text_comment", "time_in", "rate_comment"]
    list_filter = ["time_in", "rate_comment"]
    search_fields = ["authUser__username"]

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ["post", "category"]
    list_filter = ["category"]
    search_fields = ["category__category"]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
