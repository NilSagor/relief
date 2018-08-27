from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

import django_filters

from django import forms
from .models import Request, DistrictManager
from refegue.sms_handler import send_confirmation_sms

# Create your views here.


class CustomForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CustomForm, self).__init__(*args, *kwargs)

PER_PAGE = 500
PAGE_LEFT = 5
PAGE_RIGHT = 5
PAGE_INTERMEDIATE = '50'

class CreateRequest(CreateView):
	model = Request 
	template_name = 'refegue/request_form.html'
	fields = [
		'district',
		'location',
		'requestee',
		'requestee_phone',
		'is_request_for_others',
		'latlng',
		'latlng_accuracy',
		'needrescue'
		'detailrescue',
		'needwater',
		'detailrescue',
		'needwater',
		'detailwater',
		'needfood',
		'detailfood',
		'needcloth',
		'detailcloth',
		'needmed',
		'detailmed',
		'needkit_util',
		'detailkit_util',
		'needtoilet',
		'detailtoilet',
		'needothers',
		]
	success_url = '/req_rescue/'

	def form_valid(self, form):
		self.object = form.save()
		sms_queue.enqueue(send_confirmation_sms, self.object.requestee_phone)
		return HttpResponseRedirect(self.get_success_url())

class RegisterVolunteer(CreateViewte):
	model = Volunteer
	fields = ['name', 'district', 'phone', 'organization', 'area', 'address'] 
	success_url = '/reg_success/'
def volunteerdata(request):
	filter = VolunteerFilter(request.GET, queryset = Volunteer.objects.all())
	req_data = filter.qs.order_by('-id')
	paginator = Paginator(req_data, PER_PAGE)
	page = request.GET.get('page')
	req_data = paginator.get_page(page)
	req_data.min_page = req_data.number - PAGE_LEFT
	req_data.max_page = req_data.number + PAGE_RIGHT
	req_data.lim_page = PAGE_INTERMEDIATE
	return render(request, 'refegue/volunteerview.html', {'filter': filter, 'data': req_data })

class HomePageView(TemplateView):
	template_name = 'home.html'

class ReqSuccess(TemplateView):
	template_name = 'refegue/req_success.html'

class RegSuccess(TemplateView):
	template_name = 'refegue/reg_success.html'



def districtmanager_list(request):
	filter = DistrictManagerFilter(request.GET, queryset=DistrictManager.objects.all())
	return render(request, 'refegue/districtmanager_list.html', {'filter': filter})
