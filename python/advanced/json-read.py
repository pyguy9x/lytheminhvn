import json
 
with open('customer.json') as wr:
    customers = json.load(wr)
    for customer in customers:
        print(customer, type(customer))