import requests
from requests.auth import HTTPBasicAuth

# --- CONFIGURATION ---
WORDPRESS_URL = "https://yourwordpresssite.com" *************
USERNAME = "Master_Mage"
APP_PASSWORD = "XXXXXXXXX"  # Generated under User > Profile > Application Passwords
PDF_PATH = "Dragon_Heist.pdf"

# --- UPLOAD PDF ---
media_endpoint = f"{WORDPRESS_URL}/wp-json/wp/v2/media"

# Open the file in binary mode
with open(PDF_PATH, 'rb') as pdf_file:
    file_name = PDF_PATH.split('/')[-1]
    headers = {
        'Content-Disposition': f'attachment; filename={file_name}',
        'Content-Type': 'application/pdf'
    }

    response = requests.post(
        media_endpoint,
        headers=headers,
        data=pdf_file,
        auth=HTTPBasicAuth(USERNAME, APP_PASSWORD)
    )

# --- HANDLE RESPONSE ---
if response.status_code == 201:
    uploaded = response.json()
    print("PDF uploaded successfully!")
    print("File URL:", uploaded['source_url'])
else:
    print("Upload failed:", response.status_code)
    print(response.text)
