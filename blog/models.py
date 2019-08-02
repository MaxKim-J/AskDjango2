#blog/models.py
import re
from django.db import models
from django.forms import ValidationError

from django.conf import settings
from django.urls import reverse


def lnglat_validator(value): #정규표현식에 맞는 조건만 유효성 검사
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('오류다 임마') #예외발생


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #author = models.CharField(max_length=60)
    title = models.CharField(max_length=100, verbose_name='제목')
    #길이 제한 있는 문자열, 성능 좋아짐
    content = models.TextField(verbose_name='내용')
    #길이 제한 없는 문자열
    created_at=models.DateTimeField(auto_now_add=True)
    #날짜와 시간을 저장하는 필드 - 옵션: 최초 저장될때 일시 자동저장
    updated_at=models.DateTimeField(auto_now=True)
    #옵션: 레코드 갱신이 될때마다 자동저장
    status = models.CharField(max_length=1, choices = STATUS_CHOICES) #목록
    tag_set = models.ManyToManyField('Tag', blank=True) #relation 지정할때는 문자열로 모델명을
    #해당 릴레이션 클래스가 하위에 있으면 네임에러, 문자열로 지정해주기
    #다른앱에 있다면 도트연산자
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')

    def __str__(self): #인스턴스의 이름으로 디비 객체 표현
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

    class Meta: #Post 내 기본정렬, 모든 정렬 칼럼에 모오두 반영
        ordering = ['-id'] #id는 오름차순 -id는 내림차순 ,로 1/2차 기준



class Comment(models.Model): #대응되는 모델 하나 더
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #2.0부터
    #post_id 가 db필드로 들어간다. #인스턴스 한줄에 대응하는 다른 속성
    author = models.CharField(max_length=60)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name