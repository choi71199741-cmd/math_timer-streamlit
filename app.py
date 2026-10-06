import streamlit as st
import time
from textwrap import dedent

# =========================
# 기본 설정
# =========================

st.set_page_config(
    page_title="내가 바로 수학왕",
    page_icon="👑",
    layout="centered"
)

# =========================
# 세션 상태
# =========================

if "running" not in st.session_state:
    st.session_state.running = False

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0

if "limit" not in st.session_state:
    st.session_state.limit = 300

if "background" not in st.session_state:
    st.session_state.background = True


# =========================
# 전체 디자인
# =========================

if st.session_state.background:

    st.markdown(dedent("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 20%,
                rgba(255,255,255,0.8) 0 2px,
                transparent 3px),
            radial-gradient(circle at 80% 70%,
                rgba(255,255,255,0.7) 0 2px,
                transparent 3px),
            linear-gradient(135deg,
                #dbeafe,
                #ede9fe 50%,
                #fef3c7);

        background-size:
            45px 45px,
            70px 70px,
            100% 100%;
    }

    .stApp::before {
        content:
            "π  ∑  √x  ∫  x²  △  ≈  ∞  f(x)  "
            "a²+b²=c²  90°  %  ÷";

        position: fixed;
        inset: 0;

        width: 100%;
        height: 100%;

        font-size: 28px;
        line-height: 4;
        word-spacing: 25px;

        color: rgba(60,70,100,0.09);

        pointer-events: none;
        z-index: 0;
    }

    .block-container {
        position: relative;
        z-index: 1;
        max-width: 500px;
        padding-top: 35px;
        padding-bottom: 40px;
    }

    </style>
    """), unsafe_allow_html=True)

else:

    st.markdown(dedent("""
    <style>
    .stApp {
        background: #ffffff;
    }

    .block-container {
        max-width: 500px;
        padding-top: 35px;
        padding-bottom: 40px;
    }
    </style>
    """), unsafe_allow_html=True)


# =========================
# 제목
# =========================

st.markdown(dedent("""
<div style="
    text-align:center;
    margin-bottom:25px;
">
    <div style="
        font-size:42px;
        font-weight:900;
    ">
        👑
    </div>

    <div style="
        font-size:30px;
        font-weight:900;
        color:#111827;
    ">
        내가 바로 수학왕
    </div>

    <div style="
        color:#555;
        margin-top:6px;
        font-size:15px;
    ">
        수학 문제 풀이 타이머
    </div>
</div>
"""), unsafe_allow_html=True)


# =========================
# 배경 ON / OFF
# =========================

if st.session_state.background:
    bg_text = "🎨 배경 끄기"
else:
    bg_text = "🎨 배경 켜기"

if st.button(
    bg_text,
    use_container_width=True
):
    st.session_state.background = not st.session_state.background
    st.rerun()


st.write("")


# =========================
# 기준 시간
# =========================

st.markdown(
    "### ⏱️ 기준 시간"
)

col1, col2 = st.columns(2)

with col1:

    if st.session_state.limit == 300:
        button_type = "primary"
    else:
        button_type = "secondary"

    if st.button(
        "5분",
        use_container_width=True,
        type=button_type
    ):

        if not st.session_state.running:

            st.session_state.limit = 300
            st.session_state.elapsed = 0
            st.session_state.start_time = None

            st.rerun()


with col2:

    if st.session_state.limit == 600:
        button_type = "primary"
    else:
        button_type = "secondary"

    if st.button(
        "10분",
        use_container_width=True,
        type=button_type
    ):

        if not st.session_state.running:

            st.session_state.limit = 600
            st.session_state.elapsed = 0
            st.session_state.start_time = None

            st.rerun()


# =========================
# 시간 계산
# =========================

if st.session_state.running:

    st.session_state.elapsed = (
        time.time() - st.session_state.start_time
    )


elapsed = st.session_state.elapsed
limit = st.session_state.limit


# =========================
# 타이머 시간
# =========================

minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

timer_text = f"{minutes:02d}:{seconds:02d}"


# =========================
# 타이머 화면
# =========================

st.markdown(dedent(f"""
<div style="
    background:rgba(255,255,255,0.92);
    border-radius:25px;
    padding:28px 10px;
    margin:25px 0;

    text-align:center;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.10);

    border:1px solid rgba(255,255,255,0.8);
">

    <div style="
        font-size:68px;
        font-weight:900;
        letter-spacing:2px;
        color:#111827;
        line-height:1.1;
    ">
        {timer_text}
    </div>

    <div style="
        font-size:14px;
        color:#777;
        margin-top:8px;
    ">
        기준 시간 : {limit // 60}분
    </div>

</div>
"""), unsafe_allow_html=True)


# =========================
# 기준 시간 상태
# =========================

if elapsed >= limit:

    overtime = elapsed - limit

    over_minutes = int(overtime // 60)
    over_seconds = int(overtime % 60)

    st.error(
        f"🔥 기준시간 초과  +{over_minutes:02d}:{over_seconds:02d}"
    )

else:

    remaining = limit - elapsed

    remaining_minutes = int(remaining // 60)
    remaining_seconds = int(remaining % 60)

    st.info(
        f"남은 기준시간  {remaining_minutes:02d}:{remaining_seconds:02d}"
    )


# =========================
# 컨트롤 버튼
# =========================

st.write("")

col1, col2, col3 = st.columns(3)


# 시작
with col1:

    if st.button(
        "▶️ 시작",
        use_container_width=True,
        type="primary"
    ):

        if not st.session_state.running:

            st.session_state.start_time = (
                time.time() - st.session_state.elapsed
            )

            st.session_state.running = True

            st.rerun()


# 일시정지
with col2:

    if st.button(
        "⏸️ 일시정지",
        use_container_width=True
    ):

        if st.session_state.running:

            st.session_state.elapsed = (
                time.time() - st.session_state.start_time
            )

            st.session_state.running = False

            st.rerun()


# 초기화
with col3:

    if st.button(
        "🔄 초기화",
        use_container_width=True
    ):

        st.session_state.running = False
        st.session_state.start_time = None
        st.session_state.elapsed = 0.0

        st.rerun()


# =========================
# 타이머 자동 업데이트
# =========================

if st.session_state.running:

    time.sleep(0.1)
    st.rerun()
