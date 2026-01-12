import streamlit as st
import base64

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="FoodGR8",
    page_icon="🍜",
    layout="wide"
)

# ========== LOAD BANNER IMAGE ==========
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

banner_base64 = img_to_base64("assets/banner.png")

# ========== HERO / BANNER ==========
st.markdown(
    f"""
    <style>
    .hero {{
        position: relative;
        height: 320px;
        background-image: url("data:image/png;base64,{banner_base64}");
        background-size: cover;
        background-position: center;
        border-radius: 14px;
        margin-bottom: 2rem;
    }}

    .overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.45);
        border-radius: 14px;
    }}

    .hero-content {{
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
    }}

    .hero-content h1 {{
        font-size: 46px;
        margin-bottom: 8px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
    }}

    .hero-content p {{
        font-size: 20px;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.7);
    }}
    </style>

    <div class="hero">
        <div class="overlay"></div>
        <div class="hero-content">
            <h1>Welcome to FoodGR8 🍜</h1>
            <p>An easy way to detect Vietnamese dishes!</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ========== IMAGE UPLOAD SECTION ==========
st.markdown("## Image Upload 🖼️")

with st.expander("📌 Instructions: Image uploading", expanded=True):
    st.markdown(
        """
        - Upload **PNG / JPG / JPEG** images  
        - Maximum size: **200MB**  
        - The image will be used for food detection (coming soon)
        """
    )

uploaded_file = st.file_uploader(
    "Choose a picture",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.success("✅ Image uploaded successfully")
