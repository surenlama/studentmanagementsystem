from django.urls import path
from .views import signup,register,signin,login,student,logout,delete,addstu,home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
 path('signup/', signup,name="signup"),
 path('register/', register,name="register"),
 path('signin/', signin,name="signin"),
 path('login/', login,name="login"),
 path('student/', student,name="student"),
 path('logout/', logout,name="logout"),
 path('addstu/', addstu,name="addstu"),
 path('home/', home,name="home"),
 path('delete/<int:todo_id>/', delete,name="delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)