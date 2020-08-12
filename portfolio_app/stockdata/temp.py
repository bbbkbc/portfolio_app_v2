from portfolio_app.stockdata.resources import StockResource

person_resource = StockResource()
dataset = person_resource.export()
print(dataset)