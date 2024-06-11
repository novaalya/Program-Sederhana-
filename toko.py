class Produk:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Toko:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        print("Produk '{}' berhasil ditambahkan.".format(produk.nama))

    def hapus_produk(self, kode_produk):
        for produk in self.daftar_produk:
            if produk.kode == kode_produk:
                self.daftar_produk.remove(produk)
                print("Produk '{}' berhasil dihapus.".format(produk.nama))
                return
        print("Produk dengan kode '{}' tidak ditemukan.".format(kode_produk))

    def tampilkan_daftar_produk(self):
        if not self.daftar_produk:
            print("Tidak ada produk yang tersedia.")
            return
        print("Daftar Produk:")
        for produk in self.daftar_produk:
            print("Kode:", produk.kode)
            print("Nama:", produk.nama)
            print("Harga: Rp", produk.harga)
            print("Stok:", produk.stok)
            print()

def main():
    toko = Toko()

    while True:
        print("\n=== Aplikasi Manajemen Toko ===")
        print("1. Tambah Produk")
        print("2. Hapus Produk")
        print("3. Tampilkan Daftar Produk")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            kode = input("Masukkan kode produk: ")
            nama = input("Masukkan nama produk: ")
            harga = float(input("Masukkan harga produk: "))
            stok = int(input("Masukkan stok produk: "))
            produk_baru = Produk(kode, nama, harga, stok)
            toko.tambah_produk(produk_baru)
        elif pilihan == '2':
            kode = input("Masukkan kode produk yang ingin dihapus: ")
            toko.hapus_produk(kode)
        elif pilihan == '3':
            toko.tampilkan_daftar_produk()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 hingga 4.")

if __name__ == "__main__":
    main()