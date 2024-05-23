import streamlit as st
from PIL import Image

primaryColor="#653f7f"
backgroundColor="#fbf4e6"
secondaryBackgroundColor="#efd9fb"
textColor="#653f7f"
font="serif"

#Tampilan halaman web
st.sidebar.image("logo1.png", use_column_width=True)
st.sidebar.title("Menu")
add_selectbox = st.sidebar.selectbox("Pilih Menu :",("Beranda","Pengertian","Kalkulator","Tentang Sistem"))


if add_selectbox == "Beranda":
    st.header('''
    :violet[Selamat Datang di Web trical 😊]''', divider="rainbow")
    st.image("logo1.png")
    st.subheader("trical adalah singkatan dari titrimetri calculation yang dimana berisi website perhitungan tentang Normalitas, %(b/b), dan %(b/v) yang dibuat untuk membantu dan mempersingkat waktu dalam menghitung pada bidang titrimetri" 
             "yang dimana kami berharap website yang kami buat dapat berguna bagi pemakai. Web ini juga memudahkan anda dalam perhitungan pada mata kuliah Analisis Titrimetri Lhoooo &mdash;\
             🧑🏻‍🔬👩🏻‍🔬")

#Pengertian
if add_selectbox=="Pengertian":
    st.header('''
    :violet[Selamat Datang di Web trical 😊]''', divider="rainbow")
    
    #Pengertian Titrimetri
    st.subheader('''
    :violet[Analisis Titrimetri (Volumetri)]''')
    st.write("Analisis titrimetri (volumetri) adalah analisis berdasarkan pengukuran volume larutan yang diketahui konsentrasinya, untuk menentukan zat/larutan lain yang belum diketahui konsentrasinya.")
    st.image("titrasi.png")

    #Pengertian Normalitas
    st.subheader('''
    :violet[Normalitas]''')
    st.write("Normalitas dapat diartikan sebagai jumlah mol ekuivalen dari suatu zat per liter larutan.",
             "Normalitas adalah ukuran yang menunjukkan konsentrasi pada berat setara dalam gram per liter larutan.", 
             "Berat ekivalen itu sendiri adalah ukuran kapasitas reaktif molekul yang dilarutkan dalam larutan.", 
             "Normalitas dapat disingkat dengan huruf “N”, yang merupakan salah satu opsi paling efektif dan berguna dalam proses laboratorium.")
    st.image("rumus normalitas.png")
    st.markdown('''
                Penjelasan :
                1. mg sampel = Bobot sampel yang ditimbang
                2. FP = Faktor Pengenceran
                3. Vsampel = Volume Titrasi (Buret)
                4. BE = Bobot Ekuivalen
                ''')

    #Pengertian %b/b
    st.subheader('''
    :violet[%(b/b)]''')
    st.write("Persen kadar %(b/b) menyatakan jumlah massa (gram) zat terlarut dalam 100 gram larutan.")
    st.image("rumus persen b-b.png")
    st.markdown('''
                Penjelasan :
                1. V titran = Volume hasil titrasi (Buret)
                2. Normalitas = Hasil perhitungan normalitas dari suatu sampel yang ingin diketahui kadar %(b/b)
                3. BE = Bobot Ekuivalen
                4. gram sampel = Bobot sampel yang ditimbang
                ''')

    #Pengertian %b/v
    st.subheader('''
    :violet[%(b/v)]''')
    st.write("Persen kadar %(b/v) menyatakan jumlah massa (gram) zat terlarut dalam 100 mL larutan.")
    st.image("rumus persen b-v.png")
    st.markdown('''
                Penjelasan :
                1. V titran = Volume hasil titrasi (Buret)
                2. Normalitas = Hasil perhitungan normalitas dari suatu sampel yang ingin diketahui kadar %(b/b)
                3. BE = Bobot Ekuivalen
                4. V titrat = Volume sampel yang dipipet/ada di erlenmeyer
                ''')

    #Pengertian BE
    st.subheader('''
    :violet[Bobot Ekuivalen]''')
    st.write("BE (Bobot Ekuivalen) adalah bobot dalam gram (dari) suatu zat yang diperlukan untuk memberikan atau bereaksi",
             "Bobot Ekuivalen (BE) sering digunakan pada perhitungan Normlitas (N), %(b/b), dan %(b/v)",
             "Bobot Ekuivalen (BE) bisa didapatkan dengan menghitung Mr suatu senyawa yang dicari, maka dari itu kami menyediakan tabel periodik untuk memudahkan pengguna dalam menghitung.")
    st.image("rumus be.png")
    st.markdown('''
                Penjelasan :
                1. Mr = Massa atom relatif
                2. α = Jumlah valensi senyawa atau ion dalam reaksi
                ''')
    st.image("tabel periodik.png")
    st.markdown('''
                Ini adalah beberapa contoh Bobot Ekuivalen (BE) yang sering digunakan dalam perhitungan titrimetri
                |   Nama Senyawa  | Rumus Molekul | Bobot Ekuivalen (mg/mgrek)|
                |-----------------|---------------|---------------------------|
                |   Asam Oksalat  |     H₂C₂O₄    |             63            |
                |      Boraks     | Na₂B₄O₇·10H₂O |            191            |
                |   Asam Asetat   |    CH₃COOH    |             60            |
                | Natrium Karbonat|    Na₂CO₃     |             53            |
                |       Besi      |      Fe       |             56            |
                | Kalium Dikromat |    K₂Cr₂O₇    |             49            |
                |      Klor       |      Cl       |            35,5           |
                ''')

