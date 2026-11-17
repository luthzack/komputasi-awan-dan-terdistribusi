# Tugas 7 (Pekan 7) — Konsistensi Data

**Materi terkait:** Data-Centric Consistency (Sequential, Eventual), Client-Centric Consistency.

## Studi Kasus

Data saldo *e-wallet* pelanggan FoodGo berbeda antara server wilayah **Jakarta** dan **Bandung** karena replikasi antar server berjalan lambat. Contoh kasus nyata: pelanggan top-up saldo lewat server Jakarta, lalu dalam hitungan detik memesan makanan lewat aplikasi yang tersambung ke server Bandung — saldo belum ter-update, transaksi ditolak padahal saldo sebenarnya cukup.

## Tugas Kelompok

### Bagian 1 — Analisis (wajib)

1. Tentukan: apakah kasus ini **membutuhkan Sequential Consistency** (semua replika melihat urutan operasi yang sama) atau **cukup Eventual Consistency** (replika akan konsisten "pada akhirnya", boleh sementara berbeda)? Berikan argumen berbasis dampak bisnis (mis. kasus saldo *e-wallet* jauh lebih sensitif dibanding kasus "jumlah like" di media sosial).
2. Jika kalian menyimpulkan Eventual Consistency saja **tidak cukup** untuk skenario ini, usulkan pendekatan **Client-Centric Consistency** yang relevan (mis. *Read-Your-Writes*: pelanggan yang baru top-up harus selalu melihat saldo terbarunya sendiri, walau replika lain belum sinkron).
3. Gambarkan **diagram alir urutan (sequence diagram)** yang menunjukkan operasi read/write antara pelanggan, server Jakarta, server Bandung, dan proses replikasi — untuk skenario **tanpa** jaminan konsistensi (bug terjadi) DAN skenario **dengan** solusi yang kalian usulkan (bug teratasi). Pakai Mermaid (`sequenceDiagram`) di `README.md` — lihat contoh cara pakai di Tugas 2.

### Bagian 2 — Simulasi (opsional, nilai tambah)

Skeleton `src/replica_simulation.py` mensimulasikan dua replika (Jakarta & Bandung) dengan delay replikasi buatan. Lengkapi TODO untuk:
1. Menunjukkan kondisi **inconsistent read** (replika Bandung masih menunjukkan saldo lama walau Jakarta sudah update).
2. Mengimplementasikan mekanisme **Read-Your-Writes** sederhana (mis. dengan version/timestamp per client) yang memperbaiki masalah tersebut.

```bash
python3 src/replica_simulation.py
```

## Struktur Submission

```
tugas-07-konsistensi-data/
├── README.md      # Analisis konsistensi + sequence diagram Mermaid
├── JURNAL.md
├── src/            # (opsional) simulasi replikasi
└── bukti/          # (jika mengerjakan simulasi) output program
```

## Rubrik Penilaian (Tugas 7)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan pemilihan model konsistensi | 30% | Argumen berbasis dampak bisnis nyata, bukan hafalan definisi |
| Kualitas sequence diagram | 30% | Menunjukkan jelas titik kegagalan & titik perbaikan |
| Usulan solusi client-centric | 25% | Solusi konkret dan dapat diimplementasikan (bukan wacana abstrak) |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history (+ bonus jika simulasi dikerjakan) |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum consistency model ke AI untuk brainstorming; **tidak boleh** meminta AI menuliskan analisis akhir/sequence diagram atau isi `# TODO` di `src/replica_simulation.py` yang tinggal ditempel. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Sebagai bukti pemahaman konsep (bukan hafalan jawaban skenario FoodGo saja), `README.md` wajib menyertakan **satu skenario tambahan** yang kalian buat sendiri (mis. kasus lain di aplikasi ojek online) dan menentukan model konsistensi yang tepat untuk skenario tambahan tersebut.


