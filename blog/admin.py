from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

@admin.register(Post) #데코레이터로 써도 대더라, 어드민에 모델 연결
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title', 'content_size','status','created_at', 'updated_at']
    actions=['make_published', 'make_draft']

    def content_size(self, post): #로우 값 추가는 함수로 구현
        return mark_safe('<strong>{}</strong>글자' .format(len(post.content)))
    content_size.short_description = '글자수' #디스플레이에 추가해주기

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request,'{}건의 포스팅을 draft 상태로 변경'.format(updated_count))
    make_draft.short_description = "지정 포스팅을 draft상태로 변경합니다"

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 published 상태로 변경'.format(updated_count))
    make_published.short_description = "지정 포스팅을 published상태로 변경합니다"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass