import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🗡️ 검 강화 게임")

# 초기 세션 상태
if "sword_attack" not in st.session_state:
    st.session_state.sword_attack = 5  # 초기 공격력
if "monster_hp" not in st.session_state:
    st.session_state.monster_hp = 20
if "player_hp" not in st.session_state:
    st.session_state.player_hp = 30
if "turn" not in st.session_state:
    st.session_state.turn = 1

# 검 강화 함수
def enhance_sword():
    success_rate = random.randint(1, 100)
    if success_rate <= 70:  # 70% 확률로 강화 성공
        increase = random.randint(2, 5)
        st.session_state._
