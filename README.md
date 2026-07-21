# 👟 Sistem Cerdas Klasifikasi Brand Sepatu

Proyek ini adalah aplikasi berbasis web untuk mengklasifikasikan merek sepatu (**Adidas, Converse, dan Nike**) menggunakan Deep Learning. Model dibangun dengan arsitektur **VGG16** (Transfer Learning) dan antarmuka web dibangun menggunakan **Flask** serta **Bootstrap** dengan penyesuaian palet warna khusus.

Proyek ini dikembangkan sebagai bagian dari tugas akademik di program studi Teknik Informatika, Universitas Bale Bandung.

## 🌟 Fitur Utama
- **Klasifikasi Akurat:** Menggunakan model pra-latih VGG16 dari TensorFlow/Keras untuk mengekstrak fitur gambar secara maksimal.
- **Antarmuka Pengguna Modern:** Didesain dengan Bootstrap 5 dan *custom* CSS yang estetik dan nyaman di mata (perpaduan warna Ivory, Steel Blue, dan Soft Yellow).
- **Prediksi Real-time:** Menampilkan kelas prediksi beserta tingkat probabilitas / keyakinan (*confidence*) secara langsung setelah gambar diunggah.

## 🛠️ Teknologi yang Digunakan
- **Backend:** Python, Flask, Werkzeug
- **Machine Learning:** TensorFlow, Keras, NumPy, Pillow
- **Frontend:** HTML5, Bootstrap 5, CSS

## 📂 Struktur Direktori
```text
T11_VGG16/
│
├── data/                   # (Diabaikan di Git) Berisi folder train/ dan test/
├── static/
│   └── uploads/            # Tempat menyimpan sementara gambar yang diunggah
├── templates/
│   └── index.html          # Antarmuka web utama
├── train_model.py          # Script pelatihan model VGG16
├── app.py                  # Script backend Flask
├── requirements.txt        # Daftar library python
└── README.md               # Dokumentasi proyek
```

## 🚀 Cara Instalasi & Menjalankan Aplikasi

### 1. Clone Repositori
```bash
git clone <URL_GITHUB_KAMU>
cd <NAMA_FOLDER_CLONE>
```

### 2. Install Dependensi
Sangat disarankan untuk membuat *Virtual Environment* terlebih dahulu. Kemudian, jalankan:
```bash
pip install -r requirements.txt
```

### 3. Persiapan Model & Dataset (Penting!)
Karena keterbatasan ukuran file di GitHub (maksimal 100MB), file model (`.h5`) dan dataset gambar asli **tidak disertakan** dalam repositori ini. Anda memiliki dua opsi untuk dapat menjalankan aplikasi:

**Opsi A: Mengunduh Model Siap Pakai (Disarankan)**
Unduh file `model_sepatu_vgg16.h5` melalui tautan berikut:
👉 **[Tautan Google Drive Anda - Masukkan Link di Sini]**
Tempatkan file tersebut di direktori utama proyek (sejajar dengan `app.py`).

**Opsi B: Melatih Ulang Model**
Jika Anda ingin melatih model dari awal:
1. Siapkan dataset dan letakkan di dalam folder `data/train/` dan `data/test/` yang masing-masing berisi sub-folder kelas `adidas`, `converse`, dan `nike`.
2. Jalankan perintah pelatihan di terminal:
   ```bash
   python train_model.py
   ```
   Tunggu hingga proses selesai. Script akan menghasilkan file `model_sepatu_vgg16.h5` secara otomatis.

### 4. Jalankan Aplikasi Web
Setelah model `.h5` tersedia, jalankan server Flask dengan perintah:
```bash
python app.py
```
Buka *browser* Anda dan kunjungi alamat: **http://127.0.0.1:5000**

## 👥 Pengembang
Dikembangkan untuk memenuhi tugas 11 praktikum Kecerdasan Buatan