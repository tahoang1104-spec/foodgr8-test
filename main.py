import streamlit as st
from PIL import Image
import base64

# ========== CONFIG ==========
st.set_page_config(
    page_title="FoodGR8",
    page_icon="🍜",
    layout="wide"
)

# ========== LOAD IMAGE ==========
def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner_base64 = get_base64_image("assets/banner.png")

# ========== HERO SECTION ==========
st.markdown(
    f"""
    <style>
    .hero {{
        background-image: url("data:image/png;base64,{banner_base64}");
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
    }}
    .hero h1 {{
        font-size: 48px;
        margin-bottom: 10px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }}
    .hero p {{
        font-size: 20px;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.6);
    }}
    </style>

    <div class="hero">
        <h1>Welcome to FoodGR8 🍜</h1>
        <p>Nhận diện món ăn Việt Nam từ hình ảnh của bạn</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ========== UPLOAD ==========
uploaded_file = st.file_uploader(
    "📤 Upload ảnh món ăn",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Ảnh gốc")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("🧠 Kết quả")
        st.warning("Chưa gắn model YOLO")
        st.image(image, use_column_width=True)

    st.button("🚀 Detect", use_container_width=True)
else:
    st.info("👆 Upload ảnh để bắt đầu")
