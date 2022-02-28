from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import RegistrationForm, PostForm, CommentForm
from .models import Post, Comment


def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts/home.html', {'posts': posts})

def about(request):
    return render(request, 'posts/about.html', {'title':'About'})

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created you can now login')
            return redirect('login')
    return render(request, 'posts/register.html', {'form': form, 'title': 'Register'})

def post(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment_text = form.cleaned_data.get('comment')
                comment = Comment(user_id=request.user, post_id=post, comment=comment_text)
                comment.save()
                post.comments.add(comment)
                return redirect('post', id)
        else:
            messages.info(request, 'You need to login to comment on this post')
    return render(request, 'posts/post.html', {'post': post, 'form': form})

@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            code = form.cleaned_data.get('code')
            programming_language = form.cleaned_data.get('programming_language')
            post = Post(title=title, code=code, programming_language=programming_language, programmer=request.user)
            post.save()
            messages.success(request, 'Post created')
            return redirect('home')
    return render(request, 'posts/create_post.html', {'form': form})

@login_required(login_url='login')
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.programmer:
        raise PermissionDenied
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated')
            return redirect('home')
    return render(request, 'posts/update_post.html', {'form': form})

@login_required(login_url='login')
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.programmer:
        raise PermissionDenied
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('home')
    return render(request, 'posts/delete_post.html', {'post': post})

# @login_required(login_url='login')
# def account(request):
#     posts = request.user.post_save.all()
#     return render(request, '')
