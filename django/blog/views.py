from django.http import HttpResponse


# Create your views here.

def post_list(request):
    return HttpResponse('<html><body><h1>Post list</h1><p>목록을 보여줄 예정입니다</p></body></html>')
