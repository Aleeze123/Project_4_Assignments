# QR Code Encoder / Decoder 🛠️

Welcome to the **QR Code Encoder / Decoder** project! This is a Python-based application that allows you to generate QR codes and decode them from images. The project uses the `qrcode` library for encoding and `OpenCV` for decoding QR codes.

## Features ✨
- **Encode QR Code** 📱: You can input any text or URL, and the program will generate a QR code image.
- **Decode QR Code** 🔍: You can scan any QR code image, and the program will extract the encoded information.
- **Error Handling** ⚠️: The program will handle errors gracefully, such as invalid file paths and unreadable images.

## Requirements 📦
Before running the project, make sure you have the following libraries installed:
- `qrcode[pil]` for generating QR codes.
- `opencv-python` for decoding QR codes from images.

You can install these dependencies using pip:
```bash
pip install qrcode[pil]
pip install opencv-python