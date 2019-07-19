from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q: #쿼리가 있으면
        qs = qs.filter(title__icontains=q) #큐가 포함되어있는 쿼리셋만 가져온다
    return render(request, 'blog/post_list.html', {'post_list' : qs})

