from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

def main():
    load_dotenv()
    st.set_page_config(page_title="AskIt!!")
    st.header("Ask your pdf :books:")

    pdf  = st.file_uploader("Upload your PDF",type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        chunks = text_splitter.split_text(text)

        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")

        knowledge_base = FAISS.from_texts(chunks, embeddings)

        user_query = st.text_input("Ask your question")
        if user_query:
            docs = knowledge_base.similarity_search(user_query)
            llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0, "max_length":512})
            chain = load_qa_chain(llm, chain_type="stuff")
            response  = chain.run(input_documents=docs, question=user_query)
            st.write(response)

if __name__ == '__main__':
    main()
