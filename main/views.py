from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Category, Tag, Post
from .permissions import IsAdminPermission, IsAuthorPermission
from .serializers import CategorySerializer, TagSerializer, PostSerializer


@api_view()
def categories_list(request):
    categories = Category.objects.all()
    print(categories)
    serializer = CategorySerializer(categories, many=True)
    categories = serializer.data
    print(categories)
    return Response(categories)

# class CategoriesListView(APIView):
#     def get(self, request, format=None):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         categories = serializer.data
#         return Response(categories)


class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostsListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class CreatePostView(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAdminPermission, ]
#
# class PostDetailsView(RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class UpdatePostView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthorPermission]
#
# class DeletePostView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthorPermission]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'slug'

# TODO: сделать валидацию данных при создании
# TODO: подключить картинки
# TODO: расставить permission.
# TODO: подключить роутер.
# TODO: сделать пагинацию, фильтраци, поиск.
# TODO: сделать документацию для frontend
# TODO: сделать авторизация
# TODO: сделать избранное(лайки)
# TODO: сделать комментарии


# POST - create
# GET - list, retrieve(details)
# api/v1/posts - create, list
# api/v1/posts/<id/slug> - details, update, delete

# PUT, PATCH - update
# DELETE - destroy


# 1. Модель клиент-сервер
# 2. Отсутствие состояния (на сервере не хранится информация о состоянии клиента) Token
# 3. Кэширование Redis, Memcached
# 4. Единообразие интерфейса
# 5. Слои