import streamlit as st
import os
import pdf_extractor
from tempfile import NamedTemporaryFile

# Função para mostrar o leitor de PDF
def show_pdf_reader():
    st.title("PDF Text Extractor")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            uploaded_file_path = tmp_file.name

        text_info = pdf_extractor.extract_text_with_coordinates(uploaded_file_path)
        os.remove(uploaded_file_path)

        extracted_text = "\n".join([f"Page {info['page']}: {info['text']} (Coordinates: {info['coordinates']})" for info in text_info])
        st.text_area("Extracted Text", extracted_text, height=300)

# Função principal da aplicação Streamlit
def main():
    st.sidebar.title("Menu")

    # Adicionando uma imagem de capa à sidebar
    # st.sidebar.image("caminho_para_sua_imagem.jpg", use_column_width=True)

    # app_mode = st.sidebar.selectbox("Choose the App mode", ["Home", "PDF Reader", "Other Functionality"])
    app_mode = st.sidebar.selectbox("Choose the App mode", ["PDF Reader", "Other Functionality"])

    if app_mode == "PDF Reader":
        show_pdf_reader()
    elif app_mode == "Home":
        st.write("Welcome to the Home Page")
        # Aqui você pode adicionar mais conteúdo para a página inicial
    elif app_mode == "Other Functionality":
        st.write("Other functionality will be here")
        # Implementar outras funcionalidades aqui

if __name__ == "__main__":
    main()
