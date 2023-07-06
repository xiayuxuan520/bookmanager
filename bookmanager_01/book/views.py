from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


class BookListView(View):
    """
    图书列表
    """
    def get(self, request):

        return JsonResponse({'msg': 'ok'})
