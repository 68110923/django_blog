# Create your views here.

from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse,redirect,HttpResponseRedirect
import functools


from blogapp.models import *

def check_user(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        #判断是否登录
        userid = args[0].session.get("login_user", "")
        if userid == "":
            #保存当前的url到session中
            # args[0].session["path"] = args[0].path
            #重定向到登录页面
            return redirect(reverse("userget"),kwargs={'msg':'您还未登录，请登录'})
        return func(*args, **kwargs)
    return inner

def homepage(request):
    commentall = Comment.objects.all().prefetch_related('userId', 'articleId').reverse()
    articleall=Article.objects.all().select_related('User_id').reverse()
    return render(request, 'homepage.html',{'articleall':articleall,'commentall':commentall})

def user(request):
    commentall = Comment.objects.all().prefetch_related('userId', 'articleId').reverse()
    articleall = Article.objects.all().select_related('User_id').reverse()
    if request.method == 'POST':
        sex=request.POST['sex']
        userid=request.POST['userid']
        username=request.POST['username']
        pwd=request.POST['pwd']
        if sex and username and userid and pwd:
            if len(User.objects.filter(userid=userid)) > 0:
                return render(request, 'user/post_user.html',{'msg':'该用户已存在，请重新注册'})
            else:
                User.objects.create(sex=sex,userid=userid,username=username,pwd=pwd)
                return render(request,'user/get_user.html',{'msg':'注册成功,请登录'})
        else:
            return render(request, 'user/post_user.html', {'msg': '该用户已存在，请重新注册'})
    elif request.method == 'GET':
        userid = request.GET.get('userid','')
        pwd = request.GET.get('pwd','')
        temp=User.objects.filter(userid=userid).values()[0]
        if len(temp) > 0:
            if temp['pwd']==pwd:
                request.session["login_user"] = userid
                return render(request, 'homepage.html',{'msg': '登陆成功','articleall':articleall,'commentall':commentall})
            else:
                return render(request, 'homepage.html', {'msg': '账号或密码错误','articleall':articleall,'commentall':commentall})
        else:
            return render(request, 'homepage.html', {'msg': '账号不存在','articleall':articleall,'commentall':commentall})
    elif request.method == 'PUT':
        return render(request,'user/put_user.html')


def userpost(request):
    return render(request, 'user/post_user.html')
def userget(request):
    return render(request, 'user/get_user.html')
@check_user
def userput(request):
    temp=User.objects.filter(userid=request.session["login_user"]).values()[0]
    return render(request, 'user/put_user.html',{'user':temp})
@check_user
def articlepost(request):
    return render(request, 'article/article_post.html', {'msg': '请填写发布内容'})

@check_user
def article(request):
    commentall = Comment.objects.all().prefetch_related('userId', 'articleId')
    articleall = Article.objects.all().select_related('User_id').reverse()
    if request.method == 'POST':
        articleTitle = request.POST['article_title']
        articleContent = request.POST['article_content']
        if articleTitle != '':
            Article.objects.create(articleTitle=articleTitle,articleContent=articleContent,User_id=User.objects.get(userid=request.session["login_user"]))
            return render(request, 'homepage.html',{'msg':f'文章《{articleTitle}》发布成功','articleall':articleall,'commentall':commentall})
        else:
            return render(request, 'article/article_post.html',{'msg':'标题不能为空'})

@check_user
def article_comment(request):
    import re
    articleall = Article.objects.all().select_related('User_id').reverse()
    commentId=int(re.findall('articleID%3D(\d*)',str(request.get_raw_uri()))[0])
    commentall = Comment.objects.all().prefetch_related('userId','articleId')
    print(commentall.values())
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment == '':
            return render(request, 'homepage.html', {'msg': '评论内容不得为空','articleall':articleall,'commentall':commentall})
        else:
            Comment.objects.create(userId=User.objects.get(userid=request.session["login_user"]),commentContent=comment,articleId=Article.objects.get(id=commentId))
            return render(request, 'homepage.html', {'msg': '评论成功','articleall':articleall,'commentall':commentall})