from django.core.validators import URLValidator
from django.shortcuts import render
from django.views import View
from .models import UrlRecord
from .forms import UrlRecordForm
from mysite.settings import HOSTNAME
from django.shortcuts import redirect

# Create your views here.
class ShortenerView(View):
	def get(self, request, info='', **kwargs):
		url_id = kwargs.get('url_id')
		if url_id:
			# 確認到轉址URL
			this_url_record = UrlRecord.objects.filter(id=url_id).first()
			if this_url_record:
				# return redirect('https://www.google.com/')
				return redirect(this_url_record.origin_url)
		return render(request, 'index.html', {'UrlRecordForm': UrlRecordForm(), 'info': info})
	def post(self, request):
		form = UrlRecordForm(request.POST)
		print(request.POST)
		print('000')
		print(form)
		print(form.is_valid())
		print(form.errors)
		info = ''
		if form.is_valid():
			print(1111)
			
			# 檢查網址一定要http開頭
			cleaned_data = form.cleaned_data
			this_url_record = UrlRecord(origin_url=cleaned_data['origin_url'])
			this_url_record.save()
			# todo要回傳新網址
			# todo 要顯示轉網址結果
			info = '%s新的短網址為%s' % (this_url_record.origin_url, HOSTNAME+'\\'+ str(this_url_record.id))
		else:
			info = form.errors

		return self.get(request, info)