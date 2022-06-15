from zeep import Client

staton = Client('https://statononline.com/promostandards/wsdl/test/Inventory_200.wsdl')

print(staton)