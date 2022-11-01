from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import AnswerForm, CommentForm, PostForm


# Create your views here.
def post_list(request):
    """
    게시글 전체 목록
    """
    page = request.GET.get("page", 1)
    posts = Post.objects.order_by("-created_at")
    paginator = Paginator(posts, 10)
    post_list = paginator.get_page(page)
    return render(request, "board/post_list.html", {
        "post_list": post_list,
        "page": page
    })


@login_required(login_url="login")
def post_create(request):
    """
    Post 등록
    """
    if request.method == "POST":
        # form 에 내용 담기, 이미지는 request.FILES로 처리
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            # 유저 정보 가져와서 저장하기 위해 임시저장
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # 태그 저장
            form.save_m2m()
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "board/post_create.html", {"form": form})


def post_detail(request, pk):
    """
    pk에 해당하는 블로그 글 가져오기
    """
    post = get_object_or_404(Post, pk=pk)

    return render(request, "board/post_detail.html", {"post": post})
