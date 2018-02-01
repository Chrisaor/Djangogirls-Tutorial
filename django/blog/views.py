from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def post_list(request):


    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    context = {
        'post' : Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)

def post_add(request):
    # localhost:8000/add로 접근시
    # 이 뷰가 실행되어서 Post add page라는 문구를 보여주도록 urls 작성
    # HttpResponse가 아니라 blog/post_add.html을 출력
    # post_add.html은 base.html을 확장, title(h2)부분에  'Post add'라고 출력
    return render(request, 'blog/post_add.html')