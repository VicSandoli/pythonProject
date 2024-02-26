import fitz  # PyMuPDF

# Função para extrair texto e coordenadas do PDF
def extract_text_with_coordinates(pdf_path):
    doc = fitz.open(pdf_path)
    text_info = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    for span in line["spans"]:
                        text_info.append({
                            "page": page_num,
                            "text": span["text"],
                            "coordinates": span["bbox"]
                        })

    doc.close()
    return text_info