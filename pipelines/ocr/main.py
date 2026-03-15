from paddleocr import PaddleOCR

def main():
    ocr = PaddleOCR(
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )

    result = ocr.predict(image)

    for page in result:
        for text in page["rec_texts"]:
            print(text)


if __name__ == "__main__":
    main()
