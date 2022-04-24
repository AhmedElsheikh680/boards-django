from django.urls import path,include
from .views import home,board_topics,new_topic

urlpatterns = [
    path('', home, name="home"),
    path('<int:board_id>', board_topics, name="board_topics"),
    path('<int:board_id>/new', new_topic, name="new_topic"),
    # path('', include('accounts.urls')),
    # path('signup/', include('accounts.urls')),
]