import requests
url='http://localhost:5000/predict_api'

data={    
    'review': 'This product is amazing, I love it!'
}
response=requests.post(url, json=data)
print(response.json())