#blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    #길이 제한 있는 문자열, 성능 좋아짐
    content = models.TextField(verbose_name='내용')
    #길이 제한 없는 문자열
    created_at=models.DateTimeField(auto_now_add=True)
    #날짜와 시간을 저장하는 필드 - 옵션: 최초 저장될때 일시 자동저장
    updated_at=models.DateTimeField(auto_now=True)
    #옵션: 레코드 갱신이 될때마다 자동저장


