<div align="center">
  
# Implementasi Algoritma Naïve Bayes
*Membangun model klasifikasi Machine Learning menggunakan Python.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=jupyter&logoColor=white)
![Math](https://img.shields.io/badge/Mathematics-00599C?style=for-the-badge&logo=databricks&logoColor=white)

</div>

---

## Informasi Kelompok
* **Kelompok:** 3
* **Anggota Tim:**
 
|    NRP     |      Name      |
| :--------: | :-------------: |
| 5025241044 | Ahmad Loka Arziki |
| 5025241129 | Mochamad Ramadhan Aditya Rachaman |
| 5025241147 | Lucky Himawan Prasetya |
| 5025241216 | Muhammad Daffa Ramadhan |

---

## Applied Concept: Naïve Bayes Algorithm

> **Pertanyaan Utama:** *"Dengan fitur-fitur yang ada, paling mungkin masuk kelas apa?"*

**Bayes' Theorem** menyediakan cara yang berprinsip untuk membalik probabilitas bersyarat (*provides a principled way to reverse conditional probabilities*). Teorema ini didefinisikan sebagai:

$$P(y|X) = \frac{P(X|y) \cdot P(y)}{P(X)}$$

**Keterangan (Where):**
* $P(y|X)$ : *Posterior probability, probability of class $y$ given features $X$*
* $P(X|y)$ : *Likelihood, probability of features $X$ given class $y$*
* $P(y)$ : *Prior probability of class $y$*
* $P(X)$ : *Marginal likelihood or evidence*

### Cara Kerja Algoritma
Algoritma Naive Bayes menggunakan prinsip Teorema Bayes di atas. Kata **"Naive" (Naif)** digunakan karena algoritma ini membuat asumsi kuat: **setiap fitur pada data adalah independen (saling bebas) satu sama lain**. 

Dengan asumsi tersebut, kita cukup menghitung probabilitas (*likelihood*) dari masing-masing fitur secara terpisah terhadap kelas targetnya, lalu mengalikannya. Kelas dengan probabilitas akhir (*posterior*) tertinggi menjadi hasil prediksi.

---

## Dataset: Keputusan Bermain Bola

Kami menggunakan **Dataset Keputusan Bermain Bola**, sebuah dataset klasifikasi kategorikal klasik. Program menggunakan 14 baris data historis ini sebagai basis pengetahuan (*knowledge base*).

<details>
<summary><b>Klik untuk melihat Tabel Data Historis (14 Baris)</b></summary>
<br>

| No | Cuaca | Suhu | Kelembapan | Angin | Target (Main Bola) |
|:--:|:--------|:-------|:-----------|:------|:-------------------|
| 1  | Cerah   | Panas  | Tinggi     | Lemah | **Tidak** |
| 2  | Cerah   | Panas  | Tinggi     | Kuat  | **Tidak** |
| 3  | Mendung | Panas  | Tinggi     | Lemah | **Ya** |
| 4  | Hujan   | Sedang | Tinggi     | Lemah | **Ya** |
| 5  | Hujan   | Dingin | Normal     | Lemah | **Ya** |
| 6  | Hujan   | Dingin | Normal     | Kuat  | **Tidak** |
| 7  | Mendung | Dingin | Normal     | Kuat  | **Ya** |
| 8  | Cerah   | Sedang | Tinggi     | Lemah | **Tidak** |
| 9  | Cerah   | Dingin | Normal     | Lemah | **Ya** |
| 10 | Hujan   | Sedang | Normal     | Lemah | **Ya** |
| 11 | Cerah   | Sedang | Normal     | Kuat  | **Ya** |
| 12 | Mendung | Sedang | Tinggi     | Kuat  | **Ya** |
| 13 | Mendung | Panas  | Normal     | Lemah | **Ya** |
| 14 | Hujan   | Sedang | Tinggi     | Kuat  | **Tidak** |

*Statistik: 9 hari keputusan "Ya", dan 5 hari keputusan "Tidak".*
</details>

---

## Hasil Eksekusi & Evaluasi Prediksi

Program ini tidak menggunakan *train/test split*, melainkan langsung memprediksi kasus uji baru berdasarkan perhitungan probabilitas matematis dari tabel di atas.

**Kasus Uji (Test Case):**
> *Cuaca: **Cerah** | Suhu: **Dingin** | Kelembapan: **Tinggi** | Angin: **Kuat***

### Log Perhitungan Algoritma:
1. **Probabilitas Prior:**
   * $P(Ya) = \frac{9}{14} = 0.6429$
   * $P(Tidak) = \frac{5}{14} = 0.3571$
2. **Probabilitas Likelihood (Gabungan):**
   * *P(Kasus | Ya)* = P(Cerah|Ya) $\cdot$ P(Dingin|Ya) $\cdot$ P(Tinggi|Ya) $\cdot$ P(Kuat|Ya)
   * *P(Kasus | Tidak)* = P(Cerah|Tidak) $\cdot$ P(Dingin|Tidak) $\cdot$ P(Tinggi|Tidak) $\cdot$ P(Kuat|Tidak)
3. **Probabilitas Posterior (Tanpa Normalisasi):**
   * Peluang Akhir **(Ya)** = `0.005291`
   * Peluang Akhir **(Tidak)** = `0.020571`

### Kesimpulan
Berdasarkan perhitungan manual oleh sistem, probabilitas kelas **Tidak** `(0.020571)` lebih besar dari kelas **Ya** `(0.005291)`. Maka, algoritma memprediksi bahwa pada kondisi cuaca tersebut, keputusannya adalah: 
** TIDAK (Batal Bermain Bola)**.
