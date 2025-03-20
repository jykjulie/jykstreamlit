import streamlit as st
import json
import os

DATA_FILE = "latest_text.json"

##### 데이터 불러오기 & 저장 함수 #####
def load_latest_text():
    """저장된 최신 텍스트 불러오기"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("text", "")
    return ""

def save_latest_text(text):
    """최신 텍스트 저장"""
    with open(DATA_FILE, "w") as file:
        json.dump({"text": text}, file)

##### 메인 앱 #####
def main():
    st.set_page_config(page_title="텍스트 저장", layout="centered")

    # 최신 텍스트 불러오기
    latest_text = load_latest_text()

    # 입력 필드
    text = st.text_area("입력할 텍스트", height=100)

    # 저장 버튼
    if st.button("저장"):
        if text.strip():  # 빈 값 방지
            save_latest_text(text)  # 파일 저장
            st.experimental_rerun()  # 새로고침하여 최신 데이터 반영

    # 최신 저장된 텍스트 표시
    if latest_text:
        st.subheader("📌 최신 저장된 텍스트")
        st.write(latest_text)

if __name__ == "__main__":
    main()
