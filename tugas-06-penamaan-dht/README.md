# Tugas 6 (Pekan 6) — Penamaan & Resolusi Lokasi

**Materi terkait:** Flat Naming, Structured Naming (DNS), Distributed Hash Table (DHT)/Chord.

## Studi Kasus

Pelanggan FoodGo kesulitan menemukan alamat IP server kurir yang **dinamis** (kurir berpindah lokasi/jaringan, IP-nya sering berubah). FoodGo butuh cara memetakan **ID Kurir** (identitas tetap) ke **alamat IP terkininya** tanpa server pusat tunggal yang jadi bottleneck/single point of failure.

## Tugas Kelompok

Implementasikan **simulasi Chord DHT** sederhana (single-process, tidak perlu jaringan sungguhan — cukup simulasi struktur data & algoritma di satu program Python) yang memetakan ID Kurir ke alamat IP mereka.

Konsep yang harus terlihat jalan dalam simulasi kalian:
1. **Consistent hashing**: ID Kurir dan ID Node di-hash ke ruang angka yang sama (mis. 0–255 untuk kesederhanaan, `m=8` bit).
2. **Ring topology**: node-node diurutkan melingkar berdasarkan hasil hash-nya.
3. **Lookup**: fungsi `lookup(kurir_id)` yang menemukan node mana yang bertanggung jawab menyimpan mapping ID Kurir tersebut → alamat IP-nya (aturan Chord: node dengan ID hash **terkecil yang lebih besar atau sama dengan** hash key, disebut *successor*).
4. **Perubahan topologi**: simulasikan minimal satu node baru bergabung (`join`) atau satu node keluar (`leave`), tunjukkan bagaimana mapping berpindah tanggung jawab ke node lain.

Skeleton disediakan di `src/chord_simulation.py` dengan fungsi hashing dan struktur ring sudah ada — bagian `lookup()`, `join()`, dan `leave()` sengaja dikosongkan.

### Cara Menjalankan

```bash
python3 src/chord_simulation.py
```

## Tugas Analisis (`README.md`)

1. Jelaskan **kenapa DHT/Chord** lebih cocok untuk kasus ini dibanding **flat naming sederhana** (mis. tabel pusat ID→IP) atau **DNS konvensional** — kaitkan dengan sifat "IP kurir sering berubah" dan kebutuhan tanpa titik gagal tunggal.
2. Gambarkan (boleh pakai Mermaid, lihat Tugas 2) ring topology dari simulasi kalian, tandai node mana yang bertanggung jawab atas ID Kurir mana.
3. Jelaskan apa yang terjadi pada mapping saat sebuah node **keluar** dari ring (siapa yang mengambil alih tanggung jawabnya) — dukung dengan output program.

## Struktur Submission

```
tugas-06-penamaan-dht/
├── README.md      # Analisis + diagram ring
├── JURNAL.md
├── src/
│   └── chord_simulation.py
└── bukti/          # Output program (screenshot/log) untuk skenario join & leave
```

## Rubrik Penilaian (Tugas 6)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi lookup/join/leave benar | 35% | Consistent hashing & successor lookup sesuai aturan Chord |
| Bukti perubahan topologi (join/leave) | 25% | Output menunjukkan mapping berpindah dengan benar |
| Analisis kenapa DHT vs flat naming/DNS | 25% | Argumen spesifik ke kasus IP kurir dinamis, bukan definisi umum |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum consistent hashing/Chord ke AI; **tidak boleh** meminta AI menuliskan isi `# TODO` di `src/chord_simulation.py` (`find_successor`, `join`, `leave`, dst). Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `README.md` wajib menelusuri manual (langkah demi langkah) bagaimana `lookup()` menemukan successor untuk salah satu ID Kurir contoh yang dipakai di `chord_simulation.py` — bukan cuma menempelkan output program.



## Jelaskan **kenapa DHT/Chord** lebih cocok untuk kasus ini dibanding **flat naming sederhana** (mis. tabel pusat ID→IP) atau **DNS konvensional** — kaitkan dengan sifat "IP kurir sering berubah" dan kebutuhan tanpa titik gagal tunggal.

penggunaan DHT (terutama algoritma Chord) jauh lebih unggul dibandingkan flat naming sederhana (tabel pusat) maupun DNS konvensional , ini terjadi karena (misal) buat di sistem *flat naming (tabel pusat)* semua pembaruan IP kurir dan permintaan pencarian dari pelanggan harus melalui satu server yang sama. Nah ini bisa menyebabkan bottleneck karena server harus menangani banyak permintaan sekaligus. Lalu jika server ada gangguan sistem pelacakan bisa ikut berhenti karena tidak ada server lain yang mengambil alih.

Kalau *DNS KOnvensional* sendiri memang sudah terdistribusi, tetapi dia masih bergantung pada TTL dan mekanisme propagasi data. Trus apa hubungannya sama IP kurir berubah dalam waktu singkat? hubungannya adalah (misal lagi) si kuruir ganti jaringan dari wifi trus ke sinyal biasa, nah data yang tersimpan di cache bisa aja masih menggunakan IP lama. yang berakibat pelanggan memiliki resiko mendapatkan informasi alamat IP yang sudah tidak valid.

Oleh karena itu, *DHT/Chord* ini bisa mengatasi masalah tersebut melalui sistem yang terdistribusi. Dengan consistent hashing, setiap ID kurir dipetakan ke node tertentu yang bertanggung jawab menyimpan informasi IP-nya. Hal ini membuat pembaruan data tidak perlu dikirim ke seluruh jaringan atau melalui server pusat dan proses pencarian IP juga dilakukan dengan menelusuri ring Chord hingga menemukan node yang menyimpan data kurir tersebut. Trus plusnya lagi tidak ada Single Point of Failure. jadif misal salah satu node mengalami gangguan, node penerus (successor) dapat mengambil alih tanggung jawab penyimpanan data sesuai mekanisme pemulihan yang diterapkan. itulaah kenpoa Chord lebih sesuai dan unggulk untuk kebutuhan pelacakan kurir yang dinamis dan terdistribusi.


CONTIBUTOR : 
- NAUFAL LUTHFI MUAZKKI(103072400137) : ANALISIS Jelaskan **kenapa DHT/Chord** lebih cocok untuk kasus ini dibanding **flat naming sederhana** (mis. tabel pusat ID→IP) atau **DNS konvensional** — kaitkan dengan sifat "IP kurir sering berubah" dan kebutuhan tanpa titik gagal tunggal, TODO 6, 7 , 8, dan OUTPUT