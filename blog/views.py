from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.all() #검색 구현
    q = request.GET.get('q', '')
    if q: #쿼리가 있으면
        qs = qs.filter(title__icontains=q) #큐가 포함되어있는 쿼리셋만 가져온다
    return render(request, 'blog/post_list.html', {'post_list' : qs})

def post_detail(request, id):
    #post = Post.objects.get(id=id) 아래랑 같은말임 인스턴스
    #특정 모델의 인스턴스를 획득하는 방법을 그냥 밑에 함수로 통일하셈
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
