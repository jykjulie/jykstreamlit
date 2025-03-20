import streamlit as st

# 페이지 설정
st.set_page_config(page_title="텍스트 저장 및 복사", layout="centered")

st.title("텍스트 저장 및 복사")

# 세션 상태 초기화
if "saved_text" not in st.session_state:
    st.session_state.saved_text = ""

# 텍스트 입력
text = st.text_area("텍스트 입력", value=st.session_state.saved_text, height=150)

# 저장 버튼
if st.button("저장"):
    st.session_state.saved_text = text
    st.success("저장되었습니다!")

# 클립보드 복사 버튼 (JavaScript 활용)
copy_button_code = f"""
    <textarea id="copyText" style="position: absolute; left: -9999px;">{st.session_state.saved_text}</textarea>
    <button onclick="copyToClipboard()">복사</button>
    <script>
    function copyToClipboard() {{
        var copyText = document.getElementById("copyText");
        copyText.select();
        document.execCommand("copy");
        alert("클립보드에 복사되었습니다!");
    }}
    </script>
"""

st.markdown(copy_button_code, unsafe_allow_html=True)

# 저장된 텍스트 표시
st.subheader("저장된 텍스트")
st.write(st.session_state.saved_text)
