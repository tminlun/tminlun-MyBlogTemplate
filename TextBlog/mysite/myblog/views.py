from django.shortcuts import render,render_to_response,get_object_or_404
from .models import BlogType,Blog,Blog_with_news

def get_public_common_date(request):
    pass

def fengmian(request):

    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog/fengmian.html', context)



def index(request):
    context = {}
    return render_to_response('blog/index.html', context)

def info(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    context = {}
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog_types'] = BlogType.objects.all()
    #阅读数量
    if not request.COOKIES.get('blog_%s_reader'%blog.pk):
        blog.reader_num += 1
        blog.save()
    response =  render_to_response('blog/info.html', context)
    response.set_cookie('blog_%s_reader'%blog.pk, 'true')
    return response

def time(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog/time.html', context)

def picture(request):
    context = {}
    return render_to_response('blog/share.html', context)

