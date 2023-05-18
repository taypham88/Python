from blogging.models import Post
from django.shortcuts import render
from blogging.forms import PostForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {"form": form}
    return render(request, "blogging/create.html", context)


class BlogListView(ListView):

    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):

    published = Post.objects.exclude(published_date__exact=None)
    queryset = published.order_by("-published_date")
    template_name = "blogging/detail.html"
