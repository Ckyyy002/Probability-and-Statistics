import pandas as pd

def main():
    # Dataset Historis
    data = {
        'Cuaca': ['Cerah', 'Cerah', 'Mendung', 'Hujan', 'Hujan', 'Hujan', 'Mendung', 'Cerah', 'Cerah', 'Hujan', 'Cerah', 'Mendung', 'Mendung', 'Hujan'],
        'Suhu': ['Panas', 'Panas', 'Panas', 'Sedang', 'Dingin', 'Dingin', 'Dingin', 'Sedang', 'Dingin', 'Sedang', 'Sedang', 'Sedang', 'Panas', 'Sedang'],
        'Kelembapan': ['Tinggi', 'Tinggi', 'Tinggi', 'Tinggi', 'Normal', 'Normal', 'Normal', 'Tinggi', 'Normal', 'Normal', 'Normal', 'Tinggi', 'Normal', 'Tinggi'],
        'Angin': ['Lemah', 'Kuat', 'Lemah', 'Lemah', 'Lemah', 'Kuat', 'Kuat', 'Lemah', 'Lemah', 'Lemah', 'Kuat', 'Kuat', 'Lemah', 'Kuat'],
        'Main': ['Tidak', 'Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak']
    }
    df = pd.DataFrame(data)
    
    # Kasus Uji
    kasus_uji = {
        'Cuaca': 'Cerah', 
        'Suhu': 'Dingin', 
        'Kelembapan': 'Tinggi', 
        'Angin': 'Kuat'
    }

    print("  SIMULASI PERHITUNGAN NAIVE BAYES")
    print(f"Kasus Uji: {kasus_uji}\n")

    # Probabilitas Prior (Peluang Awal)
    total_data = len(df)
    total_ya = len(df[df['Main'] == 'Ya'])
    total_tidak = len(df[df['Main'] == 'Tidak'])

    prior_ya = total_ya / total_data
    prior_tidak = total_tidak / total_data

    print("LANGKAH 1: Menghitung Probabilitas Prior")
    print(f"- P(Ya) = {total_ya}/{total_data} = {prior_ya:.4f}")
    print(f"- P(Tidak) = {total_tidak}/{total_data} = {prior_tidak:.4f}\n")

    # Probabilitas Likelihood
    print("LANGKAH 2: Menghitung Probabilitas Likelihood")
    prob_likelihood_ya = 1.0
    prob_likelihood_tidak = 1.0

    # Iterasi kasus uji
    for fitur, nilai in kasus_uji.items():
        # Hitung peluang 'Ya'
        count_fitur_ya = len(df[(df[fitur] == nilai) & (df['Main'] == 'Ya')])
        prob_fitur_ya = count_fitur_ya / total_ya
        prob_likelihood_ya *= prob_fitur_ya
        # Hitung peluang 'Tidak'
        count_fitur_tidak = len(df[(df[fitur] == nilai) & (df['Main'] == 'Tidak')])
        prob_fitur_tidak = count_fitur_tidak / total_tidak
        prob_likelihood_tidak *= prob_fitur_tidak
      
        # Print perhitungan 
        print(f"- P({fitur}={nilai} | Ya) = {count_fitur_ya}/{total_ya} = {prob_fitur_ya:.4f}")
        print(f"- P({fitur}={nilai} | Tidak) = {count_fitur_tidak}/{total_tidak} = {prob_fitur_tidak:.4f}")
    print()

    # Probabilitas Posterior
    posterior_ya = prior_ya * prob_likelihood_ya
    posterior_tidak = prior_tidak * prob_likelihood_tidak

    print("LANGKAH 3: Menghitung Probabilitas Posterior (Prior x Likelihood)")
    print(f"- Peluang Akhir (Ya) = {posterior_ya:.6f}")
    print(f"- Peluang Akhir (Tidak) = {posterior_tidak:.6f}\n")

    # Kesimpulan (Prediksi Akhir)
    print("LANGKAH 4: Kesimpulan Prediksi")
    if posterior_ya > posterior_tidak:
        print(f"Nilai {posterior_ya:.6f} > {posterior_tidak:.6f}")
        print("PREDIKSI AKHIR: YA (Main Golf)")
    else:
        print(f"Nilai {posterior_tidak:.6f} > {posterior_ya:.6f}")
        print("PREDIKSI AKHIR: TIDAK (Batal Main)")

if __name__ == "__main__":
    main()
