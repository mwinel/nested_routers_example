from rest_framework_nested import routers
from django.urls import path, include
from .views import BookViewSet, ChapterViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

# Nested router for chapters
book_router = routers.NestedDefaultRouter(router, r'books', lookup='book')
book_router.register(r'chapters', ChapterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
]
