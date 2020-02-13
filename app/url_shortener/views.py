from django.core.validators import URLValidator
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from .models import UrlRecord
from .forms import UrlRecordForm

# Create your views here.
class ShortenerView(View):
	def get(self, request, info='', **kwargs):
		key = kwargs.get('key')
		if key:
			info = '%s 為無效的縮網址' % UrlRecord.shortener_url(key)

			try: 
				this_url_record = UrlRecord.objects.get(id=key)
				if this_url_record:
					info = ''
					return redirect(this_url_record.origin_url)
			except:
				pass

		return render(request, 'index.html', {'UrlRecordForm': UrlRecordForm(), 'info': info})

	def post(self, request, **kwargs):
		form = UrlRecordForm(request.POST)
		info = ''
		if form.is_valid():			
			# 檢查網址一定要http開頭
			cleaned_data = form.cleaned_data
			this_url_record = UrlRecord(origin_url=cleaned_data['origin_url'])
			this_url_record.save()
			info = '%s\n 新的短網址為 \n%s' % (this_url_record.origin_url, UrlRecord.shortener_url(this_url_record.id))
		else:
			info = '網址的格式不正確!'

		return self.get(request, info)