from django.urls import path

from muhammadyor.views import HomePageView, UserRegisterView, UserLoginView, UserLogoutView , UserAboutView, \
    UserPostDetailView, UserPostConfirmDeleteView, UserPostsView, UserPostsFormView

app_name = 'muhammadyor'
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('about/', UserAboutView.as_view(), name='about-page'),
    path('post_detail/', UserPostDetailView.as_view(), name='post-detail'),
    path('post_confirm_delete/', UserPostConfirmDeleteView.as_view(), name='post-confirm-delete'),
    path('user_posts/', UserPostsView.as_view(), name='user-posts'),
    path('post_form/', UserPostsFormView.as_view(), name='post-form'),

]
