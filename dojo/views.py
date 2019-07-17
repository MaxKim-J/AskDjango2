#dojo/views.py/

import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name,age))


def post_list1(request):
    name = "으아앙"
    return HttpResponse('''
    <h1>쟝고를 공부하는 종혁</h1>
    <h3>{name}</h3>
    <p>장고는 넘어려운것이에요</p>
    '''.format(name=name))


def post_list2(request):
    name = '으앜앜앜앜'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    #json형식 응답
    return JsonResponse({
        'message': '안녕 파이썬과 장고쨩',
        'items': ['파이썬', '장고', '자스', '아주르'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    #'FBV: 엑셀 다운로드 응답'
    filepath = '‪C:\dev\my-first-django\empty.xlsx'
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'. format(filename)
        return response

