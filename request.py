import requests

# URL
url = 'http://localhost:5003/api'

# Change the value of experience that you want to test
# age = int(input('Age : '))
# salary = int(input('Salary :'))
data = {'age':19, 'salary':19000}

r = requests.post(url,json=data)

print(r.json())

