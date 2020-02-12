from django.shortcuts import render
from django.views import View
from .models import UrlRecord
from .forms import UrlRecordForm

# Create your views here.
class ShortenerView(View):
	def get(self, request):
		return render(request, 'index.html', {'UrlRecordForm': UrlRecordForm()})
	def post(self, request):
		form = UrlRecordForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			this_url_record = UrlRecord(origin_url=cleaned_data['origin_url'])
			this_url_record.save()
			# todo要回傳新網址

		return self.get(request)