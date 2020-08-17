from django.shortcuts import render
from django.http import HttpResponse
from portfolio_app.stockdata.resources import StockResource
from tablib import Dataset
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError


def export_data(request):
    stock_resource = StockResource()
    dataset = stock_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment: filename=stocks.csv'
    return response


def import_data(request):
    if request.method == 'POST':
        stocks_resource = StockResource()
        dataset = Dataset()
        try:
            new_stocks = request.FILES['importData']
        except MultiValueDictKeyError:
            messages.warning(request, 'Firstly you have to pick a file!')
            return render(request, 'secret_page.html')
        imported_data = dataset.load(new_stocks.read().decode('utf-8'), format='csv')
        result = stocks_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            # Import now
            messages.success(request, 'Upload done successfully!')
            stocks_resource.import_data(dataset, dry_run=False)
        else:
            messages.warning(request, 'Data is already in database!')
            return render(request, 'secret_page.html')

    return render(request, 'secret_page.html')
