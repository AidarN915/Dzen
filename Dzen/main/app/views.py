import telegram
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .forms import PostForm, CommentForm, RegForm
from .models import User, Post, Comment, Mark
from .serializer import UserSerializer, PostSerializer, CommentSerializer, MarkSerializer


# Create your views here.

class UserDetail(APIView):

    def get(self, request):
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @api_view(('GET', 'POST',))
    def reg(request):
        if request.method == "POST":
            us = request.POST.get('username')
            try:
                obj = User.objects.get(username=us)
            except User.DoesNotExist:

                form = RegForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/api/account')

            msg = {"msg": "already exist"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        form = RegForm()
        data = {
            'form': form
        }
        return render(request, 'auth/reg.html', data)


class PostDetail(APIView):
    def get(self, request):
        obj = Post.objects.all()
        serializer = PostSerializer(obj, many=True)
        return Response(list(serializer.data) , status=status.HTTP_200_OK)

    @api_view(('GET',))
    def get_id(request, post_id):
        try:
            obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(obj)
        ob = Mark.objects.filter(post = post_id)
        sum = 0
        for i in ob:
            sum += i.mark
        average = sum/len(list(ob))
        data = {
            "text":serializer.data.get('text'),
            "date":serializer.data.get('date'),
            "author":serializer.data.get('author'),
            "average":average
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def create_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('post/')
        form = PostForm()
        data = {
            'form': form
        }
        return render(request, 'post/create.html', data)


class CommentDetail(APIView):
    def get(self, request, post_id):
        try:
            obj = Comment.objects.filter(post=post_id)
        except Comment.DoesNotExist:
            msg = {"msg:": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        try:
            obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            msg = {"msg:": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def comment_add(request, post_id):
        try:
            obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            msg = {"msg:": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(f'/api/post/{post_id}/comment')
        form = CommentForm()
        data = {
            'form': form,
        }
        return render(request, 'comment/comment_add.html', data)


class MarkDetail(APIView):

    def get(self, request, post_id):
        obj = Mark.objects.filter(post = post_id)
        serializer = MarkSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, post_id):
        try:
            obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            msg = {"msg:": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = MarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def patch(self):
