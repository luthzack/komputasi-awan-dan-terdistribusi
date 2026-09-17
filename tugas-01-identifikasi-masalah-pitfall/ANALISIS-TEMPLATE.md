# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Naufal Luthfi Muzakki | [103072400137] | [1] |
| Nur Ro'yul Amin | [103072400159] | [2] |

## Pitfall 1: [Sudah pasti jaringan tidak selalu ada] — ditulis oleh [Luthfi]

**Bukti di skenario:** "`# network is always reliable"

**Kenapa ini keliru:** penjelasan: karena pada jaringan yang trsidtribusi sangat tidak mungkin bahwa jaringan akan selalu ada, pasti akan terdapat paket loss dalam bentuk apapun itu bisa jadi kneksi tiba tiba hilang atau yang lainnya 

**Dampak ke FoodGo:** dampkanya pada saat terdapat transaksi dengan pelanggan akan terjadi gannguan jaringan yang berakibat kegagalan dalam transakasi, yang dimana misal pelanggan refresh atau retry akan berhasil dan sumber masalahnya hanya karena jaringan

**Solusi desain awal:** kasih tombol refresh dan pop up pembayaran gagal untuk mencegah semungkinan pelanggan gagal payout tapi ternyata di foodgo malah udah masuk 

**Trade-off:** resikonya tagihannya bisa jadi double

---

## Pitfall 2: [Latency is Zero] — ditulis oleh [Ro'yul]

**Bukti di skenario:** "tidak ada *timeout* sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)"

**Kenapa ini keliru:** penjelasan: Karena anggapan "tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)" ini seperti kita tidak perlu menerapkan timeout pada proses pemanggilan modul pembayaran dan hasil komputasi/proses dari modul ini bisa didapat secara zero ms paadahal hal seperti itu tidak mungkin, modul pembayaran pada FoodGo tentu memerlukan waktu untuk memproses hasil komputasinya. Ketika banyak modul pesanan yang memanggil modul pembayaran maka akan memakan banyak waktu ditambah tidak ada timeout yang bisa menyebabkan modul pesanan menunggu jawaban tanpa batas waktu.

**Dampak ke FoodGo:** Saat trafik naik(Misal jam makan siang atau saat ada promo besar) akan ada banyak pesanan masuk otomatis modul pesanan akan memanggil modul pembayaran dengan jumlah yang banyak (requestnya), karena tidak ada timeout pada proses pemanggilan antar kedua service ini maka beban ke server akan terus meningkat hingga server tidak mampu menangani pesanan baru (yang melebihi kapasitas resource server) sehingga terjadi gejala seperti yang dilaporkan engineering FoodGo yaitu "Server backend kadang crash total dan perlu di-restart manual" selain itu pesanan yang dilakukan setelah kapasitaas penuh akan mengalami timeout dan aplikasi jadi lambat seperti yang ada paada laporan gejala engineering FoodGo ini "Aplikasi jadi sangat lambat, beberapa permintaan timeout"
 
**Solusi desain awal:** Menambahkan kode untuk memberikan timeout pada modul pesanan ketika panggil modul pembayaran, jadi diberi waktu 10 detik/disesuaikan dengan kebutuhan sehingga setelah 10 detik maka pesanan akan timeout dan tampilkan ke user bahwa pembayaran sedang ramai/sibuk (coba lagi), menambahkan sistem retry dengan backoff jika memungkinkan agar kalau gagal (bukan karena timeout) masih bisa diusahakan sistem

**Trade-off:** Pembayaran yang bisa diproses pada detik ke 11 akan otomatis timeout, waktu timeout bisa jadi terlalu lama dan kurang cocok dari segi pengguna dan server jadi harus dicari waktu timeout yang tepat, sistem retry backoff dapat menyebabkan duplikasi request pemanggilan modul dan bisa menambah beban server modul pembayaran karena request masuk terus (sesuai dengan jumlah retrynya)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
