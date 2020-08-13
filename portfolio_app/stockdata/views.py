from django.shortcuts import render
from django.http import HttpResponse
from portfolio_app.stockdata.resources import StockResource
from tablib import Dataset


def export_data(request):
    stock_resource = StockResource()
    dataset = stock_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment: filename=stocks.csv'
    return response


def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        stocks_resource = StockResource()
        dataset = Dataset()
        new_stocks = request.FILES['importData']
        if file_format == 'CSV':
            imported_data = dataset.load(new_stocks.read().decode('utf-8'), format='csv')
            result = stocks_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            imported_data = dataset.load(new_stocks.read().decode('utf-8'), format='json')
            # Testing data import
            result = stocks_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            # Import now
            stocks_resource.import_data(dataset, dry_run=False)

    return render(request, 'secret_page.html')
