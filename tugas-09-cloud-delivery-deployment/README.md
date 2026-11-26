# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

## Jawaban
### 1. Rekomendasi Deployment Model

#### Rekomendasi: **Hybrid Cloud** 

Deployment Model yang paling sesuai untuk Sistem Data Kependudukan adalah Hybrid Cloud, yaitu kombinasi Private Cloud yang dikendalikan pemerintah dan Public Cloud sebagai infrastruktur pendukung.

Pemilihan Hybrid Cloud didasarkan pada kebutuhan sistem untuk menjaga kerahasiaan data kependudukan sekaligus menghadapi pola akses yang fluktuatif dari ribuan instansi. Data seperti NIK, nama, alamat, dan biometrik harus tetap disimpan dan diproses pada Private Cloud agar berada dalam kendali penuh negara. Sementara itu, Public Cloud digunakan untuk menangani layanan non-sensitif yang membutuhkan kapasitas elastis, seperti portal informasi dan distribusi konten publik.

Sebagai contoh, ketika memasuki musim pendaftaran sekolah, peningkatan pengunjung portal informasi dapat ditangani melalui penambahan kapasitas otomatis pada Public Cloud. Namun, permintaan verifikasi NIK tetap diproses pada Private Cloud sehingga data pribadi tidak berpindah ke infrastruktur pihak ketiga.

### Analisis Berdasarkan Karakteristik NIST 

| Karakteristik | Penerapan pada Sistem Data Kependudukan |
|---|---|
| **On-demand self-service** |Pemerintah dapat menambah VM dan kapasitas penyimpanan secara mandiri tanpa intervensi manual penyedia cloud, sementara akses data sensitif tetap dikendalikan negara |
| **Broad network access** | Dukcapil, kepolisian, dan bank mengakses layanan verifikasi melalui API dan koneksi aman sesuai kewenangan masing-masing |
| **Resource pooling** | Sumber daya server dan penyimpanan digunakan bersama oleh berbagai layanan dengan isolasi antarinstansi, sedangkan data sensitif tetap berada di Private Cloud |
| **Rapid elasticity** | Auto-scaling pada Public Cloud menangani lonjakan trafik non-sensitif saat pemilu atau pendaftaran sekolah, sementara kapasitas verifikasi ditingkatkan di Private Cloud |
| **Measured service** | Penggunaan CPU, storage, bandwidth, dan jumlah permintaan setiap instansi diukur untuk mengatur kuota, kapasitas, dan biaya operasional |

### 2.

### 3. Secara flexibilitas memang hybrid Cloud dapat diandalkan dalam mengeleola sumber daya, tetapi Hybrid Cloud masih terdapat risiko
|Resiko| Penjelasan | Mitigasi |
|---|---|---|
|Kebocoran Data|Kesalahan waktu konfigurasi jaringan atau integrasi layanan bisa menyebabkan data sensitif seperti NIK dan biometrik terekspos ke Public Cloud| Dapat dilakukannya penerapan segmentasi jaringan, enkripsi, kontrol akses berbasis peran (RBAC), memastikan data sensitif hanya disimpan dan diproses pada Private Cloud |
|Terjadinya Bottleneck pada Private Cloud|misal waktu musim pemilu atau pendaftaran sekolah, pastinya trafic akan naik dan lonjakan permintaan verifikasi identitas tetap membebani database inti meskipun Public Cloud telah melakukan auto-scaling|Menerapkan load balancing dan rate limiting untuk mengendalikan jumlah permintaan dari setiap instansi|
|Gangguan konektivitas antar-cloud|Gangguan jaringan antara Private Cloud dan Public Cloud dapat menghambat layanan yang membutuhkan komunikasi antarlingkungan| mungkin dapat disdiakannya jalur koneksi cadangan (redundant connection), mekanisme failover, dan pemantauan jaringan secara berkala |

### 4. Yang tidak kami pilih adalah menggunakan Murni Private Cloud,mengapa?

A. Secara kerahasiaan jika menggunakan Private Cloud Seluruh data berada dalam lingkungan yang dikendalikan negara,memang terlihat sama kyk Hybrid Cloud namun, dengan hybrid Cloud dapat memberikan keamanan plus untuk memastikan data sensitif tetap disimpan dan diproses pada Private Cloud.

B. Private Cloud dapat melakukan scaling, tetapi terbatas pada kapasitas infrastruktur yang tersedia. Sementara Hybrid Cloud, dia dapat memanfaatkan elastisitas Public Cloud untuk menangani lonjakan akses pada layanan non-sensitif, terutama saat musim pemilu atau pendaftaran sekolah tiba.

---

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.
