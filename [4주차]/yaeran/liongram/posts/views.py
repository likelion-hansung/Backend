from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Post
import accounts
from .forms import PostBaseForm, PostCreateForm, PostDetailForm

def index(request):
    post_list = Post.objects.all() #.order_by('-created_at')
    context = {
        'post_list': post_list
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    # post_list = Post.objects.all()
    post_list = Post.objects.filter(writer = request.user)
    context = {
        'post_list': post_list
    }
    return render(request, 'posts/post_list.html', context)
    
def post_detail_view(request, id):
    # if request.method == 'GET':
    if request.user.is_authenticated:
        try:
            post = Post.objects.get(id=id)
        except Post.DoseNotExist:
            return redirect('index')
        context = {
            'post' : post
        }
        return render(request, 'posts/post_detail.html', context)
    else:
        return redirect('/accounts/login')
    # if request.method == 'GET':
    #     # post = Post.objects.get(id=id)
    #     if not request.user.is_authenticated:
    #         return redirect('/accounts/login/')
    #     else:
    #         post = Post.objects.get(id=id)
    #         context = {
    #             'post': post
    #             # 'form': PostDetailForm(),
    #         }
    #         return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html', {'form': PostBaseForm()})
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create(
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('index')

def post_create_form_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostBaseForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                image = form.cleaned_data['image'],
                content = form.cleaned_data['content'],
                writer = request.user
            )
        else:
            return redirect('posts:post-create')
        return redirect('index')

def post_update_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'post': post
        }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        # Post.objects.create(
        if new_image:
            post.image.delete()
            post.image = new_image
        post.content = content
        # writer = request.user
        post.save()
        # )
        return redirect('post_detail', post.id)

def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context = {
            # 'post': post
            'accounts':accounts
        }
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index')

# Create your views here.
def url_view(request):
    print('url_view()')
    data = {'code': '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_view</h1>')

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    # ordering = ['-id']
    template_name = 'cbv_view.html'

def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list': object_list})
