from django.contrib import admin
from .models import Post

@admin.register(Post) #데코레이터로 써도 대더라
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at','updated_at']

# Register your models here.
