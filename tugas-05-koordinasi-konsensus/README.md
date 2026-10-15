# Tugas 5 (Pekan 5) — Koordinasi & Konsensus

**Materi terkait:** Physical/Logical Clock, Election Algorithm (Bully/Raft).

## Studi Kasus

Terjadi konflik urutan waktu pada pesanan FoodGo (dua server mencatat urutan pesanan berbeda karena jam tidak sinkron), dan sistem membutuhkan satu **"Node Leader"** untuk mengelola antrean pesanan pusat agar tidak terjadi konflik pemrosesan ganda.

## Tugas Kelompok

Implementasikan simulasi **Bully Algorithm** untuk memilih leader di antara **5 node virtual** yang berjalan sebagai 5 proses Python terpisah di laptop yang sama (tiap node = satu proses di port berbeda, komunikasi lewat TCP socket di `localhost`).

Skeleton yang disediakan (`src/node.py`) sudah menangani bagian **infrastruktur jaringan** (membuka socket, menerima & mengirim pesan antar node) — bagian **algoritma Bully sendiri sengaja dikosongkan** (`# TODO`), karena itu inti pembelajaran tugas ini.

### Aturan Bully Algorithm yang harus diimplementasikan

1. Node yang mendeteksi leader tidak merespons (atau saat start pertama kali) mengirim pesan `ELECTION` ke semua node dengan ID **lebih besar** darinya.
2. Jika ada node ber-ID lebih besar yang merespons `OK`, node yang memulai election **berhenti mencalonkan diri** dan menunggu pesan `COORDINATOR`.
3. Jika **tidak ada** node ber-ID lebih besar yang merespons dalam batas waktu tertentu, node tersebut menjadi leader dan mem-broadcast `COORDINATOR` ke semua node lain.
4. Semua node mencatat siapa leader saat ini.

### Cara Menjalankan

Buka 5 terminal terpisah (satu per node):
```bash
python3 src/node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
python3 src/node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
python3 src/node.py --id 3 --port 5003 --peers 5001,5002,5004,5005
python3 src/node.py --id 4 --port 5004 --peers 5001,5002,5003,5005
python3 src/node.py --id 5 --port 5005 --peers 5001,5002,5003,5004
```

### Skenario Wajib Diuji & Dicatat

1. **Start normal**: nyalakan node 1–5 hampir bersamaan, catat siapa yang terpilih jadi leader (harusnya node ber-ID tertinggi, yaitu node 5).
2. **Leader mati**: matikan (Ctrl+C) proses node leader (node 5), amati node lain mendeteksi leader hilang dan memicu election baru. Catat leader baru yang terpilih (harusnya node 4).
3. Simpan log terminal (screenshot atau `> log_nodeX.txt` redirect) dari kedua skenario ke folder `bukti/`.

## Struktur Submission

```
tugas-05-koordinasi-konsensus/
├── README.md      # Analisis: kenapa perlu leader, kenapa Bully (vs Raft), hasil 2 skenario
├── JURNAL.md
├── src/
│   └── node.py
└── bukti/          # Log/screenshot skenario start normal & leader mati
```

## Rubrik Penilaian (Tugas 5)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi Bully Algorithm benar | 35% | Election, OK, COORDINATOR message bekerja sesuai aturan algoritma |
| Bukti skenario leader mati → re-election | 30% | Log jelas menunjukkan leader baru terpilih otomatis |
| Analisis (kenapa perlu leader, trade-off Bully vs Raft) | 20% | Dikaitkan ke masalah urutan pesanan di skenario FoodGo |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI tentang gambaran umum algoritma election; **tidak boleh** meminta AI menuliskan isi `# TODO` di `src/node.py` (logika `on_message`, `start_election`, `declare_leader`, `monitor_leader`). Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `README.md` wajib menjelaskan kenapa Bully Algorithm selalu memilih node ber-ID tertinggi yang masih hidup, dan apa kelemahannya dibanding algoritma lain (mis. jumlah pesan yang dikirim saat election, single point of failure sebelum leader baru terpilih) — bukan sekadar definisi generik.


