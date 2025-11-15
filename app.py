import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st

st.title("🎾 Streamlit 바운스볼 (초간단 버전)")

# 초기 상태 설정
if "x" not in st.session_state:
    st.session_state.x = 5
if "y" not in st.session_state:
    st.session_state.y = 3
if "dx" not in st.session_state:
    st.session_state.dx = 1
if "dy" not in st.session_state:
    st.session_state.dy = 1

WIDTH = 20
HEIGHT = 10

# 공 움직이기
def move_ball():
    st.session_state.x += st.session_state.dx
    st.session_state.y += st.session_state.dy

    # 벽에 닿으면 튕기기
    if st.session_state.x <= 0 or st.session_state.x >= WIDTH - 1:
        st.session_state.dx *= -1
    if st.session_state.y <= 0 or st.session_state.y >= HEIGHT - 1:
        st.session_state.dy *= -1


# 맵 그리기
def draw_map():
    for j in range(HEIGHT):
        row = ""
        for i in range(WIDTH):
            if i == st.session_state.x and j == st.session_state.y:
                row += "🔴"
            else:
                row += "⬜"
        st.write(row)


draw_map()

# 버튼: 다음 프레임
if st.button("▶ 다음 프레임"):
    move_ball()
    st.experimental_rerun()

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.x = 5
    st.session_state.y = 3
    st.session_state.dx = 1
    st.session_state.dy = 1
    st.experimental_rerun()