#Kalkulator
elif add_selectbox == "Kalkulator":
    st.header('''
    :violet[Selamat Datang di Web trical 😊]''', divider="rainbow")
    tabs = st.tabs(["1. Normalitas (N)", "2. %(b/b)", "3. %(b/v)", "4. BE"])

#Hitung Normalitas
    with tabs [0] :
        st.subheader("Hitung Normalitas", divider= 'violet')
        mgsampel=st.number_input('Masukkan Nilai mg',format="%.2f",key='mgsampel')
        fp1=st.number_input('Masukkan Nilai fp',format="%.0f",key='fp1')
        vsampel=st.number_input('Masukkan Nilai V Sampel',format="%.2f",key='vsampel')
        be1=st.number_input('Masukkan Nilai BE',format="%.1f",key='be1')
        hitung=st.button('Hitung Normalitas',key='hitung')
        
        if hitung:
            Normalitas=mgsampel/(fp1*vsampel*be1)
            st.success(f"Normalitas sampel={Normalitas:.4f} N")
            st.snow()

#Kalkulator %(b/b)
    with tabs [1] :
        st.subheader(''':violet[Hitung %(b/b)]''')
        Vsampel = st.number_input('Masukkan nilai volume titran (mL)',key='Vsampel')
        Ntitran2 = st.number_input('Masukkan nilai normalitas titran (mgrek/ml)',format='%.4f',key='Ntitran2')
        Bobotekuivalen= st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f",key='BobotEkuivalen')
        FaktorP= st.number_input('Masukkan nilai FP',format="%.0f",key='FaktorP')
        gram = st.number_input('Masukkan nilai gram (g)',format="%.4f",key='gram')
        tombol1 = st.button('Hitung nilai kadarnya',key='tombol1')
        
        if tombol1:
            nilai_kadar = (Vsampel*Ntitran2*Bobotekuivalen*10**-3*FaktorP*100)/gram 
            st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}%(b/v)')
            st.snow()

#Kalkulator %(b/v)
    with tabs [2] :
        st.header(''':violet[Hitung %(b/v)]''')
        Vtitran = st.number_input('Masukkan nilai volume titran (mL)',format='%.2f',key='Vtitran')
        Ntitran = st.number_input('Masukkan nilai normalitas titran (mgrek/ml)',format='%.4f',key='Ntitran')
        Bobotekuivalen1= st.number_input('Masukkan nilai BE (mg/mgrek)',format="%.1f",key='BobotEkuivalen1')
        FaktorP1= st.number_input('Masukkan nilai FP',format="%.0f",key='FaktorP1')
        Vtitrat = st.number_input('Masukkan nilai volume titrat (mL)',format="%.0f",key='Vtitrat')
        tombol2 = st.button('Hitung nilai kadarnya',key='tombol2')
        
        if tombol2:
            nilai_kadar = (Vtitran*Ntitran*Bobotekuivalen1*10**-3*FaktorP1*100)/Vtitrat 
            st.success(f'Persentase kadarnya adalah {nilai_kadar:.2f}%(b/v)')
            st.snow()

#Kalkulator Bobot Ekuivalen (BE)
    with tabs [3] :
        st.subheader(''':violet[Bobot Ekuivalen (BE)]''')
        Mr = st.number_input('Masukkan nilai Mr(mg/mmol)',format='%.2f',key='Mr')
        Valensi = st.number_input('Masukkan nilai valensi',format='%.0f',key='Valensi')
        tombol3 = st.button('Hitung nilai BE',key='tombol3')
        
        if tombol3:
            nilai_BE = (Mr/Valensi)
            st.success(f'Nilai BE adalah {nilai_BE:.2f}')
            st.snow()

#Tentang Sistem
if add_selectbox=="Tentang Sistem":
    st.header('''
    :violet[Selamat Datang di Web trical 😊]''', divider="rainbow")
    st.write('''
    :violet[Biodata Kelompok 8 :]''')
    st.markdown('''
                1. Aina Alqolbi (2360063)
                2. Annisa Nurfitriani (2360073)
                3. Dhona Azzahra (2360107)
                4. Hera Nur Azizah (2360142)
                5. Muhamad Abieb Syah (2360176)
                ''')
    st.write('''
    :violet[Nama Projek :] Perhitungan Normalitas (N), %(b/b), dan %(b/v)''')
    st.write('''
    :violet[Nama Sistem :] trical''')
    st.write('''
    :violet[Penjelasan Sistem :] Web ini dibuat untuk menghitung Normalitas (N), %(b/b), %(b/v), dan BE suatu larutan pada bidang titrimetri''')
    st.markdown('''
                :violet[Sumber :] 
                1. Herawati dan A. Maimulyanti. 2023. PENUNTUN PRAKTIK ANALISIS TITRIMETRI. Bogor : Politeknik AKA Bogor.
                2. Tim BSE. 2013. Teknik Dasar Pekerjaan Laboratorium Kimia 1. Jakarta :  Buku  Sekolah Elektronik (BSE).
                3. Tabel Periodik, url=https://www.pngegg.com/id/png-ogrvo
                ''')
