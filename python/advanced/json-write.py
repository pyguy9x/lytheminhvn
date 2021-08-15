import json
 
customers = [
    {
        "id": 1,
        "email": "isidro_von@hotmail.com",
        "first": "Hiếu",
        "last": "Nguyễn Văn",
        "company": "Zalo",
        "created_at": "2014-12-25T04:06:27.981Z",
        "country": "Việt Nam"
    },
    {
        "id": 2,
        "email": "frederique19@gmail.com",
        "first": "Micah",
        "last": "Sanford",
        "company": "Stokes-Reichel",
        "created_at": "2014-07-03T16:08:17.044Z",
        "country": "Democratic People's Republic of Korea"
    }
]
 
with open('customer.json', 'w') as wr:
    json.dump(customers, wr, ensure_ascii=True, indent=2)