from django.contrib import admin
from portfolio_app.stockdata.models import Stock, Index
from import_export.admin import ImportExportModelAdmin

admin.site.register(Index)


@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    pass

