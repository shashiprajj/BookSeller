from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    PdfsCreateView, PdfsListView, PdfDetailView, PdfUpdateView,  PdfDeleteView
                    )
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("base/", views.base, name="base"),
    path("latest_updates/", views.latest_updates, name="latest_updates"),
    path('', PostListView.as_view(), name='index'),
    path('view_pdfs/', PdfsListView.as_view(), name='view_pdfs'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('pdf/<int:pk>/', PdfDetailView.as_view(), name='pdf-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/pdfs/', PdfsCreateView.as_view(), name='post-pdfs'),
    path('post/<int:pk>/update/',
         PostUpdateView.as_view(), name='post-update'),
    path('pdf/<int:pk>/update/',
         PdfUpdateView.as_view(), name='pdf-update'),
    path('post/<int:pk>/delete/',
         PostDeleteView.as_view(), name='post-delete'),
    path('pdf/<int:pk>/delete/',
         PdfDeleteView.as_view(), name='pdf-delete'),
    path('user/<str:username>',
         UserPostListView.as_view(), name='user-posts'),

    path("registration_base/", views.registration_base,
         name="registration_base"),
    path("branches/FE_IT/", views.FE_IT, name="FE_IT"),
    path("branches/SE_IT/", views.SE_IT, name="SE_IT"),
    path("branches/TE_IT/", views.TE_IT, name="TE_IT"),
    path("branches/BE_IT/", views.BE_IT, name="BE_IT"),
    path("branches/FE_CS/", views.FE_CS, name="FE_CS"),
    path("branches/SE_CS/", views.SE_CS, name="SE_CS"),
    path("branches/TE_CS/", views.TE_CS, name="TE_CS"),
    path("branches/BE_CS/", views.BE_CS, name="BE_CS"),
    path("branches/FE_EXTC/", views.FE_EXTC, name="FE_EXTC"),
    path("branches/SE_EXTC/", views.SE_EXTC, name="SE_EXTC"),
    path("branches/TE_EXTC/", views.TE_EXTC, name="TE_EXTC"),
    path("branches/BE_EXTC/", views.BE_EXTC, name="BE_EXTC"),

    path("branches/IT/", views.IT, name="IT"),
    path("branches/COMPS/", views.COMPS, name="COMPS"),
    path("branches/EXTC/", views.EXTC, name="EXTC"),
]
