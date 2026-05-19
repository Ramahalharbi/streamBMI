import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Sora', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        letter-spacing: -1px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }

    .card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
    }

    .bmi-result-box {
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.2), rgba(96, 165, 250, 0.2));
        border: 1px solid rgba(167, 139, 250, 0.4);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        margin: 1.5rem 0;
    }

    .bmi-number {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
    }

    .bmi-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0.5rem;
    }

    .category-badge {
        display: inline-block;
        padding: 0.4rem 1.2rem;
        border-radius: 999px;
        font-size: 1rem;
        font-weight: 600;
        margin-top: 0.8rem;
    }

    .underweight { background: rgba(251, 191, 36, 0.2); color: #fbbf24; border: 1px solid #fbbf24; }
    .normal      { background: rgba(52, 211, 153, 0.2); color: #34d399; border: 1px solid #34d399; }
    .overweight  { background: rgba(251, 146, 60, 0.2); color: #fb923c; border: 1px solid #fb923c; }
    .obese       { background: rgba(248, 113, 113, 0.2); color: #f87171; border: 1px solid #f87171; }

    .category-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.75rem;
        margin-top: 1.5rem;
    }

    .cat-item {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-size: 0.85rem;
        color: #cbd5e1;
    }

    .cat-item span {
        font-weight: 600;
        font-size: 0.9rem;
    }

    .section-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #64748b;
        margin-bottom: 0.4rem;
        margin-top: 1.2rem;
    }

    div[data-testid="stNumberInput"] input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-family: 'Sora', sans-serif !important;
    }

    div[data-testid="stNumberInput"] input:focus {
        border-color: #a78bfa !important;
        box-shadow: 0 0 0 3px rgba(167,139,250,0.2) !important;
    }

    div[data-testid="stNumberInput"] label {
        color: #94a3b8 !important;
        font-size: 0.8rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.85rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        font-family: 'Sora', sans-serif !important;
        letter-spacing: 0.5px !important;
        margin-top: 1rem !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.5) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title"> BMI Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Body Mass Index · Health Screening Tool</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=0.0, step=0.5, format="%.2f")
with col2:
    height = st.number_input("Height (m)", min_value=0.0, max_value=3.0, value=0.0, step=0.01, format="%.2f")

calculate = st.button("Calculate BMI")

if calculate:
    if height <= 0 or weight <= 0:
        st.error("⚠️ Please enter valid weight and height values greater than zero.")
    else:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            cat_class = "underweight"
            cat_label = "Underweight"
            cat_emoji = "🟡"
            advice = "Consider consulting a nutritionist to reach a healthy weight range."
        elif bmi < 25:
            cat_class = "normal"
            cat_label = "Normal Weight"
            cat_emoji = "🟢"
            advice = "Great job! Maintain your healthy lifestyle with balanced diet and exercise."
        elif bmi < 30:
            cat_class = "overweight"
            cat_label = "Overweight"
            cat_emoji = "🟠"
            advice = "Small changes in diet and activity can make a big difference."
        else:
            cat_class = "obese"
            cat_label = "Obese"
            cat_emoji = "🔴"
            advice = "Please consult a healthcare professional for a personalized plan."

        st.markdown(f"""
        <div class="bmi-result-box">
            <div class="bmi-label">Your BMI Score</div>
            <div class="bmi-number">{bmi:.1f}</div>
            <div>
                <span class="category-badge {cat_class}">{cat_emoji} {cat_label}</span>
            </div>
            <p style="color:#94a3b8; font-size:0.85rem; margin-top:1rem; margin-bottom:0;">{advice}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="margin-top: 1.5rem;">
    <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:2px; color:#64748b; margin-bottom:0.8rem;">BMI Categories</div>
    <div class="category-grid">
        <div class="cat-item">🟡 <span>Underweight</span><br>&lt; 18.5</div>
        <div class="cat-item">🟢 <span>Normal</span><br>18.5 – 24.9</div>
        <div class="cat-item">🟠 <span>Overweight</span><br>25 – 29.9</div>
        <div class="cat-item">🔴 <span>Obese</span><br>≥ 30</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)