from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.


def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()  # 블로그 모든 글을 대상으로
    paginator = Paginator(blog_list, 3)  # 블로그 세 개를 한 페이지로 자르기
    # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담고)
    page = request.GET.get('page')  # 딕셔너리형, page(key)를 넘기면 value가 리턴
    # posts에는 request된 페이지를 저장된 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})


def new(request):
    return render(request, 'new.html')


def create(request):
    # 입력받은 내용을 DB에 넣어주는 함수
    blog = Blog()

    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect('/blog/'+str(blog.id))
    # blog.id는 int형이기 때문에 str로 형변환을 시켜준 것
    # 리턴이 없는 상태에서는 DB에 post가 저장되긴 함


# venv 생성하고 들어가서 장고 깔고 프로젝트 만들고 프로젝트 들어가서 앱 만들고
# settings에 앱 정의하고
# app에 templates 만들고 html 만들고 이 html을 뷰에 함수로 정의
# 그리고 urls.py에 blogapp.views 임폴트 해주고 경로 지정

# 데이터를 넣을 수 있게 모델에 클래스를 정의
# 메이크마이그레이션 -> 마이그레이트

# 어드민 계정 생성
# 어드민.py에 모델 등록
# 레지스터 등록

# views에 모델 임폴트 하고 쿼리셋 등록

# 글쓰기 추가

# 글쓰기를 누르면 {% %}를 타고 new.html의 form tag를 타고 views.py를
# 통해서 DB에 저장
# views.py에 다음 함수가 필요
# reqeust가 들어오면 new.html을 띄우는 함수
# new.html로 입력한 내용을 db에 등록하는 함수
