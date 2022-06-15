from zeep import Client, Settings
from settings import credentials

promo_url = 'http://services.promostandards.org/WebServiceRepository/WebServiceRepository.svc?singleWsdl'
ps_client = Client(promo_url)

endpoints = ps_client.service.GetCompanyEndpointsByServiceVersion('SS', 'Product', '2.0.0')
with open('ssendpoints.txt', 'w') as f:
    for item in endpoints:
        f.write("%s\n" % item)

request_data = {
    'wsVersion': '2.0.0', 
    'id': credentials['SS']['id'],
    'password': credentials['SS']['password'],
    # 'productId': '6030CC',
    'productId': '6030',
    'localizationCountry': 'US',
    'localizationLanguage': 'en'
}

# Settings for Zeep client
settings = Settings(strict=False)

for item in endpoints:
    client = Client(item.URL + '?WSDL', settings=settings)
    r = client.service.getProduct(**request_data)
    with open('out.txt', 'w') as f:
        f.write(str(r))