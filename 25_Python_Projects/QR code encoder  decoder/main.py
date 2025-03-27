import qrcode
import cv2
from termcolor import colored
def generate_qr_code(data, filename="qr_code.png"):
    """
    Generates a QR code image from the provided data.
    
    :param data: The data to encode in the QR code.
    :param filename: The filename to save the QR code image.
    """
    try:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,  
            box_size=10,  
            border=4, 
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
        print(colored(f"QR code generated and saved as {filename}", 'green'))
    except Exception as e:
        print(colored(f"Error generating QR code: {str(e)}", 'red'))
def decode_qr_code(image_path):
    """
    Decodes a QR code from an image file and prints the decoded data.
    
    :param image_path: The path to the image file containing the QR code.
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("The image file could not be loaded. Please check the file path.")
        detector = cv2.QRCodeDetector()
        value, pts, qr_code = detector(img)
        if value:
            print(colored(f"Decoded QR Code data: {value}", 'blue'))
        else:
            print(colored("QR code could not be decoded.", 'yellow'))
    except Exception as e:
        print(colored(f"Error decoding QR code: {str(e)}", 'red'))
def main():
    print(colored("QR Code Encoder / Decoder", 'cyan'))
    try:
        choice = input(colored("Do you want to (1) Encode or (2) Decode a QR code? (Enter 1 or 2): ", 'magenta'))
        if choice == '1':
            data = input(colored("Enter the data to encode into the QR code: ", 'magenta'))
            generate_qr_code(data)
        elif choice == '2':
            image_path = input(colored("Enter the path to the QR code image: ", 'magenta'))
            decode_qr_code(image_path)
        else:
            print(colored("Invalid choice. Please select 1 to encode or 2 to decode.", 'red'))
    except Exception as e:
        print(colored(f"An error occurred: {str(e)}", 'red'))
if __name__ == "__main__":
    main()
