from django.forms import ModelForm
from .models import UrlRecord
class UrlRecordForm(ModelForm):
	class Meta:
		model = UrlRecord
		fields = ['origin_url']