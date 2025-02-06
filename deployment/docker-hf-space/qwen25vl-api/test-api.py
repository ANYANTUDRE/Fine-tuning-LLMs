import requests

url = "https://anyantudre-qwen25vl-api.hf.space/predict"

# Define the parameters
params = {
    "image_url": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
    "prompt": "describe"
}

# Send the GET request
response = requests.get(url, params=params)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
