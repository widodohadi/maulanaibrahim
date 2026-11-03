import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Maulana Ibrahim - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #555555;
        margin-bottom: 20px;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar untuk Navigasi & Kontak
with st.sidebar:
    st.image("foto.jpg", caption="Maulana Ibrahim", use_container_width=True)
    st.title("Maulana Ibrahim")
    st.write("💻 *Developer & Tech Enthusiast*")
    st.markdown("---")
    
    st.subheader("📬 Kontak & Sosial Media")
    st.markdown("[🔗 GitHub](https://github.com/widodohadi)")
    st.markdown("[💼 LinkedIn](https://linkedin.com)")
    st.markdown("📧 Email: maulana@example.com")
    
    st.markdown("---")
    menu = st.radio("Navigasi", ["Tentang Saya", "Proyek", "Keahlian", "Hubungi Saya"])

# Halaman 1: Tentang Saya
if menu == "Tentang Saya":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<p class="main-title">Halo, Saya Maulana Ibrahim 👋</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-title">Selamat datang di portofolio digital saya!</p>', unsafe_allow_html=True)
        st.write("""
            Saya adalah seorang pengembang yang memiliki ketertarikan besar dalam dunia teknologi, 
            pemrograman, dan eksplorasi alam. Website ini dibangun menggunakan **Streamlit** 
            sebagai wadah untuk memamerkan proyek, keahlian, dan perjalanan karier saya.
        """)
        st.info("💡 *“Terus belajar, berkarya, dan menjelajah batas kemampuan.”*")
        
    with col2:
        st.image("foto.jpg", use_container_width=True)

# Halaman 2: Proyek
elif menu == "Proyek":
    st.markdown("## 🚀 Proyek Unggulan")
    st.write("Berikut adalah beberapa proyek menarik yang pernah saya kerjakan:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("### 📊 Dashboard Analisis Data")
            st.write("Aplikasi web interaktif untuk visualisasi dan analisis data menggunakan Python, Pandas, dan Streamlit.")
            st.button("Lihat Detail Proyek 1", key="p1")
            
    with col2:
        with st.container():
            st.markdown("### 🤖 Web App Machine Learning")
            st.write("Model prediksi cerdas yang dikemas dengan antarmuka web yang ramah pengguna.")
            st.button("Lihat Detail Proyek 2", key="p2")

# Halaman 3: Keahlian
elif menu == "Keahlian":
    st.markdown("## 🛠️ Keahlian & Teknologi")
    st.write("Beberapa teknologi dan bahasa pemrograman yang biasa saya gunakan:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
    	st.markdown("### Bahasa")
    	st.write("- Python\n- HTML / CSS\n- SQL")
    
    with col2:
    	st.markdown("### Framework")
    	st.write("- Streamlit\n- Flask / FastAPI\n- Pandas / NumPy")
    
    with col3:
    	st.markdown("### Tools")
    	st.write("- Git & GitHub\n- VS Code\n- Streamlit Cloud")

# Halaman 4: Hubungi Saya
elif menu == "Hubungi Saya":
    st.markdown("## 📬 Kirim Pesan")
    st.write("Punya pertanyaan atau ingin berkolaborasi? Jangan ragu untuk mengisi formulir di bawah ini:")
    
    with st.form("contact_form"):
        name = st.text_input("Nama Anda")
        email = st.text_input("Email Anda")
        message =
