import http.client as ht

conn = ht.HTTPSConnection("api.msg91.com")

payload = '''{
  "sender": "GCTITA",
  "route": "4",
  "country": "91",
  "sms": [
    {
      "message": "Rathesh",
      "to": [
        "8124807980"
      ]
    },
{
      "message": "Rasega",
      "to": [
        "9952280500"
      ]
    }	
  ]
}'''

headers = {
    'authkey': "332298AXTbJ0gG5ee3d59eP1",
    'content-type': "application/json"
    }

conn.request("POST", "/api/v2/sendsms?campaign=&response=&afterminutes=&schtime=&unicode=&flash=&message=&encrypt=&authkey=&mobiles=&route=&sender=&country=91", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
