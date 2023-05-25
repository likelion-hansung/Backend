from django.shortcuts import get_object_or_404, redirect, render

from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic.list import ListView
from .models import Post
from django.contrib.auth.decorators import login_required

# 세션
from .forms import PostBaseForm, PostCreateForm, PostDetailForm
from .models import Post

# 인덱스
def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list' : post_list,
    }
    return render(request, 'index.html', context)


# 전체 목록 보기
def post_list_view(request):
    # post_list = Post.objects.all() # Post의 전체 데이터 조회
    post_list = Post.objects.filter(writer=request.user) # Post.writer 가 현재 로그인인 것 조회
    # post_list = None
    context = {
        'post_list' : post_list,
    }
    return render(request, 'posts/post_list.html', context)


# 상세 목록 보기
def post_detail_view(request, id):
    
    try:
        post = Post.objects.get(id=id)
        #로그인 된 상태가 아니라면
        if not request.user.is_authenticated:
            # 로그인 페이지로 리다이렉트
            return redirect('/accounts/login')
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post' : post,
        'form' : PostDetailForm(),
    }
    
    return render(request, 'posts/post_detail.html', context)


# 생성
@login_required
def post_create_view(request):
    if request.method=='GET':
        return render(request, 'posts/post_form.html')
    else :
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user
        )
        return redirect('index') 


# 수정
@login_required
def post_udpate_view(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id, writer=request.user)
    if request.method == 'GET':
        context = { 'post' : post }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)
        if new_image:
            post.image.delete()
            post.image = new_image
            
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)

# 삭제
@login_required
def post_delete_view(request, id):
    
    post = get_object_or_404(Post, id=id)
    # post = get_object_or_404(Post, id=id, writer=request.user)
    
    if request.user != post.writer:
        raise Http404('잘못된 접근입니다.')
    
    if request.method == 'GET':
        context = { 'post' : post }
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index')
    


def url_view(request):
    print('url_view')
    
    data = { 'code' : '001', 'msg' : 'OK'}
    # return JsonResponse(data)
    return HttpResponse('url_view')

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username : {username}')
    print(f'request.GET : {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method : {request.method}')
    if request.method == 'GET':
        print(f'request.GET : {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST : {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'
    
# 세션 
def post_create_form_view(request):
    if request.method =='GET':
        form = PostCreateForm()
        context = { 'form' : form }
        return render(request, 'posts/post_form2.html', context)
    else :
        form = PostCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user,
            )
        else:
            return redirect('posts:post-create')
        
        return redirect('index')