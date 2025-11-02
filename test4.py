import qrcode

# Direct image link
image_url = "https://i.ibb.co/20kYStY2/photo-2025-11-02-17-47-43.jpg"

# Create QR code
qr = qrcode.make(image_url)

# Save QR image in the same folder
qr.save("my_qr_image.png")

print("✅ QR code created successfully! Check the file 'my_qr_image.png' in your folder.")