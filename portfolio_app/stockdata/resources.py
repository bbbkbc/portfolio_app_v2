from import_export import resources
from portfolio_app.stockdata.models import Stock


class StockResource(resources.ModelResource):
    class Meta:
        model = Stock
