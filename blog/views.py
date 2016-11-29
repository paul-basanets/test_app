# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.urls import reverse

from blog.forms import PostForm, PostModelForm
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "index.html", context)


def read_post(request, post_id):
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     pass
    post = get_object_or_404(Post, id=post_id)
    return render(request, "read_post.html", locals())


# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print form.cleaned_data
#         post = Post(title=request.POST.get('title'), content=request.POST.get('content'))
#         post.save()
#         post.delete()
#         queryset = Post.objects.all()
#         queryset = queryset.filter()

#         return redirect(reverse("blog_index"))
#     # post = Post.objects.create(title=request.POST.get('title'), content=request.POST.get('content'))
#     # post, created = Post.objects.get_or_create(title=request.POST.get('title'), content=request.POST.get('content'))
#     form = PostModelForm()
#     return render(request, "create_post.html", locals())


def create_post(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return redirect(reverse("blog_index"))
    # return render(request, "create_post.html", locals())
    return HttpResponse(render_to_string("create_post.html", locals(), RequestContext(request)))
