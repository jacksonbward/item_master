from zeep import Client

client = Client('http://services.promostandards.org/WebServiceRepository/WebServiceRepository.svc?singleWsdl')

servicesTypes = client.service.GerServicesTypes()
services = client.service.GetServices()
companies = client.service.GetCompanies()

with open('serviceTypes.txt', 'w') as f:
    for item in servicesTypes:
        f.write("%s\n" % item)

with open('services.txt', 'w') as f:
    for item in services:
        f.write("%s\n" % item)

with open('companies.txt', 'w') as f:
    for item in companies:
        f.write("%s\n" % item)