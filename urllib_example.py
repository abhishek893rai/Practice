import urllib.request
import urllib.parse

# x = urllib.request.urlopen('https://www.udemy.com/courses/')
# print(x.read())

# url = 'http://www.pythonprogramming.net'
# values = {
#
#     's':'basic',
#     'submit':'search'
# }
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url,data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# saveFile = open("saveData.txt",'w')
# saveFile.write(str(respData))
# saveFile.close()
# print(respData)

try:
    url = 'https://www.google.co.in/?gfe_rd=cr&ei=QPbNVpaSI8X08wep44HwAQ&gws_rd=ssl#q=test'
    # searchItem = input("search?")
    # values = { 'q':searchItem }
    # data = urllib.parse.urlencode(values)
    # data = data.encode('utf-8')
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile = open("saveData1.txt",'w')
    saveFile.write(respData)
    saveFile.close()
except Exception as e:
    print('this is the error-',str(e))


