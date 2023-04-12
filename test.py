import base64
import requests
import os
api_url = "http://127.0.0.1:5000/predict" 

def uploadFile(filepath:str,filename:str):
    # with open(filepath, "rb") as img:
    #     imgstring = img.read()
    # with open(filepath, 'rb') as file:
    #     imgstring = file.read().replace('\\n', '').replace('\\','').replace("b'",'')
    #     imgstring = imgstring + '=' * (4 - len(imgstring) % 4)
    #     imgstring = base64.b64encode(imgstring)
    # print(type(string))
    # print(string)
    response = requests.post(url= api_url, json={
            'user_photo': filepath,
            'filename': filename,
            'uname': "Ansh",
            'gender': "Male"
            })
    # response = requests.post(url= api_url, json={'user_photo': str(string)})
    res_json = response.json()
    print(res_json)

folder = r"D:/PROJECTS/UPLOADS/"
filename = "Dablu.jpg"
filepath = os.path.join(folder, filename)
uploadFile(filepath=filepath,filename=filename)