#### Kenapa Bully Algorithm selalu piiih node dengan ID tinggi?
Karena proses pemilihan node leader tidak akan menjadi rumit, hanya perlu membandingkan ID node sendiri dengan ID node yang lain dan tujuan akhirnya adalah node dengan ID paling tinggi. Pencarian ID tertinggi itu arahnya pasti (tidak perlu cek nilai ID dari semua node ketika ada node yang menjawab `OK`, hanya perlu cek apakah ada ID dengan nilai di atas node itu sekarang, kalau tidak ada jawaban maka bisa jadi Nodenya mati, kalau dari awal tidak ada yang lebih tinggi dari id saat ini maka langsung jadi `node leader`)

#### Kelemahan Bully Algoritm Dibanding Algoritma yang lain
1. Node Leader sering terputus. Node leader (anggap saja 5) bisa saja mengalami gangguan dijaringannya yang digunakan untuk mengatur kepemimpinannya dan terjadi restart, disaat restart otomatis `ELECTION` terjadi dan node id 4 terpilih, disaat node id 5 kembali hidup maka dia akan melakukan `ELECTION` dan merebut gelar leader dari node id 4, Jika hal ini berlangsung terus menerus maka sistem tidak bisa fokus melakukan pekerjaannya karena harus urus `ELECTION`
2. SPOF (Single Point Of Failure). Kondisi dimana sistem itu kehilangan Node leader sedangkan sistem masih harus memproses pesanan yang masuk, pesanan itu akan tergantung menunggu diarahkan (sistem down). Apabila dalam waktu `ELECTION` ternyata pesanan itu membludak bisa saja terjadi hal yang tidak diinginkan (Pembayaran dilakukan 2 kali, penjualan melebihi stok, server crash karena pesanan menumpuk)

#### Analisis (kenapa perlu leader, trade-off Bully vs Raft)

diperlukan Leader pada kasus FoodGo karena dua server mencatat urutan pesanan yang berbeda karena jam fisiknya tidak sinkron, jadi pesanan yang sama bisa diproses dua kali atau dalam urutan yang beda. Solusinya kita pakai satu **node leader** yang jadi satu-satunya pengelola antrean pusat. dengan begitu urutan pesanan jadi punya satu sumber kebenaran dan tidak lagi bergantung pada jam tiap server, pemrosesan ganda juga tercegah karena hanya leader yang boleh memproses antrean, sementara node lain cukup tahu siapa leader-nya. Konsekuensinya, leader jadi titik kritis: kalau misal dia mati, sistem jadi harus cepat memilih pengganti, nah di sinilah election algorithm (Bully) berperan.

#### Trade-off Bully vs Raft

Bully memilih leader berdasarkan ID tertinggi jadi buat node yang hidup dengan ID paling besar otomatis jadi Leader. Cara ini simpel dan gampang diimplementasikan, tapi punya beberapa kelemahan seperti  pada Saat jaringan terpartisi, tiap sisi bisa memilih leader sendiri (split brain), sehingga bisa ada dua leader sekaligus. Selain itu, node ber-ID tinggi yang kembali hidup langsung merebut posisi leader walaupun leader sekarang masih sehat, jadi leader bisa gonta-ganti. Bully juga hanya memilih leader dan tidak menjamin data antrean tetap konsisten, dan jumlah pesannya bisa membengkak kalau node ber-ID terendah yang memulai election.

di sisi lain misal raft memilih leader lewat voting yang dimana kandidat harus mendapat suara mayoritas dalam satu term. Karena butuh mayoritas, hanya sisi partisi yang punya mayoritas yang bisa punya leader jadi split brain tidak terjadi. Leader lama juga tidak digeser selama term-nya masih yang terbaru, dan Raft punya log replication sehingga data dianggap sah setelah tersimpan di mayoritas node. masalahnya , Raft lebih rumit karena ada term, vote, heartbeat, dan replikasi log.


Kontribusi Kelompok : 
Naufal luthfi Muzakki 103072400137 (Todo 3, 4 , analisis , dan tradeoff bully vs Raft)
Nur Ro'yul Amin (Todo 1,2, Kenapa Bully Algorithm selalu piiih node dengan ID tinggi?, dan Kelemahan Bully Algoritm Dibanding Algoritma yang lain )