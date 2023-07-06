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

