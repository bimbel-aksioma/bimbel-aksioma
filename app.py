import streamlit as st

# Pengaturan tampilan HP / Mobile Friendly
st.set_page_config(page_title="Bimbel Aksioma", page_icon="📐", layout="centered")

# Desain Header Aplikasi
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>📐 Bimbel Online AKSIOMA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Aplikasi Latihan Soal TKA untuk SD, SMP, dan SMA</p>", unsafe_allow_html=True)
st.markdown("---")

# Navigasi Jenjang Sekolah
jenjang = st.selectbox("🎯 Pilih Jenjang Pendidikan Anda:", ["-- Pilih Jenjang --", "SD (TKA Dasar)", "SMP (TKA Menengah)", "SMA (TKA Lanjut)"])

# Database Soal Contoh Paket 1
database_soal = {
    "SD (TKA Dasar)": {
        "soal": "Sebuah toko buku memberikan diskon 20%. Jika Budi membeli buku seharga Rp150.000, berapa total yang harus dibayar Budi?",
        "pilihan": ["A. Rp120.000", "B. Rp130.000", "C. Rp140.000", "D. Rp110.000"],
        "jawaban": "A",
        "pembahasan": "Diskon = 20% x Rp150.000 = Rp30.000. \n\nTotal Bayar = Rp150.000 - Rp30.000 = Rp120.000."
    },
    "SMP (TKA Menengah)": {
        "soal": "Hasil dari operasi aljabar 3(x + 2) - 2(x - 4) adalah...",
        "pilihan": ["A. x - 2", "B. x + 14", "C. x + 2", "D. 5x + 14"],
        "jawaban": "B",
        "pembahasan": "3(x + 2) - 2(x - 4) = 3x + 6 - 2x + 8 = x + 14."
    },
    "SMA (TKA Lanjut)": {
        "soal": "Jika f(x) = 2x + 3 dan g(x) = x^2 - 1, maka nilai dari fungsi komposisi (g o f)(2) adalah...",
        "pilihan": ["A. 24", "B. 35", "C. 48", "D. 50"],
        "jawaban": "C",
        "pembahasan": "1. Cari f(2) = 2(2) + 3 = 7. \n\n2. Masukkan ke g(x) -> g(7) = 7^2 - 1 = 49 - 1 = 48."
    }
}

if jenjang != "-- Pilih Jenjang --":
    # Memilih Paket (Simulasi 20 Paket)
    paket = st.slider("📁 Pilih Paket Soal (Tersedia Paket 1 - 20):", 1, 20, 1)
    
    st.markdown(f"### 📝 {jenjang} - Paket {paket}")
    
    if paket == 1:
        konten = database_soal[jenjang]
        st.info(konten["soal"])
        
        # Pilihan Jawaban
        pilihan_user = st.radio("Pilih Jawaban Terbaik Anda:", konten["pilihan"])
        
        # Tombol Aksi
        if st.button("Kirim Jawaban & Lihat Pembahasan", use_container_width=True):
            user_letter = pilihan_user[0] # Mengambil huruf depan A, B, C, atau D
            
            if user_letter == konten["jawaban"]:
                st.success("🎉 Luar Biasa! Jawaban Anda BENAR.")
            else:
                st.error(f"❌ Sayang sekali, jawaban kurang tepat. Jawaban benar adalah: {konten['jawaban']}")
            
            # Menampilkan Pembahasan
            st.markdown("#### 📖 Pembahasan Soal:")
            st.help(konten["pembahasan"])
    else:
        st.warning(f"Paket {paket} sedang dalam proses pengisian data soal oleh Admin Aksioma.")
else:
    st.markdown("<p style='text-align: center; color: gray;'>Silakan pilih jenjang sekolah di atas untuk mulai berlatih dari HP.</p>", unsafe_allow_html=True)
