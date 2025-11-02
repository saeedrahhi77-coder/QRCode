import qrcode
import webbrowser

# 1️⃣ لینک مستقیم عکس
image_url = "https://i.ibb.co/20kYStY2/photo-2025-11-02-17-47-43.jpg"

# 2️⃣ ساخت QR
qr = qrcode.make(image_url)
qr_filename = "my_qr_image.png"
qr.save(qr_filename)

# 3️⃣ ساخت فایل HTML (فقط QR وسط صفحه)
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QR Code</title>
  <style>
    body {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f9f9f9;
      font-family: Arial, sans-serif;
    }}
    img {{
      width: 280px;
      height: 280px;
      border: 6px solid #222;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }}
    h2 {{
      color: #333;
      font-weight: normal;
      margin-bottom: 20px;
    }}
  </style>
</head>
<body>
  <h2>Scan this QR Code 👇</h2>
  <img src="{qr_filename}" alt="QR Code">
</body>
</html>
"""

html_filename = "qr_page.html"
with open(html_filename, "w", encoding="utf-8") as f:
    f.write(html_code)

# 4️⃣ باز کردن صفحه در مرورگر
webbrowser.open(html_filename)

print("✅ QR code and HTML page created successfully!")