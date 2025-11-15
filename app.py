import streamlit as st

st.title("Hello Streamlit!")
st.write("이것은 가장 기본적인 Streamlit 예제입니다.")

import streamlit as st
import random

st.title("🗡️ 검 강화 게임")

# 초기 상태
if "sword_attack" not in st.session_state:
    st.session_state.sword_attack = 5  # 초기 공격력
if "monster_hp" not in st.session_state:
    st.session_state.monster_hp = 20
if "turn" not in st.session_state:
    st.session_state.turn = 1

# 검 강화 함수
def enhance_sword():
    success_rate = random.randint(1, 100)
    if success_rate <= 70:  # 70% 확률로 강화 성공
        increase = random.randint(2, 5)
        st.session_state.sword_attack += increase
        st.write(f"🗡️ 검 강화 성공! 공격력이 {increase} 증가하여 {st.session_state.sword_attack}이 되었습니다!")
    else:
        st.write("💥 검 강화 실패! 공격력은 변하지 않았습니다.")

# 몬스터 자동 전투
def monster_turn():
    damage = random.randint(st.session_state.sword_attack - 2, st.session_state.sword_attack + 2)
    st.session_state.monster_hp -= damage
    st.write(f"🗡️ 플레이어가 몬스터에게 {damage} 데미지를 주었습니다!")

# 버튼
if st.button("⚒️ 검 강화"):
    enhance_sword()
    st.session_state.turn += 1

monster_turn()  # 매 턴마다 몬스터 체력 감소

# 상태 출력
st.subheader(f"턴: {st.session_state.turn}")
st.write(f"🗡️ 검 공격력: {st.session_state.sword_attack}")
st.write(f"👹 몬스터 HP: {st.session_state.monster_hp}")

# 승리/패배 체크
if st.session_state.monster_hp <= 0:
    st.success("🎉 몬스터 처치! 승리!")
if st.session_state.sword_attack >= 50:  # 검 강화 최대값
    st.write("⚔️ 검이 너무 강해져서 더 이상 강화할 수 없습니다!")

# 리셋 버튼
if st.button("🔄 리셋"):
    st.session_state.sword_attack = 5
    st.session_state.monster_hp = 20
    st.session_state.turn = 1
    st.experimental_rerun()
