import http.client as ht

conn = ht.HTTPSConnection("api.msg91.com")

payload = '''{
  "sender": "GCTITA",
  "route": "4",
  "country": "91",
  "sms": [
    {
      "message": "Welcome Rathesh, Today you have Python and CNS class",
      "to": [
        "989128XXXX"
      ]
    },
    {
      "message": "Welcome Billcates, Today you have IS and Open Elective Class",
      "to": [
        "9944XXX102"
      ]
    }
  ]
}'''

headers = {
    'authkey': "**************", #Paste your MSG91 API key here
    'content-type': "application/json"
    }

conn.request("POST", "/api/v2/sendsms", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
