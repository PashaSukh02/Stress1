from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home, name='test_home'),
    path('create', views.create_test, name='create_test'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='test-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='test-update'),
    path('<int:pk>/delete', views.NewsDeliteView.as_view(), name='test-delete'),
    path('tests', views.test_work, name='tests_work'),
    path('result1', views.index1, name='result1'),
    path('result2', views.index2, name='result2'),
    path('result3', views.index3, name='result3'),

]
