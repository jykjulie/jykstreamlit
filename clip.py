import streamlit as st
import json
import os

DATA_FILE = "latest_text.json"

# 저장된 텍스트 불러오기
def load_latest_text():
    """저장된 최신 텍스트 불러오기"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data.get("text", "")
    return ""  # 데이터가 없으면 빈 문자열 반환

# 최신 텍스트 저장
def save_latest_text(text):
    """최신 텍스트 저장"""
    with open(DATA_FILE, "w") as file:
        json.dump({"text": text}, file)

def main():
    # 세션 상태 초기화 (최초 1회)
    if "latest_text" not in st.session_state:
        st.session_state["latest_text"] = load_latest_text()
    
    # 텍스트 입력창 (빈 값으로 시작)
    text = st.text_area("", height=100)

    # 저장 버튼
    if st.button("저장"):
        if text.strip():  # 텍스트가 비어있지 않으면 저장
            st.session_state["latest_text"] = text  # 세션 상태 업데이트
            save_latest_text(text)  # 파일에 저장
            st.experimental_rerun()  # 새로고침하여 반영

    # 최신 저장된 텍스트 표시
    if st.session_state["latest_text"]:
        st.write(st.session_state["latest_text"])

if __name__ == "__main__":
    main()
