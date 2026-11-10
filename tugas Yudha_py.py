# ==========================================
# 1. Mulai Program & Inisialisasi
# ==========================================
print("=========================================")
print("     APLIKASI KASIR RESTORAN BARU        ")
print("=========================================")

# Inisialisasi variabel total belanja awal
total_belanja = 0

# Rincian harga menu disimpan dalam dictionary untuk mempermudah pengecekan
menu_harga = {
    1: ("Nasi Goreng", 25000),
    2: ("Mie Ayam", 15000),
    3: ("Ayam Geprek", 20000),
    4: ("Sate Ayam", 30000),
    5: ("Bakso", 18000)
}

# ==========================================
# 2 & 3. Perulangan Menu & Proses Pemesanan
# ==========================================
while True:
    print("\n--- DAFTAR MENU MAKANAN ---")
    print("1. Nasi Goreng  - Rp 25.000")
    print("2. Mie Ayam     - Rp 15.000")
    print("3. Ayam Geprek  - Rp 20.000")
    print("4. Sate Ayam    - Rp 30.000")
    print("5. Bakso        - Rp 18.000")
    print("0. Selesai Memilih")
    print("---------------------------")
    
    # Input pilihan menu dari pengguna
    pilihan = input("Pilih menu (0-5): ")
    
    # Validasi input agar program tidak error jika pengguna salah ketik huruf
    if not pilihan.isdigit():
        print("Input tidak valid! Masukkan angka 0 sampai 5.")
        continue
        
    pilihan = int(pilihan)
    
    # 4. Apakah Pilihan 0? (Cek Selesai)
    if pilihan == 0:
        break # Keluar dari loop perulangan (while) jika memilih 0
        
    # Pengecekan jika pilihan menu ada di daftar 1-5
    if pilihan in menu_harga:
        nama_makanan = menu_harga[pilihan][0]
        harga_satuan = menu_harga[pilihan][1]
        
        # Input jumlah pesanan
        jumlah_input = input(f"Masukkan jumlah {nama_makanan} yang dibeli: ")
        if not jumlah_input.isdigit():
            print("Jumlah harus berupa angka! Pesanan dibatalkan.")
            continue
            
        jumlah = int(jumlah_input)
        
        if jumlah <= 0:
            print("Jumlah pesanan minimal 1!")
            continue
            
        # Hitung subtotal pesanan dan tambahkan ke total belanja keseluruhan
        subtotal = harga_satuan * jumlah
        total_belanja += subtotal
        print(f"-> Berhasil menambahkan {jumlah} {nama_makanan} (Subtotal: Rp {subtotal:,})")
    else:
        print("Pilihan menu tidak tersedia! Silakan pilih angka 1-5 atau 0.")

# ==========================================
# 5. Proses Hitung Diskon
# ==========================================
# Jika total belanja > Rp200.000, mendapat diskon 20%
if total_belanja > 200000:
    persen_diskon = 20
    potongan_harga = total_belanja * 0.20
else:
    persen_diskon = 0
    potongan_harga = 0

# Hitung total akhir yang harus dibayar
total_bayar = total_belanja - potongan_harga

# ==========================================
# 6. Tampilkan Struk Pembayaran
# ==========================================
print("\n=========================================")
print("           STRUK PEMBAYARAN              ")
print("=========================================")
print(f"Total Belanja : Rp {total_belanja:,}")
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : Rp {potongan_harga:,}")
print("-----------------------------------------")
print(f"Total Bayar   : Rp {total_bayar:,}")
print("=========================================")
print("              Terima Kasih               ")
print("=========================================")