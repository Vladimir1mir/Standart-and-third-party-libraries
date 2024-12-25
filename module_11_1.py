import requests
import pprint
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

'''
requests - позволяет быстро работать с запросами 
с наименьшей строкой кода
'''
response = requests.get('https://api.github.com')
response_json = response.json()
pprint.pprint(response.json)
print(response_json['repository_search_url'])

img_url = 'https://repository-images.githubusercontent.com/663291669/42953e67-0e46-40d1-bd3b-ea562c8bf878'
response_1 = requests.get(img_url)
with open('image.jpg', 'wb') as file:
    file.write(response_1.content)

"""" 
Библиотека pillow, довольна интересна. Работа с фотографиями и картинками, хорошо бы 
зашла тем, кто работает с фотошопом или возможно клепает визуал сайта с однотипными блокам
(изменение размеров картинки, формата, выделение области обрезки, и разные эффекты).
Есть возможность откорректировать разом все фотографии одним разом прописав определенный
код, что значительно может ускорить работу.
"""

img = Image.open('image.jpg')
new_name = 'image.png'
img.save(new_name)

img1 = Image.open('image.png')
print(img1.format, img1.size, img1.mode)
new_size = (240, 320)
img1.thumbnail(new_size)
img1.save('image_size.png')
img1.show()

img2 = img.crop((600, 200, 1940, 1440))
img2.save('image_box.jpg')
img2.show()

img = Image.open('image.jpg')
img = img.convert('L')
img.save('image_new.jpg')

'''
matplotlib - с помощью данной библиотеки можно визуализировать данные, построить любые виды графиков.
'''

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 12, 67, 34]

plt.bar(categories, values)
plt.show()

'''
numpy - Библиотека для работы с многомерными массивами.
'''

a = np.array([1, 2, 3])
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a)
print(a1)
print(a2)
