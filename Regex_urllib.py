import urllib.request
import urllib.parse
import re

try:
    url = 'http://www.pythonprogramming.net'
    values = {'s':'basics',
               'submit':'search'}
    data = urllib.parse.urlencode(values)
    #data = data.encode('utf-8') #converts to byte
    #print(data,"\n")
    #req = urllib.request.Request(url,data)
    #resp = urllib.request.urlopen(req)

    resp = urllib.request.urlopen(url+'?'+data)
    respData = resp.read()
    parsedData = re.findall(r'<p>(.*?)</p>',str(respData))
    for i in parsedData:
        print(i)
except Exception as e:
    print(str(e))
