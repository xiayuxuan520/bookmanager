import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from book.models import BookInfo


# Create your views here.


class BookListView(View):
    """
    图书列表
    查询所有图书、增加图书
    """
    def get(self, request):
        booklist = BookInfo.objects.all()
        book_list = []
        for book in booklist:
            book_list.append({
                'id': book.id,
                'name': book.name,
                'pub_date': book.pub_date,
            })
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """
           新增图书
           路由：POST /books/
           接受参数
           验证参数
           数据入库
           返回响应
        """
        data = json.loads(request.body.decode())
        book = BookInfo.objects.create(
            name=data.get('name'),
            pub_date=data.get('pub_date')
        )
        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date
        }, safe=False, status=201)


class BookDetailView(View):
    """
        获取单个图书信息
        修改图书信息
        删除图书
    """
    def get(self, request, id):
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            return JsonResponse({}, status=404)

        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date
        })

    def put(self, request, id):
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            return JsonResponse({},status=404)
        data = json.loads(request.body.decode())
        book.name = data.get('name')
        book.pub_date = data.get('pub_date')
        book.save()
        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date
        })

    def delete(self, request, id):
        try:
            book = BookInfo.objects.get(id=id)
        except Exception as e:
            return JsonResponse({}, status=404)
        book.is_delete = True
        book.save()
        return JsonResponse({}, status=204)
