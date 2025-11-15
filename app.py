import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("⚽ Streamlit 2D 축구 게임")

WIDTH = 5
HEIGHT = 5

# 초기 세션 상태
if "player" not in st.session_state:
    st.session_state.player = [2, 4]  # x, y
if "ball" not in st.session_state:
    st.session_state.ball = [2, 3]
if "opponent" not in st.session_state:
    st.session_state.opponent = [2, 1]
if "turn" not in st.session_state:
    st.session_state.turn = 1

GOAL_Y = 0

# 맵 그리기
def draw_field():
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if [x, y] == st.session_state.player:
                row += "🙂"
            elif [x, y] == st.session_state.opponent:
                row += "🟥"
            elif [x, y] == st.session_state.ball:
                row += "⚽"
            elif y == GOAL_Y:
                row += "🏁"
            else:
                row += "⬜"
        st.write(row)

# 플레이어 이동
def move_player(dx, dy):
    px, py = st.session_state.player
    nx, ny = px + dx, py + dy
    if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
        st.session_state.player = [nx, ny]
        # 공 이동
        if st.session_state.player == st.session_state.ball:
            bx, by = st.session_state.ball
            st.session_state.ball = [nx, ny-1 if ny>0 else 0]

# 상대 이동 (간단 AI)
def move_opponent():
    ox, oy = st.session_state.opponent
    bx, by = st.session_state.ball
    if ox < bx:
        ox += 1
    elif ox > bx:
        ox -= 1
    if oy < by:
        oy += 1
    elif oy > by:
        oy -= 1
    st.session_state.opponent = [ox, oy]

# 승리 체크
def check_goal():
    if st.session_state.ball[1] == GOAL_Y:
        st.success("🎉 골! 승리!")
        st.session_state.ball = [2, 3]
        st.session_state.player = [2, 4]
        st.session_state.opponent = [2, 1]

draw_field()
st.write(f"턴: {st.session_state.turn}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️"):
        move_player(-1,0)
with col2:
    if st.button("⬆️"):
        move_player(0,-1)
    if st.button("⬇️"):
        move_player(0,1)
with col3:
    if st.button("➡️"):
        move_player(1,0)

# 상대 이동 후 턴 증가
move_opponent()
st.session_state.turn += 1

check_goal()

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.player = [2,4]
    st.session_state.ball = [2,3]
    st.session_state.opponent = [2,1]
    st.session_state.turn = 1
    st.experimental_rerun()
