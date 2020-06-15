import http.client as ht

conn = ht.HTTPSConnection("api.msg91.com")

payload = '''{
  "sender": "GCTITA",
  "route": "4",
  "country": "91",
  "sms": [
    {
      "message": "Welcome Ajith, Today you have PC class",
      "to": [
        "9090XX8921"
      ]
    },
    {
      "message": "Welcome Shanmugam, Today you have WT Class",
      "to": [
        "901X83XX01"
      ]
    }
  ]
}'''

headers = {
    'authkey': "************", #Paster Your MSG91 API Key
    'content-type': "application/json"
    }

conn.request("POST", "/api/v2/sendsms", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
