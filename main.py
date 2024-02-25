import streamlit as st
import fitz
import os
from tempfile import NamedTemporaryFile


def extract_text_with_coordinates(pdf_path):
    doc = fitz.open(pdf_path)
    text_info = []

    for page_num, page in enumerate(doc):
        # Extrair blocos de texto junto com suas coordenadas
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:  # Verificar se o bloco contém linhas de texto
                for line in b["lines"]:
                    for span in line["spans"]:  # Cada 'span' é um trecho de texto
                        text_info.append({
                            "page": page_num,
                            "text": span["text"],
                            "coordinates": span["bbox"]  # bbox = bounding box (coordenadas)
                        })

    return text_info

# Função principal da aplicação Streamlit
def main():
    st.title("PDF Text Extractor")

    # Upload de arquivos
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Criando um arquivo temporário para armazenar o upload
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            uploaded_file_path = tmp_file.name

        # Extraindo texto e coordenadas
        text_info = extract_text_with_coordinates(uploaded_file_path)

        # Removendo o arquivo temporário
        os.remove(uploaded_file_path)

        # Exibindo o texto extraído
        for info in text_info:
            st.write(f"Page {info['page']}: {info['text']} (Coordinates: {info['coordinates']})")

# Executando a aplicação
if __name__ == "__main__":
    main()