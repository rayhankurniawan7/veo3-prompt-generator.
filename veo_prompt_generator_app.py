import streamlit as st

st.set_page_config(page_title="Veo 3 Prompt Generator – By MAS JAGO", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f9fafb;
        }
        .big-font {
            font-size: 22px !important;
            font-weight: 600;
        }
        .stTextInput>div>div>input {
            background-color: #fff !important;
            padding: 0.6em;
        }
        .stTextArea>div>div>textarea {
            background-color: #fff !important;
            padding: 0.6em;
        }
        .block-container {
            padding-top: 2rem;
        }
        .custom-button {
            background-color: #10b981;
            color: white;
            border-radius: 0.5rem;
            padding: 0.7rem 1.2rem;
            font-size: 1rem;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Veo 3 Prompt Generator")
st.markdown("#### By MAS JAGO")
st.markdown("Isi setiap kolom untuk membuat prompt **video sinematik** berkualitas tinggi untuk **Veo 3**.")

with st.form("veo_form"):
    st.markdown("### ✏️ Prompt Details")

    col1, col2 = st.columns(2)
    with col1:
        subjek = st.text_input("1. Subjek", placeholder="Contoh: Seorang pemuda skateboarder")
        aksi = st.text_input("2. Aksi", placeholder="Contoh: melompat dari atap ke atap")
        ekspresi = st.text_input("3. Ekspresi", placeholder="Contoh: wajah penuh semangat")
        tempat = st.text_input("4. Tempat", placeholder="Contoh: di jalanan kota cyberpunk")
        waktu = st.selectbox("5. Waktu", ["Pagi", "Siang", "Sore", "Malam", "Fajar", "Senja", "Tengah malam"])

    with col2:
        kamera = st.selectbox("6. Gerakan Kamera", [
            "Kamera mengikut subjek (tracking shot)",
            "Kamera mengelilingi subjek (orbit shot)",
            "Slow zoom in",
            "Drone shot dari atas",
            "Handheld close-up",
            "Panning ke kanan/kiri",
            "Dolly zoom dramatis"
        ])
        pencahayaan = st.selectbox("7. Pencahayaan", [
            "Cahaya matahari alami",
            "Pencahayaan lembut dan redup",
            "Neon terang",
            "Kontras tinggi",
            "Cahaya latar dramatis",
            "Cahaya bulan",
            "Cahaya kuning keemasan senja"
        ])
        gaya = st.selectbox("8. Gaya Video", [
            "Sinematik", "Dokumenter", "Gaya anime", "Gaya retro 80-an",
            "Gaya noir hitam putih", "Gaya fiksi ilmiah futuristik", "Gaya iklan komersial"
        ])
        suasana = st.selectbox("9. Suasana Video", [
            "Emosional dan menyentuh", "Tegang dan penuh aksi", "Lucu dan ringan",
            "Tenang dan damai", "Misterius dan gelap", "Romantis dan hangat"
        ])
        musik = st.text_input("10. Musik atau Suara", placeholder="Contoh: musik piano lembut")
    
    dialog = st.text_input("11. Kalimat yang Diucapkan", placeholder='Contoh: "Aku akan menemukan jawabannya."')
    tambahan = st.text_area("12. Detail Tambahan", placeholder="Contoh: partikel debu beterbangan di udara")

    submitted = st.form_submit_button("🎥 Generate Prompt")

if submitted and subjek and aksi and ekspresi and tempat:
    prompt = f"""**By MAS JAGO**  
{subjek} {aksi} dengan {ekspresi}, {tempat}, saat {waktu.lower()}, dengan {kamera.lower()} dan {pencahayaan.lower()}.  
Gaya video {gaya.lower()}, suasana {suasana.lower()}, dengan latar {musik.lower()}.  
Ia berkata, `{dialog}`  
Tambahkan {tambahan}.
"""
    st.markdown("### ✅ Hasil Prompt:")
    st.code(prompt, language="markdown")

    st.download_button("📥 Unduh Prompt (.txt)", data=prompt, file_name="veo3_prompt_by_mas_jago.txt", mime="text/plain")

    st.markdown("""
        <button onclick="navigator.clipboard.writeText(document.querySelector('code').textContent)"
                style="margin-top:10px; background-color:#0ea5e9; color:white; padding:0.5em 1.2em; border:none; border-radius:8px; cursor:pointer;">
            📋 Salin Prompt ke Clipboard
        </button>
    """, unsafe_allow_html=True)
else:
    if submitted:
        st.warning("❗ Harap isi minimal Subjek, Aksi, Ekspresi, dan Tempat.")
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🎬 Veo 3 Prompt Generator")
col1, col2 = st.columns(2)
with col1:
    st.text_input("Subjek")
with col2:
    st.text_input("Aksi")
st.image("https://link-to-your-logo.png", width=200)
