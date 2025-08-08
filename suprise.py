import streamlit as st

# Page settings
st.set_page_config(page_title="💌 Open When...", layout="centered")

# Custom CSS for romantic look
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffe6f0, #ffd6f5);
        color: #4a0033;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h2 {
        text-align: center;
        color: #d63384;
    }
    .stSelectbox label {
        font-size: 1.1rem;
        color: #ff4d94;
    }
    .stButton>button {
        background-color: #ff66a3;
        color: white;
        border-radius: 12px;
        padding: 0.5rem 1rem;
        font-size: 1.1rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e60073;
    }
    </style>
""", unsafe_allow_html=True)

# Messages
messages = {
    "Open On Your First Day of Training 🩷": """🎯 *Open On Your First Day of Training*

I’m so proud of you...  
Remember, every step you take is a step closer to your dreams.  
— Your Girl 🩷""",

    "Open When You Miss Me 🩷": """💌 *Open When You Miss Me*

Missing me? I’m missing you too — like crazy.  
Imagine I’m hugging you right now.  
— Your Girl 🩷""",

    "Open When You Can’t Sleep 🩷": """🌙 *Open When You Can’t Sleep*

Close your eyes and pretend I’m right there, holding your hand.  
Sweet dreams, my night owl.  
— Your Girl 🩷""",

    "Open When You’re Bored 🩷": """😄 *Open When You’re Bored*

Think about our memories...  
You can always text me too.  
— Your Girl 🩷""",

    "Open When You Need to Smile 🩷": """😊 *Open When You Need to Smile*

I miss that cute smile of yours.  
Imagine that I am with you.  
— Your Girl 🩷""",

    "Open When You Feel Alone 🩷": """🫂 *Open When You Feel Alone*

You’re never alone.  
I’m right here — in your heart, your mind, and every beat.  
— Your Girl 🩷""",

    "Open On Your Last Day of Training 🩷": """🎉 *Open On Your Last Day of Training*

These days without you weren't easy...  
Let’s celebrate when you’re back!  
— Your Girl 🩷"""
}

# Title
st.markdown("<h2>💌 Open When... </h2>", unsafe_allow_html=True)

# Card selector
selected_card = st.selectbox("Pick a card to open:", list(messages.keys()))

# Open button
if st.button("📬 Open This Card"):
    st.markdown(messages[selected_card])
    st.markdown("❤ " * 20)
