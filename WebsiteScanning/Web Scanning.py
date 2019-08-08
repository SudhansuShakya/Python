import urllib.request
url=input("Enter Url: ")
text=urllib.request.urlopen(url)
print(text.read().decode('utf-8'))
