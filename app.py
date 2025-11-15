import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🏰 초간단 타워디펜스 (턴 기반)")

# 초기 세션 상태 설정
if "enemy_pos" not in st.session_state:
    st.session_state.enemy_pos = 0  # x 좌표
if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 5
if "turn" not in st.session_state:
    st.session_state.turn = 1

TOWER_X, TOWER_Y = 2, 2  # 고정 포탑 위치


# 맵 그리기 함수
def draw_map():
    grid = [["⬜" for _ in range(5)] for _ in range(5)]
    
    # 탑 위치
    grid[TOWER_Y][TOWER_X] = "🔫"

    # 적 위치
    if st.session_state.enemy_hp > 0 and st.session_state.enemy_pos < 5:
        grid[2][st.session_state.enemy_pos] = "●"

    # 출력
    for row in grid:
        st.write(" ".join(row))


st.subheader(f"턴: {st.session_state.turn}")
draw_map()

# 다음 턴 버튼
if st.button("▶ 다음 턴"):
    st.session_state.turn += 1

    # 1) 적 이동
    if st.session_state.enemy_hp > 0:
        st.session_state.enemy_pos += 1

    # 2) 포탑 공격 (같은 Y줄이면 공격)
    if st.session_state.enemy_hp > 0 and st.session_state.enemy_pos < 5:
        if 2 == 2:  # 같은 행
            st.session_state.enemy_hp -= 2
