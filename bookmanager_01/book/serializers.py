from rest_framework import serializers
"""
序列化器类
①将对象转换为字典
序列化器类的定义
①参考模型来定义就可以了




子段名=serializer.类型(选项)
字段名和模型字段名一致.
"""


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID')
    name = serializers.CharField(label='名称')
    pub_date = serializers.DateField(label='发布日期')
    readcount = serializers.IntegerField(label='阅读量')
    commentcount = serializers.IntegerField(label='评论量')


class PeopleInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    id = serializers.IntegerField(label='ID')
    name = serializers.CharField(label='名字')
    password = serializers.CharField(label='密码')
    description = serializers.CharField(label='描述信息')
    ###对外键进行学习
    # ①如果我们定又的序列化器外键字段类型为IntegerField
    # 那么,我们定又的序列化器字段名必须和数据库中的外键字段名一致
    book_id = serializers.IntegerField(label='书籍id')

