from django.shortcuts import render
from django.views import View
from .models import UrlRecord
from .forms import UrlRecordForm
from django.shortcuts import redirect

# Create your views here.
class ShortenerView(View):
	def get(self, request, **kwargs):
		url_id = kwargs.get('url_id')
		if url_id:
			# 確認到轉址URL
			this_url_record = UrlRecord.objects.filter(id=url_id).first()
			if this_url_record:
				# return redirect('www.google.com')
				# return redirect('https://www.google.com/')
				# todo 找出不用加上https的轉網址方法
				return redirect('https://' + this_url_record.origin_url)
		return render(request, 'index.html', {'UrlRecordForm': UrlRecordForm()})
	def post(self, request):
		form = UrlRecordForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			this_url_record = UrlRecord(origin_url=cleaned_data['origin_url'])
			this_url_record.save()
			# todo要回傳新網址
			# todo 要顯示轉網址結果
		return self.get(request)