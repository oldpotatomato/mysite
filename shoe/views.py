from django.shortcuts import render
from django.views.decorators.http import require_get,require_post
from .models import User,Shoes
from django.http import JsonResponse



def admin_change(request):
    return render(request, 'admin_change.html')

@require_get
def getusershoes(request):
    try:
        # 接收参数
        userid = request.GET.get('userid')

        user = User.object.get(userid=userid)
        # 有用户返回页面json
        return JsonResponse({'username': user.username, 'shoes': user.shoes})
    except User.DoesNotExist as e:
        # 异常信息说明用户不存在
        return JsonResponse({'msg': '抱歉，在此请求方式下没有Mock数据，请检查您的请求方式与文档中的接口请求方式是否一致（如API的请求方式是POST，则Mock API也需按照POST方式发送请求方可获得数据）或者是否已经填写了Mock数据'})

@require_post
def updateusershoes(request):
    try:
        # 接收参数
        userid = request.POST.get('userid')

        phone = request.POST.get('phone')

        username = request.POST.get('username')

        # 根据userid查询是否有该用户
        username = User.objects.get(userid=userid)

        user = Shoes.object.get(userid=userid)

        # 有用户返回页面json
        return JsonResponse({'success': 'True', 'messsage': 'ok','result':user})
    except User.DoesNotExist as e:
        # 异常信息说明用户不存在
        return JsonResponse({'success': 'False', 'messsage': '储存出错'})



