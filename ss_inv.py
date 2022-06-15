from zeep import Client, Settings

promo_url = 'http://services.promostandards.org/WebServiceRepository/WebServiceRepository.svc?singleWsdl'
# ss = Client('https://promostandards.ssactivewear.com/productdata/v2/productdataservicev2.svc?wsdl')
ps_client = Client(promo_url)

endpoints = ps_client.service.GetCompanyEndpointsByServiceVersion('SS', 'INV', '2.0.0')
with open('ssendpoints.txt', 'w') as f:
    for item in endpoints:
        f.write("%s\n" % item)

request_data = {
    'wsVersion': '2.0.0', 
    'id': '07675', 
    'password': '650a74a4-649d-4a8d-ac9b-1c94e9b51bf3', 
    'productId': '6030'
}

settings = Settings(strict=False)

for item in endpoints:
    client = Client(item.URL + '?WSDL', settings=settings)
    r = client.service.getInventoryLevels(**request_data)
    with open('out.txt', 'w') as f:
        f.write(str(r))