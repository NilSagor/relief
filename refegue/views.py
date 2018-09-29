from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

import django_filters
from django.conf import settings
from django.urls import reverse

from collections import OrderedDict

from django import forms
from .models import Request, DistrictManager, Volunteer, NGO, PrivateRescueCamp, CollectionCenter, Contributor
from refegue.sms_handler import send_confirmation_sms

# Create your views here.


class CustomForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CustomForm, self).__init__(*args, *kwargs)

PER_PAGE = 100
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
		'needrescue',
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
		'needkit_utils',
		'detailkit_utils',
		'needtoilet',
		'detailtoilet',
		'needothers',
		]
	success_url = '/req_success/'

	def form_valid(self, form):
		self.object = form.save()
		sms_queue.enqueue(
			send_confirmation_sms, self.object.requestee_phone
		)
		return HttpResponseRedirect(self.get_success_url())

class RegisterVolunteer(CreateView):
	model = Volunteer
	fields = [
		'name', 
		'district', 
		'phone', 
		'organization', 
		'area', 
		'address'
		] 
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

'''
Ngo view 
'''
class RegisterNGO(CreateView):
	model = NGO
	fields = [
		'organization',
		'organization_type',
		'organization_address',
		'district',
		'name',
		'phone',
		'area',
		'description',
		'website_url',
		'location',
	]
	success_url = '/reg_success'

def download_ngo_list(request):
	district = request.GET.get('district', None)
	filename = 'ngo_list.csv'
	if district is not None:
		filename = 'ngo_list_{0}.csv'.format(district)
		qs = NGO.objects.filter(district = district).order_by('district', 'name')
	else:
		qs = NGO.objects.all().order_by('district', 'name')
	header_row = [
		'organization',
		'Type',
		'Address',
		'Name',
		'Phone',
		'Description',
		'District',
		'Area',
		'Location',
	]
	body_rows = qs.values_list(
		'organization',
		'organization_type',
		'organization_address',
		'name',
		'phone',
		'description',
		'district',
		'area',
		'location',
	)
	return create_csv_response(filename, header_row, body_rows)



def request_list(request):
	filter = RequestFilter(request.GET, queryset = Request.objects.exclude(status = 'sup'))
	req_data = filter.qs.order_by('-id')
	paginator = Paginator(req_data, PER_PAGE)
	page = request.GET.get('page')
	req_data.min_page = req_data.number - PAGE_LEFT
	req_data.max_page = req_data.number + PAGE_RIGHT
	req_data.lim_page = PAGE_INTERMEDIATE
	return render(request, 'refegue/request_list.html', {'filter': filter, 'data': req_data })

def ngo_list(request):
	filter = NGOFilter(request.GET, queryset = NGO.objects.all())
	ngo_data = filter.qs.order_by('-id')
	paginator = Paginator(ngo_data, PER_PAGE)
	page = request.GET.get('page')
	ngo_data = paginator.get_page(page)
	ngo_data.min_page = ngo_data.number - PAGE_LEFT
	ngo_data.max_page = ngo_data.number + PAGE_RIGHT
	ngo_data.lim_page = PAGE_INTERMEDIATE

	return render(request, 'refegue/ngo_list.html', {'filter': filter, 'data': ngo_data})

def request_details(request, request_id = None):
	if not request_id:
		return HttpResponseRedirect('/error?error_text={}'.format('Page not found'))
	filter = RequestFilter(None)
	try:
		req_data = RequestUpdate.objects.get(id = request_id)
		updates = RequestUpdate.objects.all().filter(request_id=request_id).order_by('-update_ts')
	except Exception as e:
		return HttpResponseRedirect('/error?error_text={}'.format('Sorry, we couldnot fetch details for that request'))
		return render(request, 'refegue/request_details.html', {'filter':filter, 'req':req_data, 'updates': updates})
		raise e
	
class RegisterPrivateReliefCampForm(forms.ModelForm):
	class Meta:
		model = PrivateRescueCamp
		fields = [
			'name',
			'location',
			'district',
			'lsg_name',
			'ward_name',
			'contacts',
			'facilities_available',
			'map_link',
			'latlng',
			'total_people',
			'total_males',
			'total_females',
			'total_infants',
			'food_req',
			'clothing_req',
			'sanitry_req',
			'medical_req',
			'other_req'
		]
		widgets = {
			'lsg_name': forms.Select(),
			'ward_name': forms.Select()
		}

class RegisterPrivateReliefcamp(CreateView):
	model = PrivateRescueCamp
	success_url = '/pcamp'
	form_class = RegisterPrivateReliefCampForm

