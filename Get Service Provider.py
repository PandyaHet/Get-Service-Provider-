import phonenumbers
from phonenumbers import carrier
mobileNo  = input("enter Mobile Number With Country Code:")
service_provider = phonenumbers.parse(mobileNo)
print(carrier.name_for_number(service_provider,"en"))