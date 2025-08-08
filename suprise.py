import streamlit as st
import datetime

# Set page configuration
st.set_page_config(page_title="💌 Open When...", layout="centered")

# Messages dictionary
messages = {
    "Open On Your First Day of Training 🩷": """🎯 *Open On Your First Day of Training*

I’m so proud of you. I'm so happy for you, and it's so inspiring to watch you succeed.I’m so proud of you on your very first day of training. This is just the beginning of an amazing journey, and I know you’re going to shine brighter than ever. Remember, every step you take is a step closer to your dreams. I’m cheering for you every moment. — Your Girl 🩷

— Your Girl 🩷""",

    "Open When You Miss Me 🩷": """💌 *Open When You Miss Me*

Hey You,  
Missing me? I’m missing you too — like crazy.  
Imagine I’m hugging you right now.  
Love you more than distance can handle.  
— Your Girl 🩷""",

    "Open When You Can’t Sleep 🩷": """🌙 *Open When You Can’t Sleep*

Can’t sleep?  
Close your eyes and pretend I’m right there, holding your hand.  
Sweet dreams, my night owl.  
— Your Girl 🩷""",

    "Open When You’re Bored 🩷": """😄 *Open When You’re Bored*

Bored already?  
Think about our memories.  
You can always text me too… I never get bored of you.  
— Your Girl 🩷""",

    "Open When You Need to Smile 🩷": """😊 *Open When You Need to Smile*

I miss that cute smile of yours.  
Imagine that I am with you, and you are making fun of me.  
— Your Girl 🩷""",

    "Open When You Feel Alone 🩷": """🫂 *Open When You Feel Alone*

You’re never alone.  
I’m right here — in your heart, your mind, and every beat.  
Just close your eyes and feel my love.  
Always with you.  
— Your Girl 🩷""",

    "Open On Your Last Day of Training 🩷": """🎉 *Open On Your Last Day of Training*

These days without you weren't easy, but knowing you were chasing your dreams made it worth every second.  
I missed you more than I ever thought possible, and I love you more than I can ever explain.  
Thinking about hugging you soon.  
Let’s celebrate when you’re back!  
— Your Girl 🩷"""
}

# Main app UI
st.markdown("<h2 style='text-align: center;'>💌 Open When... </h2>", unsafe_allow_html=True)

# Select and display card
st.markdown("### Select a card:")
selected_card = st.selectbox(
    "Select a card",
    list(messages.keys()),
    key="select_card",
    label_visibility="collapsed"
)

if st.button("📬 Open This Card", key="open_card_btn"):
    st.markdown(messages[selected_card])
    st.markdown("---")
