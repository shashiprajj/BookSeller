from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts, Pdfs

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.


class PostListView(ListView):
    model = Posts
    template_name = 'index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Posts
    template_name = 'user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(username=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Posts


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['branch', 'year', 'sem', 'book_name', "Author_of_book",
              'op_price', 'sp_price', 'email', 'contact', 'book_img']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['branch', 'year', 'sem', 'book_name', "Author_of_book",
              'op_price', 'sp_price', 'email', 'contact', 'book_img']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False


# PDFS CLASSES

class PdfsCreateView(LoginRequiredMixin, CreateView):
    model = Pdfs
    fields = ['branch', 'year', 'sem', 'EBook_name',
              'Upload_EBook']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class PdfsListView(ListView):
    model = Pdfs
    template_name = 'index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pdfs'
    ordering = ['-date_posted']
    paginate_by = 4


class PdfDetailView(DetailView):
    model = Pdfs


class PdfUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pdfs
    fields = ['branch', 'year', 'sem', 'EBook_name',
              'Upload_EBook']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False


class PdfDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pdfs
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username:
            return True
        else:
            return False


def index(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, "index.html", context)


def base(request):
    return render(request, "base.html")


def about(request):
    return render(request, "about.html")


def latest_updates(request):
    return render(request, "latest_updates.html")


def registration_base(request):
    return render(request, "registration_base.html")


# IT DEPARTMENT

def FE_IT(request):
    context = {
        'FE_IT': Posts.objects.filter(branch="IT", year="FE")
    }
    return render(request, 'branches/FE_IT.html', context)


def SE_IT(request):
    context = {
        'SE_IT': Posts.objects.filter(branch="IT", year="SE")
    }
    return render(request, 'branches/SE_IT.html', context)


def TE_IT(request):
    context = {
        'TE_IT': Posts.objects.filter(branch="IT", year="TE")
    }
    return render(request, 'branches/TE_IT.html', context)


def BE_IT(request):
    context = {
        'BE_IT': Posts.objects.filter(branch="IT", year="BE")
    }
    return render(request, 'branches/BE_IT.html', context)


# COMPS DEPARTMENT

def FE_CS(request):
    context = {
        'FE_CS': Posts.objects.filter(branch="CS", year="FE")
    }
    return render(request, 'branches/FE_CS.html', context)


def SE_CS(request):
    context = {
        'SE_CS': Posts.objects.filter(branch="CS", year="SE")
    }
    return render(request, 'branches/SE_CS.html', context)


def TE_CS(request):
    context = {
        'TE_CS': Posts.objects.filter(branch="CS", year="TE")
    }
    return render(request, 'branches/TE_CS.html', context)


def BE_CS(request):
    context = {
        'BE_CS': Posts.objects.filter(branch="CS", year="BE")
    }
    return render(request, 'branches/BE_CS.html', context)


# EXTC DEPARTMENT

def FE_EXTC(request):
    context = {
        'FE_EXTC': Posts.objects.filter(branch="EXTC", year="FE")
    }
    return render(request, 'branches/FE_EXTC.html', context)


def SE_EXTC(request):
    context = {
        'SE_EXTC': Posts.objects.filter(branch="EXTC", year="SE")
    }
    return render(request, 'branches/SE_EXTC.html', context)


def TE_EXTC(request):
    context = {
        'TE_EXTC': Posts.objects.filter(branch="EXTC", year="TE")
    }
    return render(request, 'branches/TE_EXTC.html', context)


def BE_EXTC(request):
    context = {
        'BE_EXTC': Posts.objects.filter(branch="EXTC", year="BE")
    }
    return render(request, 'branches/BE_EXTC.html', context)


#  E-BOOKS
def IT(request):
    context = {
        'IT': Pdfs.objects.filter(branch="IT")
    }
    return render(request, 'branches/IT.html', context)


def COMPS(request):
    context = {
        'COMPS': Pdfs.objects.filter(branch="CS")
    }
    return render(request, 'branches/COMPS.html', context)


def EXTC(request):
    context = {
        'EXTC': Pdfs.objects.filter(branch="EXTC")
    }
    return render(request, 'branches/EXTC.html', context)
