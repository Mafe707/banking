from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Countries
from .forms import CountryForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse("This is my first view!!!!")

def country_list(request):
    query = request.GET.get('q')
    status_filter = request.GET.get('status')

    countries_list = Countries.objects.all().order_by('name')

    if query:
        countries_list = countries_list.filter(name__icontains=query) | countries_list.filter(abrev__icontains=query)

    if status_filter in ['true', 'false']:
        countries_list = countries_list.filter(status=(status_filter == 'true'))

    paginator = Paginator(countries_list, 10)  # 10 por página
    page_number = request.GET.get('page')
    countries = paginator.get_page(page_number)

    return render(request, 'banking_app/country_list.html', {
        'countries': countries,
        'query': query,
        'status_filter': status_filter
    })

def country_edit(request, pk):
    country = get_object_or_404(Countries, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('banking_app:country_list')
    else:
        form = CountryForm(instance=country)

    return render(request, 'banking_app/country_form.html', {'form': form, 'country': country})

def country_delete(request, pk):
    country = get_object_or_404(Countries, pk=pk)
    if request.method == 'POST':
        country.delete()
        messages.success(request, 'País eliminado correctamente.')
        return redirect('banking_app:country_list')
    return render(request, 'banking_app/country_confirm_delete.html', {'country': country})
