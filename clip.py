import streamlit as st
import json
import os
from datetime import datetime

DATA_FILE = "logs.json"

##### 데이터 불러오기 & 저장 함수 #####
def load_data():
    """저장된 최신 데이터를 불러옴"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("texts", [])
    return []

def save_data(text):
    """입력된 데이터를 저장"""
    with open(DATA_FILE, "w") as file:
        json.dump({"texts": [text]}, file)

##### 메인 앱 #####
def main():
    st.set_page_config(page_title="최신 텍스트 저장", layout="centered")
    st.title("📌 최신 텍스트 저장")

    # 세션 상태 초기화
    if "latest_text" not in st.session_state:
        stored_texts = load_data()
        st.session_state["latest_text"] = stored_texts[0] if stored_texts else ""

    if "current_text" not in st.session_state:
        st.session_state["current_text"] = ""

    # 입력 필드
    st.text_area("💬 입력할 텍스트", key="current_text", height=100)

    # 저장 버튼
    if st.button("저장"):
        if st.session_state["current_text"].strip():  # 빈 값 방지
            new_entry = {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "text": st.session_state["current_text"]
            }
            st.session_state["latest_text"] = new_entry  # 최신 값 업데이트
            st.session_state["current_text"] = ""  # 입력 필드 초기화
            save_data(new_entry)  # 파일 저장
            st.rerun()

    # 최신 저장된 텍스트 표시
    if st.session_state["latest_text"]:
        st.subheader("📄 최신 저장된 텍스트")
        st.write(f"🕒 {st.session_state['latest_text']['time']}  \n{st.session_state['latest_text']['text']}")

if __name__ == "__main__":
    main()
