import requests
import base64

# read and encode img to base64
with open("C:/Users/Erlangga/Downloads/logo_bank_jatim.png", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()

# send POST request to API
response = requests.post(
    "http://127.0.0.1:5000/remove-bg",
    json={"image_base64": encoded}
)

# save base64 output to file .png
if response.status_code == 200 and 'image_base64' in response.json():
    output_base64 = response.json()["image_base64"]
    with open("output.png", "wb") as f:
        f.write(base64.b64decode(output_base64))
    print("✅ Output disimpan sebagai output.png")
else:
    print("❌ Error:", response.json())
