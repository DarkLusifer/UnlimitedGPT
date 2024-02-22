# ===================Demo code==================== #
import requests

url = "https://testapi-pwp4.onrender.com/api/ai"
data = {
    "prompt":"hello"
    }

re = requests.post(url, json=data)

print(re.text)
# ================================================= #


# API ownership alright received ©️ Mr_darklusifer
