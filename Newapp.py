import streamlit as st
import requests

API_URL = "https://my-fastapi-service.onrender.com/convert"

st.title("🚀 AI Mainframe Modernizer")
uploaded_file = st.file_uploader("Upload Legacy File", type=["txt","cbl","jcl"])
prompt = st.text_area("Enter modernization prompt",
                      "Convert this COBOL program to Java with Spring Boot")

if st.button("Modernize Code") and uploaded_file:
    files = {'file': uploaded_file.getvalue()}
    data = {'prompt': prompt}

    res = requests.post(API_URL, files=files, data=data)
    if res.status_code == 200:
        modern_code = res.json()["converted_code"]
        st.code(modern_code, language='java')
        st.download_button("Download Modern Code", modern_code)
    api_thread = threading.Thread(target=run_api)
    api_thread.start()