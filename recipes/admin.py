from django.contrib import admin

from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
