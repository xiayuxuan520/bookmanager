from rest_framework import serializers

from book.models import BookInfo

"""
序列化器类
①将对象转换为字典
序列化器类的定义
①参考模型来定义就可以了




子段名=serializer.类型(选项)
字段名和模型字段名一致.
"""


class PeopleIRelatedSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    id = serializers.IntegerField(label='ID')
    name = serializers.CharField(label='名字')
    password = serializers.CharField(label='密码')


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', required=False)
    name = serializers.CharField(label='名称')
    pub_date = serializers.DateField(label='发布日期')
    readcount = serializers.IntegerField(label='阅读量')
    commentcount = serializers.IntegerField(label='评论量')
    people = PeopleIRelatedSerializer(many=True, required=False)

    def validate_readcount(self, value):
        if value < 0:
            raise serializers.ValidationError('阅读数量不能为负数')
        return value

    def validate(self, attrs):
        readcount = attrs.get('readcount')
        commentcount = attrs.get('commentcount')
        if commentcount > readcount:
            raise serializers.ValidationError('评论量不能大于阅读量')
        return attrs

    def create(self, validated_data):
        # validated data验证没有问题的数据
        # 如果我们的data经过我们的层层验证,没有问题,则
        # validated data = data
        return BookInfo.objects.create(**validated_data)




class PeopleInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    id = serializers.IntegerField(label='ID')
    name = serializers.CharField(label='名字')
    password = serializers.CharField(label='密码')
    description = serializers.CharField(label='描述信息')
    ###对外键进行学习
    # ①如果我们定又的序列化器外键字段类型为IntegerField
    # 那么,我们定又的序列化器字段名必须和数据库中的外键字段名一致
    #//book_id = serializers.IntegerField(label='书籍id')
    # ②如果我们期望的外键数据的key就是模型字段的名字,
    # 那么PrimaryKeyRelatedField 就可以获取到关联的模型id值
    # queryset在验证数据的时候,我们要告诉系统,
    # 在哪里匹配外键数据
    #book = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())
    # read only=True意思就是我不验证数据了
    # book = serializers.PrimaryKeyRelatedField(read_only=True)
    # ③如果我们期望获取外键关联的字符串的信息，这个时候我们可以使用StringRelationField
    # （即__str__方法的返回值）
    #book = serializers.StringRelatedField(label='图书')
    # ④如果我们期望获取，book所关联的模型的所有数据,这个时候我们就定又book=BookInfoSerializer()
    # book=关联的BookInfo的一个关联对象数据
    # book=BookInfo. objects. get(id=xxx)
    # book=BookInfoSerializer(instance=book).data
    # 等号右边的book是模型对象
    # 等号左边的book是字典数据
    book = BookInfoSerializer()


"""
通过字段的选项来验证数据
例如:
CharField (max_ Length=10,min_ Length=5)
IntegerField(max_ value=10,min_ vaLue=1)
required=True默认是True
read only:只用于序列化使用。反序列化的时候忽略该字段
write_ only:只是用于反序列化使用。序列化的时候忽略该字段



3.如果我们的数据,满足类型要求,又满足选项要求。我们如果需要对数据
进行进一步验证的时候，可以实现以下方法:
以validate_开头 接字段名字的方法
value就是字段对应的值
例如:
def validate_ readcount(self , value):
return value



如果我们的序列化器是维承自Serialzier
当调用序列化器的save方法的时候，会触发调用序列化器的create方法

"""

