import os
import cv2
from paddleocr import PaddleOCR

def preprocess_image(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    
    return image

def run_ocr(image: any):
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )
    return ocr.predict(image)

def extract_fields(ocr_result):
    pass

def main():
    image_path = os.path.join(os.path.dirname(__file__), "receipt.png")
    image = preprocess_image(image_path)
    result = run_ocr(image)
    extract_fields(result)
    for page in result:
        for text in page["rec_texts"]:
            print(text)

if __name__ == "__main__":
    main()