import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🐸 길건너 친구들")

WIDTH = 5
HEIGHT = 5

# 세션 초기화
if "player_pos" not in st.session_state:
    st.session_state.player_pos = [2, 4]  # 시작 위치 (x, y)
if "obstacles" not in st.session_state:
    st.session_state.obstacles = []  # 장애물 위치
if "turn" not in st.session_state:
    st.session_state.turn = 1

# 맵 그리기
def draw_map():
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if [x, y] == st.session_state.player_pos:
                row += "🧑"
            elif [x, y] in st.session_state.obstacles:
                row += "🚗"
            elif y == 0:
                row += "🏁"  # 골대
            else:
