import cv2

def qr_reader(image):
    img = cv2.imread(image)

    if img is None:
        return "Error: Image not found."

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        return data
    else:
        return "No QR code detected."

print(qr_reader("QR Code.png"))
