from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# Create your models here.
class Course(models.Model):
    """
    普通课程
    """
    name = models.CharField(max_length=32, help_text='课程的名称')
    # 仅仅用于反向查找（无须修改表结构）
    price_policy_list = GenericRelation('PricePolicy')


class VipCourse(models.Model):
    """
    VIP普通课程
    """
    name = models.CharField(max_length=32, help_text='Vip课程的名称')
    # 仅仅用于反向查找（无须修改表结构）
    price_policy_list = GenericRelation('PricePolicy')


class PricePolicy(models.Model):
    """
    价格策略
    """
    price = models.FloatField(help_text='价格')
    period = models.IntegerField(help_text='时间周期')
    # table_name = models.CharField(verbose_name='关联的表名称')
    # course_id = models.IntegerField(verbose_name='关联的表中的数据行的ID，即课程ID')
    content_type = models.ForeignKey(ContentType, verbose_name='关联的表名称', on_delete=models.CASCADE)
    """
    课程的ID，要使用object_id，不要使用course_id，这是个坑
    """
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID，即课程ID')
    # 仅仅用于快速操作content_type（无须修改表结构）
    content_object = GenericForeignKey('content_type', 'object_id')
