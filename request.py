import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'aa':0.5, 'bb':0.5, 'cc':1,'a':1, 'b':1, 'c':0.5,'d':0.5, 'e':0.5, 'f':0.5})

print(r.json())
