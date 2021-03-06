from django.shortcuts import render, HttpResponse

from app import models


# Create your views here.
def test(request):
    """
    # 添加之前向两个课程表中添加数据
    models.Course.objects.create(name='Python')
    models.Course.objects.create(name='Flask')
    models.Course.objects.create(name='Django')
    models.VipCourse.objects.create(name='DRF')
    models.VipCourse.objects.create(name='VUE')
    models.VipCourse.objects.create(name='Scrapy')
    """
    """
    # 添加一条普通课程为“Python”价格为99.9，学习周期为3个月的价格策略记录(首先还要查询相关字段的值)
    course_obj = models.Course.objects.filter(name='Python').first()
    print(course_obj)  # Course object (1)
    # 首先需要获取根据课程的名称获取课程的id
    course_id = course_obj.id
    # 然后还要获取content_type表中course表对应的id
    content_type_obj = models.ContentType.objects.filter(model='course').first()
    content_type_id = content_type_obj.id
    models.PricePolicy.objects.create(price=99.9, period=3, course_id=course_id, content_type_id=content_type_id)
    """
    """
    1. 借助content_type快速实现数据插入(content_type)操作
    1. 借助content_type快速实现数据插入(content_type)操作
    course_obj = models.Course.objects.filter(name='Python').first()
    models.PricePolicy.objects.create(price=99.9, period=3, content_object=course_obj)
    """
    """
    2. 根据课程ID获取该课程所有的价格策略(借助GenericRelation实现反向查找)
    """
    try:
        course_obj = models.Course.objects.filter(id=1).first()  # id=1是Python课程
        price_policy_list = course_obj.price_policy_list.all()
        print(
            price_policy_list)  # <QuerySet [<PricePolicy: PricePolicy object (1)>, <PricePolicy: PricePolicy object (2)>]>
        for i in price_policy_list:
            print(i)
        """
        PricePolicy object (1)
        PricePolicy object (2)
        """
    except Exception as e:
        print(
            e)  # Cannot resolve keyword 'object_id' into field. Choices are: content_object, content_type, content_type_id, course_id, id, period, price
    return HttpResponse('...')
