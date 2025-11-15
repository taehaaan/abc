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
    st.write(f"🗡️ 플레이어가 몬스터에게 {dmg} 데미지를 줬습니다!")
    monster_turn()

# 플레이어 방어
def defend():
    st.write("🛡️ 플레이어가 방어! 몬스터 데미지 절반")
    monster_turn(defend=True)

# 플레이어 회복
def heal():
    hp = random.randint(3, 7)
    st.session_state.player_hp += hp
    st.write(f"💖 플레이어 HP {hp} 회복!")
    monster_turn()

# 몬스터 공격
def monster_turn(defend=False):
    if st.session_state.monster_hp <= 0:
        return
    dmg = random.randint(3, 6)
    if defend:
        dmg = dmg // 2
    st.session_state.player_hp -= dmg
    st.write(f"👹 몬스터가 플레이어에게 {dmg} 데미지를 줬습니다!")

# 버튼 배치
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⚔️ 공격"):
        attack()
        st.session_state.turn += 1
with col2:
    if st.button("🛡️ 방어"):
        defend()
        st.session_state.turn += 1
with col3:
    if st.button("💖 회복"):
        heal()
        st.session_state.turn += 1

# 승리/패배 체크
if st.session_state.player_hp <= 0:
    st.error("💀 플레이어 패배!")
if st.session_state.monster_hp <= 0:
    st.success("🎉 몬스터 처치! 승리!")

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.player_hp = 30
    st.session_state.monster_hp = 20
    st.session_state.turn = 1
    st.experimental_rerun()
