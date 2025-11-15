import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("⚔️ 간단 턴제 RPG")

# 초기 상태
if "player_hp" not in st.session_state:
    st.session_state.player_hp = 30
if "monster_hp" not in st.session_state:
    st.session_state.monster_hp = 20
if "turn" not in st.session_state:
    st.session_state.turn = 1

st.subheader(f"턴: {st.session_state.turn}")
st.write(f"💖 플레이어 HP: {st.session_state.player_hp}")
st.write(f"👹 몬스터 HP: {st.session_state.monster_hp}")

# 플레이어 공격
def attack():
    dmg = random.randint(4, 8)
    st.session_state.monster_hp -= dmg
    st.write(f"🗡️ 플레이어가
