from django.shortcuts import render

# Create your views here.
from art_app.models import Details


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        books = Details.objects.filter(details_title__icontains=keyword).values('details_id', 'details_title','image_url','details_js').order_by(
            'details_id')
        return render(request, 'sear.html', {'books': books})
    else:
        return render(request, 'error/400.html')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 't15623456@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 't123456'
# 收件人看到的发件人
EMAIL_FROM = 't15623456@163.com>'
