import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🐸 길건너 친구들 (긴 길 버전)")

WIDTH = 5
HEIGHT = 10  # 길을 길게 확장

# 세션 초기화
if "player_pos" not in st.session_state:
    st.session_state.player_pos = [2, HEIGHT-1]  # 시작 위치 (맨 아래)
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
                row += "⬜"
        st.write(row)

# 플레이어 이동
def move_player(dx, dy):
    px, py = st.session_state.player_pos
    nx, ny = px + dx, py + dy
    if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
        st.session_state.player_pos = [nx, ny]

# 장애물 이동
def move_obstacles():
    new_obs = []
    for x, y in st.session_state.obstacles:
        ny = y + 1  # 아래로 이동
        if ny < HEIGHT:
            new_obs.append([x, ny])
    # 새 장애물 추가
    if random.random() < 0.5:  # 50% 확률로 새 장애물 생성
        new_obs.append([random.randint(0, WIDTH-1), 0])
    st.session_state.obstacles = new_obs

# 충돌 체크
def check_collision():
    if st.session_state.player_pos in st.session_state.obstacles:
        st.error("💥 친구가 차량에 부딪혔습니다! 게임 오버!")
        st.session_state.player_pos = [2, HEIGHT-1]
        st.session_state.obstacles = []

# 골대 도착 체크
def check_goal():
    if st.session_state.player_pos[1] == 0:
        st.success("🎉 친구가 안전하게 골대에 도착했습니다!")
        st.session_state.player_pos = [2, HEIGHT-1]
        st.session_state.obstacles = []

draw_map()
st.write(f"턴: {st.session_state.turn}")

# 이동 버튼
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️"):
        move_player(-1, 0)
with col2:
    if st.button("⬆️"):
        move_player(0, -1)
    if st.button("⬇️"):
        move_player(0, 1)
with col3:
    if st.button("➡️"):
        move_player(1, 0)

# 턴 진행
move_obstacles()
check_collision()
check_goal()
st.session_state.turn += 1

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.player_pos = [2, HEIGHT-1]
    st.session_state.obstacles = []
    st.session_state.turn = 1
    st.experimental_rerun()
