from django.shortcuts import render
from django.http import HttpResponse
from portfolio_app.stockdata.resources import StockResource
from tablib import Dataset


def export(request):
    stock_resource = StockResource()
    dataset = stock_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment: filename=stocks.csv'
    return response


def simple_upload(request):
    if request.method == 'POST':
        stock_resource = StockResource()
        dataset = Dataset()
        new_stocks = request.FILES['myfile']
        imported_data = dataset.load(new_stocks.read())
        result = stock_resource.import_data(imported_data, dry_run=True)  # Test the data import
        if not result.has_errors():
            stock_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/secret_page_2.html')


