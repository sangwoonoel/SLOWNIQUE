from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .forms import CustomLoginView

app_name = 'users'

mypage_patterns = [
    path("", views.mypage, name="mypage"),
    path("brands/", views.brand_like, name="my_brand"),
    path("scraps/", views.post_like, name="my_scrap"),
    path("comments/", views.comments_list, name="my_comment"),
    path("posts/", views.user_post, name="my_post"),
    path("brand_delete/<int:pk>", views.mypage_brand_delete, name="mypage_brand_delete"),
    path("scrap_delete/<int:pk>", views.mypage_scrap_delete, name="mypage_scrap_delete"),
    path("comment_delete/<int:pk>", views.mypage_comment_delete, name="mypage_comment_delete"),
    path("post_delete/<int:pk>", views.mypage_post_delete, name="mypage_post_delete"),
]

account_patterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns = [
    path('', views.main, name='main'),
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'), 
    path("signup/", views.signup, name="signup"),
    path('mypage/', include(mypage_patterns)),
    # path("mypage/home", views.mypage, name="mypage"),
    # path("mypage/brands/", views.brand_like, name="my_brand"),
    # path("mypage/scraps/", views.post_like, name="my_scrap"),
    # path("mypage/posts/", views.user_post, name="my_post"),
    # path("mypage/comments/", views.comments_list, name="my_comment"),
    # path("post_delete/", views.mypage_post_delete, name="mypage_post_delete"),
    # path("brand_delete/", views.mypage_brand_delete, name="mypage_brand_delete"),  
    # path("mypage_comment_delete/", views.mypage_comment_delete, name="mypage_comment_delete"),  
    path('account/', include(account_patterns)),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('change_password/', views.password, name='change_password'),
    path('forgot_id/', views.ForgotIDView, name="forgot_id"),
    # path("user_post_delete/", views.user_post_delete, name="user_post_delete")
    path('forbidden/', views.forbid_access, name='forbidden'),
]