def pcamplist(request):
	filter = PrivateCampFilter(request.GET, queryset = PrivateRescueCamp.objects.all())
	data = filter.qs.order_by('-id')
	paginator = Paginator(data, 50)
	page = request.GET.get('page')
	data = paginator.get_page(page)

	return render(request, 'refegue/pcamplist.html', {'filter': filter, 'data': data})

class RegisterContributor(CreateView):
	model = Contributor
	fields = [
		'name',
		'district',
		'phone',
		'address',
		'contribution_type',
		'contrib_details'
	]
	success_url = '/contrib_success/'

class ContribFilter(django_filters.FilterSet):
	class Meta:
		model = Contributor
		fields = {
			'district':['exact'],
			'name':['icontains'],
			'phone':['exact'],
			'status':['exact'],
			'address':['icontains'],
			'contrib_details':['icontains'],
		}

	def __init__(self, *args, **kwargs):
		super(ContribFilter, self).__init__(*args, **kwargs)
		if self.data == {}:
			self.queryset = self.queryset.none()

def contributors(request):
	filter = ContribFilter(request.GET, queryset = Contributor.objects.all())
	contrib_data = filter.qs.order_by('-id')
	paginator = Paginator(contrib_data, PER_PAGE)
	page = request.GET.get('page')
	contrib_data.min_page = contrib_data.number - PAGE_LEFT
	contrib_data.max_page = contrib_data.number + PAGE_RIGHT
	contrib_data.lim_page = PAGE_INTERMEDIATE

	return render(request, 'refegue/contrib_list.html', {'filter': filter, 'data': contrib_data})

def privatecc(request):
	return render(request, 'privatecc.html')

class HomePageView(TemplateView):
	template_name = 'home.html'

class ReqSuccess(TemplateView):
	template_name = 'refegue/req_success.html'

class RegSuccess(TemplateView):
	template_name = 'refegue/reg_success.html'

class ContribSuccess(TemplateView):
	template_name = 'refegue/contrib_success.html'
	
class DisclaimerPage(TemplateView):
	template_name = 'refegue/disclaimer.html'

class AboutIEEE(TemplateView):
	template_name = 'refegue/aboutieee.html'

class DistrictManagerFilter(django_filters.FilterSet):
	class Meta:
		model: DistrictManager
		fields: ['districts']

	def __init__(self, *args, **kwargs):
		super(DistrictManagerFilter, self).__init__(*args, **kwargs)
		if self.data == {}:
			self.queryset = self.queryset.none()

def districtmanager_list(request):
	filter = DistrictManagerFilter(request.GET, queryset=DistrictManager.objects.all())
	return render(request, 'refegue/districtmanager_list.html', {'filter': filter})

class DistNeeds(TemplateView):
	template_name = 'refegue/district_needs.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['district_data'] = DistrictNeed.objects.all()
		return context 

class CollectionCenterFilter(django_filters.FilterSet):
	lsg_name = django_filters.ChoiceFilter()
	ward_name = django_filters.ChoiceFilter()

	class Meta:
		model = CollectionCenter
		fields = OrderedDict()
		fields['name']=['icontains']
		fields['address']=['icontains']
		fields['contacts']=['icontains']
		fields['district']=['exact']
		fields['lsg_name']=['exact']
		fields['ward_name']=['exact']

	def __init__(self, *args, **kwargs):
		super(CollectionCenterFilter, self).__init__(*args, **kwargs)
		if self.data=={}:
			self.queryset=self.queryset.none()

class CollectionCenterListView(ListView):
	model = CollectionCenter
	paginated_by = PER_PAGE
	ordering = ['-id']

	def get_context_data(self, **kwargs):

		location = self.kwargs['location']
		inside_kerala = True if location == 'inside_kerala' else False
		context = super().get_context_data(**kwargs)
		context['inside_kerala'] = inside_kerala
		context['filter']= CollectionCenterFilter(
			self.request.GET, 
			queryset = CollectionCenter.objects.filter(is_inside_kerala = inside_kerala).order_by('-id')
			)
		
		return context

class CollectionCenterForm(forms.ModelForm):
	class Meta:
		model = CollectionCenter
		fields = [
		'name',
		'address',
		'contacts',
		'type_of_materials_collecting',
		'is_inside_kerala',
		'district',
		'lsg_name',
		'ward_name',
		'city',
		'map_link',
		]

		widgets = {
			'lsg_name': forms.Select(),
			'ward_name': forms.Select(),
		}

class CollectionCenterView(CreateView):
	model = CollectionCenter
	form_class = CollectionCenterForm
	success_url = '/collection_centers/'

