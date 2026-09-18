# Tugas 1 (Pekan 1) — Identifikasi Masalah & Pitfall Sistem Terdistribusi

**Materi terkait:** Definisi sistem terdistribusi, tujuan desain (transparansi, skalabilitas, keterbukaan), *Fallacies of Distributed Computing* (pitfall klasik).

## Studi Kasus: FoodGo

Startup **FoodGo** (aplikasi pesan-antar makanan) mengalami kegagalan sistem saat pesanan melonjak (misalnya jam makan siang atau saat promo besar). Gejala yang dilaporkan tim engineering FoodGo:

- Aplikasi jadi sangat lambat, beberapa permintaan *timeout*.
- Server backend kadang *crash* total dan perlu di-restart manual.
- Tim menemukan bahwa kode mereka menulis asumsi seperti `# network is always reliable, no need for retry` dan tidak ada *timeout* sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu).
- Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama.

Ini merupakan gejala klasik dari **kesalahan asumsi tentang jaringan dan skala** yang terkenal di literatur sebagai *Fallacies of Distributed Computing* (Peter Deutsch et al.), ditambah masalah desain terkait skalabilitas.

## Tujuan Pembelajaran

Setelah tugas ini, kelompok harus mampu:
1. Mengidentifikasi asumsi keliru spesifik (bukan generik) yang menyebabkan kegagalan sistem terdistribusi.
2. Mengaitkan tiap pitfall dengan **gejala konkret** di skenario (bukan sekadar mengutip definisi buku).
3. Mengusulkan solusi desain awal yang realistis, dengan trade-off yang disadari (bukan solusi "pasang cloud lebih besar" tanpa analisis).

## Tugas Kelompok

1. **Identifikasi minimal 3 pitfall utama** yang dialami FoodGo dari daftar *Fallacies of Distributed Computing* (referensi: "the network is reliable", "latency is zero", "bandwidth is infinite", "the network is secure", "topology doesn't change", "there is one administrator", "transport cost is zero", "the network is homogeneous") **DAN/ATAU** masalah desain sistem terdistribusi lain yang relevan (mis. *single point of failure* karena arsitektur monolitik).
2. Untuk **tiap pitfall**, tulis:
   - Kutipan/paraphrase bagian skenario yang menunjukkan pitfall ini terjadi.
   - Penjelasan **kenapa** asumsi ini keliru dalam sistem terdistribusi nyata.
   - Dampak konkret ke FoodGo (mis. "karena tidak ada timeout, satu service pembayaran yang lambat membuat seluruh thread modul pesanan tertahan, akhirnya server kehabisan resource").
3. Usulkan **solusi desain awal** (tingkat konsep, bukan kode) untuk tiap pitfall — misalnya: timeout + retry dengan backoff untuk asumsi jaringan reliabel, circuit breaker, pemisahan modul jadi service terpisah, dsb.
4. Diskusikan **satu trade-off** dari solusi yang diusulkan (solusi tidak gratis — misalnya retry bisa memperparah beban saat *cascading failure*).

## Langkah Kerja yang Disarankan

1. Kelompok diskusi tatap muka/panggilan (bukan hanya chat teks) untuk membedah skenario bersama — dokumentasikan poin diskusi di `JURNAL.md`.
2. Tiap anggota mengambil 1 pitfall sebagai tanggung jawab utama (tulis analisisnya sendiri di `README.md`, dengan nama di bagian yang ditulis).
3. Gabungkan hasil, diskusikan solusi desain bersama sebagai kelompok.
4. Review silang: tiap anggota membaca dan mengomentari analisis rekan sebelum submit (catat di `JURNAL.md`).

## Struktur Submission

```
tugas-01-identifikasi-masalah-pitfall/
├── README.md      # Isi dengan template ANALISIS-TEMPLATE.md di bawah
├── JURNAL.md       # Log diskusi & proses berpikir kelompok
└── bukti/          # (opsional untuk tugas ini) screenshot diskusi/whiteboard
```

Gunakan [`ANALISIS-TEMPLATE.md`](ANALISIS-TEMPLATE.md) sebagai kerangka — salin isinya ke `README.md` kelompok kalian lalu isi bagian `[...]`.

## Rubrik Penilaian (Tugas 1)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan identifikasi pitfall | 25% | Pitfall yang dipilih benar-benar tercermin di skenario, bukan asal tempel definisi |
| Kedalaman analisis dampak | 30% | Menjelaskan mekanisme kegagalan (kenapa & bagaimana), bukan cuma "ini menyebabkan lambat" |
| Kualitas solusi & trade-off | 25% | Solusi realistis untuk tim kecil (bukan solusi enterprise berlebihan), trade-off disadari |
| Proses & kontribusi kelompok | 20% | `JURNAL.md` menunjukkan diskusi asli, tiap anggota terlihat kontribusinya |

## Batasan Penggunaan AI (Level 2)

Tugas ini memakai kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md) untuk aturan lengkap. Boleh memakai AI untuk brainstorming pitfall apa saja yang mungkin relevan atau menyusun outline analisis; **tidak boleh** meminta AI menuliskan analisis akhirnya (kaitan ke skenario, penjelasan dampak, usulan solusi) yang tinggal ditempel ke `README.md`. Catat setiap sesi pemakaian AI di bagian "Log Penggunaan AI" pada `JURNAL.md`.

Karena tugas ini murni analisis (rawan sekadar salin-tempel dari AI), verifikasi tambahan yang berlaku:
- Setiap pitfall harus dikaitkan dengan **kalimat spesifik** dari skenario di atas — jawaban generik yang bisa dipakai untuk skenario apa saja akan dinilai rendah pada komponen kedalaman analisis.


## Pitfall 1: [Network Is Realible] — ditulis oleh [Luthfi]

**Bukti di skenario:** "`# network is always reliable"

**Kenapa ini keliru:** penjelasan: karena pada jaringan yang trsidtribusi sangat tidak mungkin bahwa jaringan akan selalu ada, pasti akan terdapat paket loss dalam bentuk apapun itu bisa jadi kneksi tiba tiba hilang atau yang lainnya 

**Dampak ke FoodGo:** dampkanya pada saat terdapat transaksi dengan pelanggan akan terjadi gannguan jaringan yang berakibat kegagalan dalam transakasi, yang dimana misal pelanggan melakukan refresh atau retry transaksi "mungkin" akan berhasil dan sumber masalahnya hanya karena jaringan yang tiba tiba hilang

**Solusi desain awal:** kasih fiur tombol refresh dan pop up pembayaran gagal untuk mencegah kemungkinan pelanggan gagal payout tapi ternyata di foodgo malah udah masuk 

**Trade-off:** resikonya tagihannya bisa jadi double
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
Dari 3 pitfall yang kami tulis diatas, kalau tim engineering FoodGo menerapkan solusi desain kami mungkin arsitektur yang cocok adalah arsitektur Microservices, karena dengan memisahkan modul-modul yang berat server dari FoodGo dapat mengurangi beban yang berlebihan pada server utama, selain itu juga akan memudahkan FoodGo untuk mengatur resource setiap modul service yang terpisah dan meminimalisir terjadinya hal yang tidak diinginkan (Server backend crash total, aplikasi jadi lambat serta pembayaran yang tidak kunjung selesai), namun akan ada tantangan seperti kompleksitasnya meningkat untuk mengatur komunikasi antar modul service.