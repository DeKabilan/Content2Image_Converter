
"""if you run this code it will prompts you for the keyword to search for,
then around 20 images respective to your keyword will be downloaded locally"""

from serpapi import GoogleSearch
import requests,os
from PIL import Image
import requests
import io
import config
from PIL import Image
import random


search_key = input("Keyword: ")

query = search_key
print(query)
    
params = {
  "q": search_key,
  "engine": "google_images",
  "ijn": random.randint(1,5),
  "api_key": config.api_key
}

search = GoogleSearch(params)
results = search.get_dict()
images_results = results["images_results"]
count = 0
result = []
for img in range(3):
    result.append(results["images_results"][img]["original"])
    if "gif" not in result[img].split("."):
        print(result)
        count += 1
print(count)


def save_images(search_key,image_urls):
       
       min_re=(0,0)
       max_re=(1920,1080)
       for indx,image_url in enumerate(image_urls):
           try:
               search_string = ''.join(e for e in search_key if e.isalnum())
               image = requests.get(image_url,timeout=5)
               if image.status_code == 200:
                   with Image.open(io.BytesIO(image.content)) as image_from_web:
                       try:
                           filename = "%s%s.%s"%(search_string,str(indx),
                           image_from_web.format.lower())
                           image_path = os.path.join(r"C:\Users\RAJ\OneDrive\Pictures\New folder", filename)
                           image_from_web.save(image_path)
                       except OSError:
                           print("some exception needs to be done")
                           rgb_im = image_from_web.convert('RGB')
                           rgb_im.save(image_path)
                       image_resolution = image_from_web.size
                       if image_resolution != None:
                           if image_resolution[0]<min_re[0] or image_resolution[1]<min_re[1] or image_resolution[0]>max_re[0] or image_resolution[1]>max_re[1]:
                              image_from_web.close()
                              os.remove(image_path)
                       image_from_web.close()
           except Exception as e:              
               print(e)

save_images(search_key,result)