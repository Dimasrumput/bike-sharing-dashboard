# Bike Sharing Demand Analysis Dashboard

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis pola penggunaan sistem penyewaan sepeda berdasarkan:

- Pengaruh musim terhadap penggunaan
- Pengaruh hari libur / weekend terhadap demand
- Tren penggunaan dari waktu ke waktu
- Segmentasi tingkat demand (Low, Medium, High)

## Persiapan _Environment_

### 1. Buat Virtual Environment (Opsional tapi Direkomendasikan)

```
python -m venv venv
```

Aktifkan environment:

*Windows*

```
venv\Scripts\activate
```
*Mac / Linux*

```
source venv/bin/activate
```

### 2. Install _Dependencies_

Pastikan anda sudah menginstall library berikut:

```
pip install streamlit pandas matplotlib seaborn numpy
```

Atau jika menggunakan `requirements.txt`:

```
pip install -r requirements.txt
```

## Cara Menjalankan Dashboard

Masuk ke folder `Dashboard`:

```
cd Dashboard
```

Kemudian jalankan Streamlit:

```
streamlit run dashboard.py
```

Setelah itu, dashboard akan otomatis terbuka di browser anda. 
Biasanya berjalan di:

```
Code

http://localhost:8501
```

Jika ingin menghentikan dashboard, tekan:

```
Code

CTRL + C
```

## Author

Nama: Dimas Rumekso Putra, S.Mat

Proyek: Analisis Dataset Bike Sharing 2011-2012

Platform: Streamlit