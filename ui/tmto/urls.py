from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.title, name='title'),
    url(r'^function1$', views.function1, name='function1'),
    url(r'^function2$', views.function2, name='function2'),
    url(r'^function3$', views.function3, name='function3'),
    url(r'^function1_oninput$', views.function1_oninput, name='function1_oninput'),
    url(r'^function2_oninput$', views.function2_oninput, name='function2_oninput'),
    url(r'^function3_oninput$', views.function3_oninput, name='function3_oninput'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)