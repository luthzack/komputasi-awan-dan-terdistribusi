# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Naufal Luthfi Muzakki | [103072400137] | [1 & 3] |
| Nur Ro'yul Amin | [103072400159] | [2 & 3] |

## Pitfall 1: [Network Is Realible] — ditulis oleh [Luthfi]

**Bukti di skenario:** "`# network is always reliable"

**Kenapa ini keliru:** penjelasan: karena pada jaringan yang terdistribusi sangat tidak mungkin bahwa jaringan akan selalu ada, pasti akan terdapat paket loss dalam bentuk apapun itu bisa jadi kneksi tiba tiba hilang atau yang lainnya 

**Dampak ke FoodGo:** dampkanya pada saat terdapat transaksi dengan pelanggan bisa terjadi gangguan jaringan yang berakibat kegagalan dalam transakasi, yang dimana misal pelanggan melakukan refresh atau retry transaksi "mungkin" akan berhasil dan sumber masalahnya hanya karena jaringan yang tiba tiba hilang

**Solusi desain awal:** kasih fiur tombol refresh dalam refresh dan pop up pembayaran gagal untuk mencegah kemungkinan pelanggan gagal payout tapi ternyata di foodgo malah udah masuk 

**Trade-off:** resikonya adalah tagihan yang akan dibayar oleh pelanggan bisa jadi double dan juga request ke sever bisa membeludak akibat refresh terlalu banyak oleh pelanggan

---

## Pitfall 2: [Latency is Zero] — ditulis oleh [Ro'yul]

**Bukti di skenario:** "tidak ada *timeout* sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)"

**Kenapa ini keliru:** penjelasan: Karena anggapan "tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)" ini seperti kita tidak perlu menerapkan timeout pada proses pemanggilan modul pembayaran dan hasil komputasi/proses dari modul ini bisa didapat secara zero ms paadahal hal seperti itu tidak mungkin, modul pembayaran pada FoodGo tentu memerlukan waktu untuk memproses hasil komputasinya. Ketika banyak modul pesanan yang memanggil modul pembayaran maka akan memakan banyak waktu ditambah tidak ada timeout yang bisa menyebabkan modul pesanan menunggu jawaban tanpa batas waktu.

**Dampak ke FoodGo:** Saat trafik naik(Misal jam makan siang atau saat ada promo besar) akan ada banyak pesanan masuk otomatis modul pesanan akan memanggil modul pembayaran dengan jumlah yang banyak (requestnya), karena tidak ada timeout pada proses pemanggilan antar kedua service ini maka beban ke server akan terus meningkat hingga server tidak mampu menangani pesanan baru (yang melebihi kapasitas resource server) sehingga terjadi gejala seperti yang dilaporkan engineering FoodGo yaitu "Server backend kadang crash total dan perlu di-restart manual" selain itu pesanan yang dilakukan setelah kapasitaas penuh akan mengalami timeout dan aplikasi jadi lambat seperti yang ada paada laporan gejala engineering FoodGo ini "Aplikasi jadi sangat lambat, beberapa permintaan timeout"
 
**Solusi desain awal:** Menambahkan kode untuk memberikan timeout pada modul pesanan ketika panggil modul pembayaran, jadi diberi waktu 5 detik/disesuaikan dengan kebutuhan sehingga setelah 5 detik maka pesanan akan timeout dan tampilkan ke user bahwa pembayaran sedang ramai/sibuk (coba lagi), menambahkan sistem retry dengan backoff jika memungkinkan agar kalau gagal (bukan karena timeout) masih bisa diusahakan sistem

**Trade-off:** Pembayaran yang bisa diproses pada detik ke 6 akan otomatis timeout, waktu timeout bisa jadi terlalu cepat dan kurang cocok dari segi server jadi harus dicari waktu timeout yang tepat, sistem retry backoff dapat menyebabkan duplikasi request pemanggilan modul dan bisa menambah beban server modul pembayaran karena request masuk terus (sesuai dengan jumlah retrynya)

---

## Pitfall 3: [Single Point of Failure karena Arsitektur Monolitik] — ditulis oleh [luthfi & ro'yul]

**Bukti di skenario:**  Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama

**Kenapa ini keliru:** penjelasan: karena aristektur monolitik ini yang dimana artinya mereka berbagi dalam satu proses CPU, memori, dan thread pool yang sama akan membebani kinerja server dan juga ini tidak sesuai dengan prinsip skalabilitas yang dimana sebaiknya dibagi menjadi setiap modulnya tersendiri tanpa mengganggu modul lainnya

**Dampak ke FoodGo:** dampaknya jika masih menggunakan arsitektur monolitik foodgo pada setiap modul akan terganggu satu sama lain, karena berjalan pada satu sistem yang sama ketika terjadi gangguan pada suatu proses (misal pembayaran atau notifikasi kurir ) dapat terjadi kelambatan pada server hingga worst casenya adalah crash total pada seluruh apk foodgo 

**Solusi desain awal:** Berdasarkan analisis diatas itu semua modulnya dijalankan pada 1 server, solusi yang saya berikan adalah memindahkan modul-modul yang ada pada 1 server itu menjadi sebuah modul service yang terpisah, jadi setiap modul dideploy sendiri-sendiri yang akan mempermudah peningkatan resource server sesuai dengan kebutuhan modulnya, sehingga server utama aplikasi FoodGo tidak akan mengalami crash

**Trade-off:** Proses pemisahan modul service akan meningkatkan kinerja aplikasi dan mengurangi kelambatan, namun kompleksitas kodenya akan menjadi tinggi mulai dari mengurus komunikasi antar modul service, penanganan antara modul service kalau gagal terhubung, penaganan timeout, pemantauan kelancaran sistem dan lain-lain.

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
