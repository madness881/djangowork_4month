from django.shortcuts import render, HttpResponse, redirect
from posts.models import Comment, Post
from posts.forms import CommentForm, PostForm, PostUpdateForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home_view(request):
    return render(request, "home.html")

def first_view(request):
    return HttpResponse(f'hello world')

def html_view(request):
    return render(request,"base.html")

@login_required(login_url="login")
def post_list_view(request):
    limit = 3
    if request.method == "GET":
        posts = Post.objects.exclude(author=request.user)
        form = SearchForm()
        q = request.GET.get("q")
        category_id_value = request.GET.get("category_id")
        tag_ids = request.GET.get("tag_ids")
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        if q:
            posts = posts.filter(Q(title__icontains = q | Q(content__icontains = q)))
        if category_id_value:
            posts = posts.filter(category_id=category_id_value)
        if tag_ids:
            posts = posts.filter(tags__id__in=tag_ids).distinct()
        if ordering:
            posts = posts.order_by(ordering)
        if page:
            max_pages = len(posts) / limit
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1
            else:
                max_pages = round(max_pages)
            start = (page - 1 ) * limit
            end = page * limit 
            posts = posts[start:end]

        return render(request,"posts/post_list.html", context={"posts": posts, "form": form, "max_pages":range(1,  max_pages + 1)})

@login_required(login_url="login")
def post_detail_view(request, post_id):
    post = Post.objects.get(id = post_id)
    comments = Comment.objects.filter(post=post).order_by("-created")
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", post_id=post.id)
    return render(request, "posts/post_detail.html", context={"form": form, "post": post, "comments": comments})

@login_required(login_url="login")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        else:
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content") 
            image = form.cleaned_data.get("image")
            Post.objects.create(title=title,content=content,image=image)
        return redirect("/posts")
    
def post_update_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return HttpResponse("Post not found")
    if request.method == "GET":
        form = PostUpdateForm(instance=post)
        return render(request, "posts/post_update.html", context={"form": form})
    if request.method == "POST":
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "posts/post_update.html", context={"form": form})
        elif form.is_valid():
            form.save()
            return redirect(f"/profile/")
    
