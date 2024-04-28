import streamlit as st # import library streamlit ke program python
import pandas as pd # import library pandas ke program python untuk manipulasi data
import joblib # import model yg sudah dilatih joblib 
from sklearn.preprocessing import LabelEncoder # iimport LabelEncoder untuk encoding data kategorikal

# load model yg telah dilatih
model = joblib.load("Rendi.joblib")

# load data yang telah dipetakan
mapped_data = pd.read_csv("Transformed Data Set - Sheet1.csv")
# judul aplikasi di halaman web
st.title("Gender Prediction App")
# label encoder untuk setiap kolom data
label_encoders = {}
# iterasi setiap kolom dalam data yg telah dipetakan
for column in mapped_data.columns:
    # inisialisasi objek LabelEncoder
    le = LabelEncoder()
    # enccoding dalam kolom
    mapped_data[column] = le.fit_transform(mapped_data[column])
    # simpan objek LabelEncoder dalam directionary untuk penggunaan berikutnya 
    label_encoders[column] = le


# opsi yang dapat dipilih dalam setiap fitur halaman web sesuai data
color_op = ['Cool', 'Neutral', 'Warm']
music_genre_op = ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic','R&B and soul']
beverage_op = ['Vodka', 'Wine', 'Whiskey',"Doesn't drink",'Beer', 'Other']
soft_drink_op = ['7UP/Sprite', 'Coca Cola/Pepsi','Fanta','Other']

# pemetaan opsi yang dipilih ke nilai numerik setiap fitur
# fitur warna
color_map = {'Cool': 1, 'Neutral': 2, 'Warm': 3}
# fitur genre lagu
music_genre_map = {
    'Rock': 1, 
    'Hip hop': 2, 
    'Folk/Traditional': 3, 
    'Jazz/Blues': 4,
    'Pop': 5,
    'Electronic': 6,
    'R&B and soul': 7,
} 

# fitur minuman
beverage_map = {
    'Vodka' : 1, 
    'Wine' : 2, 
    'Whiskey' : 3,
    "Doesn't drink" : 4,
    'Beer': 5, 
    'Other' : 6
}
soft_drink_map = {
    '7UP/Sprite': 1, 
    'Coca Cola/Pepsi': 2,
    'Fanta': 3,
    'Other' : 4
}


# buat selectbox dropdown untuk setiap fitur di halaman web
favorite_color = st.selectbox('Favorite Color', ['Select']+color_op)
favorite_music_genre = st.selectbox('Favorite Music Genre', ['Select']+music_genre_op)
favorite_beverage = st.selectbox('Favorite Beverage', ['Select']+beverage_op)
favorite_soft_drink = st.selectbox('Favorite Soft Drink', ['Select']+soft_drink_op)

# tambahkan tombol untuk memicu prediksi
if st.button('Predict'):
    # periksa apakah semua fitur telah dipilih
    if favorite_color != 'Select' and favorite_music_genre != 'Select' and favorite_beverage != 'Select' and favorite_soft_drink != 'Select':
        # peta fitur yg dipilih ke nilai numeriknya
        favorite_color_numeric = color_map[favorite_color]
        favorite_music_genre_numeric = music_genre_map[favorite_music_genre]
        favorite_beverage_numeric = beverage_map[favorite_beverage]
        favorite_soft_drink_numeric = soft_drink_map[favorite_soft_drink]

        # prediksi gender berdasarkan nilai numerik yg dipilih
        prediction = model.predict([[favorite_color_numeric, favorite_music_genre_numeric, favorite_beverage_numeric, favorite_soft_drink_numeric]])[0]
        

        # tampilkan hasil prediksi jenis kelamin di halaman web
        st.write(f"Predicted Gender: {prediction}")
    else:
        # pesan tampilan jiba ada fitur yg belum dipilih
        st.write("Please select values for all features.")