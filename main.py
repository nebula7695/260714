import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 포켓몬 직업 추천기", page_icon="⚡")

# MBTI별 데이터 (직업, 포켓몬 이름, 설명, 이미지 URL)
mbti_data = {
    "ISTJ": {
        "job": "회계사 / 데이터 분석가",
        "pokemon": "메타그로스",
        "desc": "책임감이 강하고 현실적이며 꼼꼼합니다. 4개의 뇌로 슈퍼컴퓨터급 연산 능력을 자랑하는 메타그로스처럼 정확하고 논리적인 업무에 탁월합니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png"
    },
    "ISFJ": {
        "job": "간호사 / 사회복지사",
        "pokemon": "럭키",
        "desc": "따뜻하고 헌신적이며 타인을 돕는 것을 좋아합니다. 다친 포켓몬이나 사람에게 영양 만점의 알을 나누어주는 럭키와 완벽하게 어울립니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/113.png"
    },
    "INFJ": {
        "job": "심리 상담가 / 작가",
        "pokemon": "가디안",
        "desc": "통찰력이 뛰어나고 타인의 감정을 잘 읽어냅니다. 트레이너의 마음을 읽고 헌신적으로 지켜주는 가디안처럼 깊은 공감 능력을 가졌습니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"
    },
    "INTJ": {
        "job": "전략 기획자 / 건축가",
        "pokemon": "후딘",
        "desc": "분석적이고 전략적이며 독립적인 사고를 합니다. IQ 5000을 자랑하며 모든 것을 기억하고 계산하는 후딘과 같은 완벽한 전략가입니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"
    },
    "ISTP": {
        "job": "엔지니어 / 파일럿",
        "pokemon": "로토무",
        "desc": "도구를 다루는 데 능숙하고 문제 해결 능력이 뛰어납니다. 다양한 가전제품에 들어가 형태를 바꾸며 활약하는 로토무처럼 기계와 친숙합니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/479.png"
    },
    "ISFP": {
        "job": "예술가 / 디자이너",
        "pokemon": "루브도",
        "desc": "감수성이 풍부하고 예술적인 감각이 뛰어납니다. 꼬리에서 나오는 분비물로 자신만의 그림을 그리는 루브도처럼 창의적입니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/235.png"
    },
    "INFP": {
        "job": "심리치료사 / 동화작가",
        "pokemon": "토게키스",
        "desc": "이상주의자이며 따뜻하고 평화를 사랑합니다. 다툼이 없는 평화로운 곳에 나타나 은혜를 베푸는 토게키스와 같은 긍정적인 에너지를 줍니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png"
    },
    "INTP": {
        "job": "프로그래머 / 연구원",
        "pokemon": "폴리곤",
        "desc": "호기심이 많고 지적이며 복잡한 문제를 탐구하는 것을 즐깁니다. 세계 최초로 프로그래밍을 통해 인공적으로 만들어진 폴리곤과 어울립니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png"
    },
    "ESTP": {
        "job": "사업가 / 운동선수",
        "pokemon": "괴력몬",
        "desc": "활동적이고 순발력이 뛰어나며 스릴을 즐깁니다. 4개의 팔로 어떤 격투기든 소화해내는 근육질의 괴력몬처럼 넘치는 에너지를 가졌습니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png"
    },
    "ESFP": {
        "job": "연예인 / 파티 플래너",
        "pokemon": "로파파",
        "desc": "사교적이고 긍정적이며 분위기 메이커 역할을 합니다. 경쾌한 음악을 들으면 춤을 추며 파워를 내는 로파파처럼 흥이 넘칩니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/272.png"
    },
    "ENFP": {
        "job": "크리에이터 / 홍보 전문가",
        "pokemon": "이브이",
        "desc": "상상력이 풍부하고 열정적이며 가능성이 열려있습니다. 환경에 따라 다양한 모습으로 진화할 수 있는 이브이처럼 무궁무진한 잠재력을 가졌습니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
    },
    "ENTP": {
        "job": "발명가 / 변호사",
        "pokemon": "팬텀",
        "desc": "독창적이고 논쟁을 즐기며 재치가 넘칩니다. 장난치는 것을 좋아하지만 두뇌 회전이 매우 빠른 팬텀처럼 통통 튀는 매력이 있습니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"
    },
    "ESTJ": {
        "job": "경영자 / 프로젝트 매니저",
        "pokemon": "엠페르트",
        "desc": "체계적이고 리더십이 있으며 목표 지향적입니다. 무리를 이끄는 황제펭귄처럼 단호하고 카리스마 있는 리더의 모습을 보여주는 엠페르트와 어울립니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/395.png"
    },
    "ESFJ": {
        "job": "교사 / 인사 담당자",
        "pokemon": "푸크린",
        "desc": "친절하고 협조적이며 사람들과의 조화를 중시합니다. 부드러운 털과 아름다운 목소리로 사람들을 편안하게 해주는 푸크린과 닮았습니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/40.png"
    },
    "ENFJ": {
        "job": "코치 / 교육자",
        "pokemon": "망나뇽",
        "desc": "카리스마 있고 타인의 성장을 돕는 것을 좋아합니다. 다정하고 지능이 높아 바다에 빠진 사람을 구출한다는 망나뇽처럼 든든한 조력자입니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png"
    },
    "ENTJ": {
        "job": "CEO / 경영 컨설턴트",
        "pokemon": "리자몽",
        "desc": "대담하고 결단력이 있으며 장기적인 비전을 제시합니다. 강력한 화력과 압도적인 비행 능력을 자랑하는 리자몽처럼 타고난 지배자입니다.",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
    }
}

# 앱 UI 시작
st.title("🎯 MBTI별 직업 & 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면, 딱 맞는 직업과 찰떡궁합인 포켓몬을 추천해 드립니다!")
st.divider()

# MBTI 선택 드롭다운 (16개 유형 리스트 추출)
mbti_options = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_options)

# 선택된 MBTI에 대한 결과 출력
if selected_mbti:
    info = mbti_data[selected_mbti]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(f"✨ 추천 직업: **{info['job']}**")
        st.write(f"**{selected_mbti}** 유형의 성향:")
        st.write(info['desc'])
        st.subheader(f"🐾 매칭 포켓몬: **{info['pokemon']}**")
        
    with col2:
        # st.image에 URL을 직접 넣으면 Streamlit이 알아서 이미지를 렌더링합니다.
        st.image(info['img'], caption=f"{selected_mbti}와 어울리는 {info['pokemon']}", use_column_width=True)

st.divider()
st.caption("포켓몬 일러스트 출처: [PokeAPI](https://pokeapi.co/)")
