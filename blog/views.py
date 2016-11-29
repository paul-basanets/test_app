# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from blog.forms import PostModelForm
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "index.html", context)


@login_required
def read_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "read_post.html", locals())


def create_post(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return redirect(reverse("blog_index"))
    return render(request, "create_post.html", locals())