1. Tentukan: apakah kasus ini **membutuhkan Sequential Consistency** (semua replika melihat urutan operasi yang sama) atau **cukup Eventual Consistency** (replika akan konsisten "pada akhirnya", boleh sementara berbeda)? Berikan argumen berbasis dampak bisnis (mis. kasus saldo *e-wallet* jauh lebih sensitif dibanding kasus "jumlah like" di media sosial).

-> Pada kasus FoodGo, terjadi perbedaan saldo pelanggan antara server Jakarta dan Bandung karena proses replikasi membutuhkan waktu. Contohnya, pelanggan top-up Rp50.000 lewat server Jakarta, tapi saat memesan makanan melalui server Bandung, jadinya saldo yang terbaca masih Rp0 kenapa? karena data terbaru belum sinkron.

Menurut saya(luthfi), **Eventual Consistency saja tidak cukup** untuk kasus ini karena saldo e-wallet berkaitan langsung dengan transaksi keuangan. Perbedaan saldo bisa menyebabkan transaksi ditolak meskipun pelanggan sebenarnya memiliki saldo yang cukup.

beda dengan kasus  jumlah like di media sosial yang masih bisa mengalami keterlambatan pembaruan, data saldo harus lebih akurat dan tidak boleh terlambat, karena berpengaruh langsung ke transaksi dan kepercayaan pelanggan.

Sequential Consistency bisa menjaga urutan operasi tetap konsisten, tapi belum tentu menjamin pembacaan data terbaru secara langsung. Oleh karena itu, menurut sayaFoodGo butuh mekanisme konsistensi yang lebih kuat untuk transaksi saldo, sementara Eventual Consistency masih dapat digunakan untuk proses replikasi data.

2. Jika kalian menyimpulkan Eventual Consistency saja **tidak cukup** untuk skenario ini, usulkan pendekatan **Client-Centric Consistency** yang relevan (mis. *Read-Your-Writes*: pelanggan yang baru top-up harus selalu melihat saldo terbarunya sendiri, walau replika lain belum sinkron).

->Untuk solusinya saya(luthfi), menurut saya menggunakan Read-Your-Writes Consistency, yaitu pendekatan Client-Centric Consistency yang dimana memastikan pelanggan dapat membaca perubahan data terakhir yang telah dilakukannya.

bagiamana solusi ini bekerja? 
jadi,Pelanggan melakukan top-up melalui server Jakarta lalu server Jakarta memperbarui saldo dan memberikan nomor versi terbaru kepada pelanggan,Pelanggan berpindah ke server Bandung untuk memesan makanan dengan membawa informasi versi tersebut, nah server Bandung memeriksa versi saldo yang dimiliki user ini,Jika versinya lebih lama,server Bandung mengarahkan pembacaan ke server Jakarta atau menunggu replikasi selesai,Setelah mendapatkan saldo terbaru, proses pemesanan dapat dilanjutkan.

jika diimplemetasikan mungkin seperti ini
| Proses | Server Jakarta | server Bandung | 
|---|---|---|
| Sebelum top-up | Rp0 (data awal 0) | Rp0 (data awal 0) |
| Setelah top-up | Rp50.000 | Rp0 |
| Pemeriksaan versi | Rp50.000 | Redirect ke Jakarta |
| Setelah replikasi | Rp50.000  | Rp50.000 |

jadi jika akai mekanisme ini, pelanggan tidak akan membaca saldo lama ketika berpindah server. Selain itu, FoodGo tetap perlu melakukan validasi dan pengurangan saldo secara atomik untuk mencegah transaksi ganda.

3. Gambarkan **diagram alir urutan (sequence diagram)** yang menunjukkan operasi read/write antara pelanggan, server Jakarta, server Bandung, dan proses replikasi — untuk skenario **tanpa** jaminan konsistensi (bug terjadi) DAN skenario **dengan** solusi yang kalian usulkan (bug teratasi). Pakai Mermaid (`sequenceDiagram`) di `README.md` — lihat contoh cara pakai di Tugas 2.

