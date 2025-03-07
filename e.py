import streamlit as st
from datetime import datetime, timedelta
import json
import os

DATA_FILE = "logs.json"

##### 기능 구현 함수 #####
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"e": [], "v": []}

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump({"e": st.session_state["e"], "v": st.session_state["v"]}, file)


##### 메인 함수 #####
def main():
    # 세션 상태 초기화
    if "e" not in st.session_state or "v" not in st.session_state:
        data = load_data()
        st.session_state["e"] = data["e"]
        st.session_state["v"] = data["v"]
    if "et" not in st.session_state:
        st.session_state["et"] = ""
    if "vt" not in st.session_state:
        st.session_state["vt"] = ""
    
    # 현재 시간
    now = datetime.now()
    
    # 버튼 및 입력 필드
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("e"):
            st.session_state["e"].append((now.strftime("%Y-%m-%d %H:%M:%S"), st.session_state["et"]))
            st.session_state["et"] = ""
            save_data()
            st.rerun()
    
    with col2:
        if st.button("v"):
            st.session_state["v"].append((now.strftime("%Y-%m-%d %H:%M:%S"), st.session_state["vt"]))
            st.session_state["vt"] = ""
            save_data()
            st.rerun()
    
    # 탭 생성
    tab1, tab2 = st.tabs(['e', 'v'])
    
    def display_records(records, key):
        if records:
            latest_time = datetime.strptime(records[-1][0], "%Y-%m-%d %H:%M:%S")
            time_diff = now - latest_time
            color = "green" if time_diff < timedelta(hours=24) else "red"
            st.markdown(f"### <span style='color:{color};'>{records[-1][0]}</span>  {records[-1][1]}", unsafe_allow_html=True)
            
            # 삭제 버튼 추가
            if st.button(f"마지막 기록 삭제 ({key})"):
                st.session_state[key].pop()
                save_data()
                st.rerun()
        
    with tab1:
        st.text_input("메모", key="et")
        display_records(st.session_state["e"], "e")
        for time, note in st.session_state["e"][::-1]:
            st.write(f"{time} {note}")
    
    with tab2:
        st.text_input("메모", key="vt")
        display_records(st.session_state["v"], "v")
        for time, note in st.session_state["v"][::-1]:
            st.write(f"{time} {note}")

if __name__ == "__main__":
    main()
