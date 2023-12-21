import streamlit as st
import pandas as pd

st.markdown(
    """
    # Potensi Pasar Air Purifier KeyFresh 

    """)

tab1, tab2, tab3 = st.tabs(["Polusi & Standar", "Beijing - Stasiun Aotizhongxing", "Jincheng - Stasiun Changping"])

with tab1:
    st.header("Polusi Udara & Standar Pengukuran")
    st.image("https://akcdn.detik.net.id/visual/2023/03/22/badai-pasir-menyelimuti-beijing-4_169.jpeg?w=400&q=90")
    st.markdown("""
    Perusahaan KeyEnvi merupakan perusahaan yang bergerak di bidang Air Purifier rumahan dengan nama produk KeyFresh.
    Saat ini, KeyEnvi ingin memperluas bisnisnya di kota Beijing yang datanya diambil dari stasiun Aotizhongxing
    dan kota Jincheng dengan stasiun Changping sebagai pusat pengambilan data.

    1. Bagaimana kondisi pencemaran udara di kota Beijing (Aotizhongxing) dan Jincheng (Changping) dari tahun ke tahun?
    2. Kapankah KeyFresh harus bekerja dengan kondisi paling optimal?
    """)

    st.subheader("Standar Acuan Kualitas Udara")
    st.image("air_po.jpeg")
    st.markdown("""

    Berdasarkan standar yang dipublikasikan dari AQI terdapat beberapa parameter untuk menyatakan kualitas udara di daerah tersebut dalam
    kondisi baik. Hal tersebut dapat dijabarkan dalam 5 parameter yaitu PM2.5, PM10, CO, NO2, and SO2. Kuliatas udara dan
    indeksnya dapat dilihat melalui tabel berikut. Pada analisis kali ini, nilai CO dari dataset yang tersedia 
    tergolong sangat besar sehingga hasilnya tidak akan sesuai dengan standar yang digunakan.
    Maka dari itu, untuk CO akan diabaikan dan mengambil 4 indikator lain."

                """
                )
    st.markdown("""
    #### Rangkuman Analisis
    ##### Bagaimana kondisi pencemaran udara di kota Beijing (Aotizhongxing) dan Jincheng (Changping) dari tahun ke tahun?
    Berdasarkan data yang diperoleh, kualitas udara di Beijing dan Jincheng berada dalam kondisi moderate. Kualitas udara
    tersebut fluktuatif dari tahun ke tahun namun masih dalam batas level yang sama yaitu moderate.

    ##### Kapankah KeyFresh harus bekerja dengan kondisi paling optimal?
    Untuk kualitas udara dari bulan ke bulan, terlihat adanya perbedaan kualitas udara/tingkat pencemaran tiap bulannya
    yang mana hal tersebut ditunjukkan dari grafik by month untuk Aotizhongxing dan Changping. Secara keseluruhan 
    terdapat tren yang sama yang mana sama-sama menunjukkan adanya kualitas udara yang lebih baik di bulan April-September. 
    Sebaliknya untuk bulan Okotber-Maret, terlihat bahwa adanya peningkatan pencemaran udara berdasarkan indikator dari
    PM10 dan PM2.5. Dengan demikian, KeyFresh akan bekerja lebih optimal ketika bulan Oktober-Maret.

    """)

with tab2:
    st.header("Beijing - Stasiun Aotizhongxing")
    st.subheader('Polusi Udara Tahunan Beijing')
    st.image("aot_annual.png")
    st.markdown("""
    Kota Beijing berdasarkan standar AQI dapat dilihat bahwa Changping and Aotizhongxing memiliki nilai rata-rata yang yang
    nilainya di atas standar. Untuk kota Aotizhongxing sendiri memiliki nilai rata-rata dalam kurun waktu 4 tahun
    (2013-2017) PM2.5 adalah 81, PM10 bernilai 109, So2 bernilai 17, dan NO2 bernilai 59.

    Kemudian dilihat dari tren tahunan, polusi udara di kota Beijing fluktuatif. 
    Hal tersebut ditandai dengan naik turunnya PM2.5, PM10, SO2, dan NO2 dari tahun ke tahun. Secara keseluruhan dalam
     4 tahun terkahir, kualitas udara di kota Beijing berada dalam level moderate berdasarkan parameter SO2, dan NO2.

    """)

    st.subheader('Polusi Udara Bulanan Beijing')
    st.image("aot_m.png")
    st.markdown("""
    Untuk tren bulanan, dapat dilihat adanya tren pada bulan-bulan tertentu. Secara keseluruhan kualitas udara di kota
    Beijing berapa pada level moderate, namun memiliki nilai yang berbeda. Bulan April-September memiliki kualitas
    udara yang relatif lebih baik dibandingkan bulan Oktober-Maret. Untuk bulan April-September, nilainya di rentang
    55-75 untuk PM2.5. Tren tersebut juga diikuti dengan parameter lain yang memberikan penguatan terhadap tren tersebut.
    """)

with tab3:
    st.header("Jincheng - Stasiun Changping")
    st.subheader('Polusi Udara Tahunan Jincheng')
    st.image("ch_annual.png")
    st.markdown("""
    Kota Jincheng (Changping) memiliki nilai polusi udara rata-rata dalam kurun 4 tahun (2013-2017) PM2.5 70, PM10
    sebesar 94, SO2 sebesar 15, dan NO2 sebesar 44. Hal tersebut mengindikasikan kuliatas udara di Jincheng berada
    di level moderate. Kemudian dilihat dari tren tahunan, polusi udara di kota Jincheng lebih stabil dan memiliki
    kondisi udara yang lebih bersih walau pada level yang sama. Hal tersebut ditandai dengan cenderung stabilnya
    nilai PM2.5, PM10, SO2, dan NO2.
    """)

    st.image("ch_m.png")
    st.markdown("""
        Untuk tren bulanan, dapat dilihat adanya tren pada bulan-bulan tertentu. Secara keseluruhan kualitas udara
        di kota Jincheng berapa pada level moderate, namun memiliki nilai yang berbeda. Bulan April-September memiliki
        kualitas udara yang relatif lebih baik dibandingkan bulan Oktober-Maret. Untuk bulan April-September, nilainya
        di rentang 46-69 untuk PM2.5. Tren tersebut juga diikuti dengan parameter lain yang memberikan penguatan
        terhadap tren tersebut. Untuk bulan Oktober-Maret sendiri nilai PM2.5 berada pada rentang 76-86. Hal tersebut
        masih berada dalam level moderate dengan nilai yang lebih besar dibandingkan rentang bulan Paril-September yang
        mengindikasikan kualitas udara di rentang bulan tersebut lebih kotor.
        """)



