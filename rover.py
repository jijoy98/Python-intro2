import requests
from PIL import Image
from io import BytesIO

api_key = 'DXdeKNbyZHh0oF7jIn0MXpbwTeIhhLYe6CNwdNcc'
rover = 'curiosity'
sol = 1000
camera = 'fhaz'

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': sol,
    'camera': camera,
    'api_key': api_key
}

response = requests.get(url, params=params)
data = response.json()

if data['photos']:
    photo_url = data['photos'][0]['img_src']
    response = requests.get(photo_url)
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print(' No photo Found')