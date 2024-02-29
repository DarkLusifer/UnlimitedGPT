# ===================Demo code==================== #
import requests

#GET method
url = "https://testapi-pwp4.onrender.com/api/ai?prompt=YOUR_TEXT"
re = get(url)

print(re.text)

#POST method
url = "https://testapi-pwp4.onrender.com/api/ai"
data = {
    "prompt":"YOUR_TEXT"
    }
re = requests.post(url, json=data)

print(re.text)
# ================================================= #


# API ownership alright received ©️ Mr_darklusifer
