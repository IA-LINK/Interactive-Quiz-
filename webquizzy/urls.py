from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from quiz import views  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Root URL
    path('', views.index, name='home'),
    
    # App-specific URLs
    path('base/', include('base.urls')),  # Adjust if 'base.urls' handles the root path
    path('quiz/', include('quiz.urls')),

    # Specific views
    path('profile/index.html', views.index, name='index'),
    path('quiz.html', views.quiz, name='quiz'),
    path('quizz.html', views.quizz_view, name='quiz'),
    path('login.html', views.login_view, name='login'),
    path('signup.html', views.signup_view, name='signup'),
    path('leaderboard.html', views.leaderboard_view, name='leaderboard'),
    #path('profile/leaderboard.html', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    
    path('quiz_result.html', views.quiz_result, name='quiz_result'),
]

# Static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
