from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from faker import Faker
import codecs



# Create your views here.

#어떤 데이터가 어떻게 처리될지를 함수로 정의하기

def home(request):
    #모델로부터 객체 목록을 전달받을 수 있게 됐음. -> 이 기능을 .objects. 이 목록을 쿼리셋 이라구 함!
    # 이 쿼리셋을 구동시키는 것이 메소드래 (?)
    # 쿼리셋을 활용하게 해주는 것이 메소드 (날것으로의 데이터는 사용할 일이 없잖아!)
    # 표기 방식 : 모델.쿼리셋  = objects.method

    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request,'home.html',{'blogs':blogs,'posts':posts})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)

    return render(request,'detail.html',{'blog':blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body= request.GET['body']
    blog.mydate=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))


def new(request):
    return render(request,'new.html')

def fakeblog(request):
    fakeblog=Faker()
    blog=Blog()
    a=fakeblog.name()+'가 말하기를'
    b=fakeblog.text()+' 라네요'
    blog.title = a
    blog.body = b
    blog.mydate=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))