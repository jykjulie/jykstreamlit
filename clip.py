import streamlit as st
import json
import os

DATA_FILE = "latest_text.json"

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

def main():
    # 세션 상태 초기화 (최초 1회)
    if "latest_text" not in st.session_state:
        st.session_state["latest_text"] = load_latest_text()

    # 입력 필드
    text = st.text_area("", value=st.session_state["latest_text"], height=100)

    # 저장 버튼
    if st.button("저장"):
        if text.strip():  # 빈 값 방지
            st.session_state["latest_text"] = text  # 세션 상태 업데이트
            save_latest_text(text)  # 파일 저장
            st.session_state["latest_text"] = ""  # 저장 후 입력창 초기화

    # 최신 저장된 텍스트 표시
    if st.session_state["latest_text"]:
        st.write(st.session_state["latest_text"])

if __name__ == "__main__":
    main()
