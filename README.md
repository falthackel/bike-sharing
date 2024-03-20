# Proyek Analisis Data: Bike Sharing Dataset
Nama: Farrel Jonathan Vickeldo
Email: farrel.jonathan.fj@gmail.com
ID Dicoding: falthackel

## Menentukan Pertanyaan Bisnis
- Bagaimana performa peminjaman dalam beberapa bulan terakhir?
- Apa pengaruh lingkungan terhadap peminjaman sepeda?
- Apakah peminjaman sepeda lebih banyak dilakukan oleh orang yang sedang bekerja atau tidak?

## Conclusion
- Performa peminjaman sepeda dalam 2 tahun menunjukkan bahwa Bulan Mei dan Bulan Juli adalah bulan terlaris. Jika dikalkulasikan antara jumlah peminjaman dan durasi peminjaman, Bulan Mei dan Bulan Juli menunjukkan angka yang tertinggi di tahun 2011, namun bukan di tahun 2012.
- Peminjaman terbanyak terjadi pada musim semi dengan rata-rata pada suhu sekitar 10 - 15 (terendah), pada kelembaban sekitar 60, dan pada kecepatan angin sekitar 14 (tertinggi).
- Peminjaman lebih banyak dilakukan oleh orang di hari kerja dibandingkan pada hari libur dengan tren peminjaman pada hari kerja cukup stabil antara jam 5 pagi hingga 12 malam.

## Cara Menjalankan Dashboard
### Setup environment
```
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit altair
```

### Run streamlit app
```
streamlit run bike-sharing.py
```
