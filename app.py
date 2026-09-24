import streamlit as st

# Page Config
st.set_page_config(page_title="AI Video-to-Script Studio", page_icon="🎬", layout="wide")

# Main Title matching the reference style
st.title("AI စာသား ထွက်ယူရန်")
st.write("မည်သည့် ဗီဒီယိုကိုမဆို ထည့်သွင်းပြီး Script တစ်ခုအဖြစ် ပြောင်းလဲလိုက်ပါ။")

# AI Voice Mode / Model Selection Tabs
st.markdown("### ⚡ AI Video-to-Script")
st.write("AI Voice Mode ရွေးချယ်ရန်")

col1, col2 = st.columns(2)
with col1:
    ai_model = st.selectbox("Model", ["AI Script (Gemini)", "AI Script (Microsoft)"], label_visibility="collapsed")

# Warning/Tip note matching the reference interface
st.warning("⚠️ PRO TIP: Gemini Voice mode အတွက် အချက်အလက် သိပ်မပိုသော ဗီဒီယိုများက အဆင်ပြေဆုံး ဖြစ်သည်။")

# File Uploader for Video
uploaded_file = st.file_uploader("📁 ဗီဒီယိုဖိုင်တင်ရန် (Upload video)", type=["mp4", "mov", "avi", "mkv"])

# Language and Audio Options
col_lang, col_type = st.columns(2)
with col_lang:
    language = st.selectbox("Language", ["Burmese (မြန်မာ)", "English", "Thai"])

with col_type:
    transcript_type = st.selectbox("အသံပုံစံ", ["Auto (Detected from video)", "Manual Upload"])

# Action Button
generate_btn = st.button("✍️ Script ထုတ်မည်", use_container_width=True)

# Output Section for Script
st.markdown("---")
st.subheader("📝 ရလဒ် Script")

script_output = st.text_area(
    "ထွက်လာမည့် စာသားများကို ဤနေရာတွင် ပေါ်လာပါမည်။",
    value="သင်တင်လိုက်သော ဗီဒီယိုမှ အသံလမ်းကြောင်းကို (Script) များကို ဤနေရာတွင် ဖော်ပြပေးပါမည်။...",
    height=200
)

# Copy/Action button Below output
st.button("📋 မှတ်စုသို့ ကူးယူမည်")
