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
    添加一条普通课程为“Python”价格为99.9，学习周期为3个月的价格策略记录()
    """
    course_obj = models.Course.objects.filter(name='Python').first()
    print(course_obj)  # Course object (1)
    # 首先需要获取根据课程的名称获取课程的id
    course_id = course_obj.id
    # 然后还要获取content_type表中course表对应的id
    content_type_obj = models.ContentType.objects.filter(model='course').first()
    content_type_id = content_type_obj.id
    models.PricePolicy.objects.create(price=99.9, period=3, course_id=course_id, content_type_id=content_type_id)
    return HttpResponse('...')
