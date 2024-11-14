from django.urls import path

from KnowledgeBase import views

urlpatterns = [
    path('get/all/rules', views.getAllRules, name='get_all_rules'),
    path('save/request', views.save_request, name='save_request'),
    path('get/rules/by/namespace/<str:namespace>', views.getRuleByNamespace, name='get_rules_by_namespace'),    
]