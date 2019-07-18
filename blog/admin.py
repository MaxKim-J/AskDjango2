from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

@admin.register(Post) #데코레이터로 써도 대더라
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title', 'content_size','created_at','updated_at']

    def content_size(self, post): #로우 값 추가는 함수로 구현
        return mark_safe('<strong>{}</strong>글자' .format(len(post.content)))
    content_size.short_description = '글자수'