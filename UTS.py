# Inisialisasi data game
game_list = {"TAKKAN 9": {"harga": 800000},
             "Bensin Impek": {"harga": 400000},
             "Supidarman 2": {"harga": 800000},
             "Mancing Mania": {"harga": 50000},
             "Palorant": {"harga": 75000}}

# Inisialisasi variabel pembeli
total_pembelian = 0
cart = {}  # Menyimpan item yang dibeli

# Inisialisasi variabel voucher diskon
kode_voucher = ["TAUFIKBALSEM10", "BARQIKNALPOT20", "RAFLIEWIBU30"]
diskon_voucher = {"TAUFIKBALSEM10": 0.1, "BARQIKNALPOT20": 0.2, "RAFLIEWIBU30": 0.3}
diskon = 0

# Nama toko
toko_nama = "HokiGaming.store"

# Tampilkan nama toko dan daftar game yang tersedia
print(f"Selamat datang di {toko_nama}\nDaftar Game Tersedia:")
for game, info in game_list.items():
    print(f"{game} - Harga: Rp {info['harga']:,}")

# Input pilihan pembeli
while True:
    print("\nMenu:")
    print("1. Beli Game")
    print("2. Lihat Cart")
    print("3. Checkout")

    try:
        menu_choice = int(input("Pilih menu (1/2/3): "))
        if menu_choice == 1:
            game_choice = input("Masukkan nama game yang ingin dibeli: ")
            if game_choice in game_list:
                qty = int(input("Masukkan jumlah yang ingin dibeli: "))
                if qty > 0:
                    if game_choice in cart:
                        cart[game_choice] += qty
                    else:
                        cart[game_choice] = qty

                    total_pembelian += game_list[game_choice]['harga'] * qty
                    print(f"Berhasil menambahkan {qty} {game_choice} ke keranjang.")
                else:
                    print("Jumlah harus lebih dari 0.")
            else:
                print("Game tidak ditemukan. Silakan masukkan nama game yang valid.")
        elif menu_choice == 2:
            if not cart:
                print("Cart belanja kosong.")
            else:
                print("\nCart Belanja:")
                for item, quantity in cart.items():
                    print(f"{item} - Jumlah: {quantity}")

                total_cart = sum(game_list[item]['harga'] * qty for item, qty in cart.items())
                print(f"Total di Cart: Rp {total_cart:,}")
        elif menu_choice == 3:
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    except ValueError:
        print("Masukkan angka yang valid.")

# Pilihan metode pembayaran
print("\nPilih Metode Pembayaran:")
print("1. Transfer Bank")
print("2. Kartu Kredit")
print("3. E-Wallet")
metode_pembayaran_choice = input("Pilih metode pembayaran (1/2/3): ")

if metode_pembayaran_choice == "1":
    metode_pembayaran = "Transfer Bank"
elif metode_pembayaran_choice == "2":
    metode_pembayaran = "Kartu Kredit"
elif metode_pembayaran_choice == "3":
    metode_pembayaran = "E-Wallet"
else:
    metode_pembayaran = "Metode Pembayaran Tidak Valid"

# Pilihan pengguna untuk menggunakan kode voucher diskon
if total_pembelian > 0:
    gunakan_voucher = input("Apakah Anda memiliki kode voucher diskon? (ya/tidak): ").lower()
    if gunakan_voucher == "ya":
        kode_voucher_input = input("Masukkan kode voucher: ").upper()
        if kode_voucher_input in kode_voucher:
            diskon = diskon_voucher[kode_voucher_input]
            total_pembelian -= total_pembelian * diskon
            print(f"Diskon {int(diskon * 100)}% berhasil diterapkan.")
        else:
            print("Kode voucher tidak valid. Diskon tidak diterapkan.")

# Tampilkan total pembelian dalam format Rupiah dan metode pembayaran
print(f"\nTotal pembelian di {toko_nama}: Rp {total_pembelian:,}")
print(f"Metode Pembayaran: {metode_pembayaran}")
print("Terima kasih telah berbelanja di HokiGaming.store!")