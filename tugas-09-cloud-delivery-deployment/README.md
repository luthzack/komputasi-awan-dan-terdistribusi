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

#### Rekomendasi: **Hybrid Cloud** (inti Private Cloud milik negara)

- **Private Cloud pemerintah** → menyimpan dan memproses data inti (NIK, biometrik, alamat) di bawah kendali penuh negara.
- **Public Cloud** (idealnya dengan region di Indonesia) → melayani lapisan akses (API gateway, portal verifikasi, cache non-sensitif) agar bisa melonjak saat pemilu atau pendaftaran sekolah.

### 2. Perbandingan Deployment Model

| Model | Kelebihan | Kekurangan untuk kasus ini |
|---|---|---|
| **Public** | Elastis, biaya rendah | Data biometrik berada di infrastruktur pihak ketiga, bertentangan dengan syarat "terkendali penuh negara" |
| **Private** | Kontrol dan kerahasiaan maksimal | Kapasitas harus disediakan untuk beban puncak (mahal), tetap berisiko downtime saat lonjakan melebihi kapasitas |
| **Community** | Cocok untuk instansi dengan kepentingan bersama | Pengguna (dukcapil, polisi, bank) tidak berbagi satu komunitas setara; bank adalah pihak swasta |
| **Hybrid** ✅ | Kontrol data + elastisitas | Integrasi dan keamanan antar-lingkungan lebih kompleks (dapat dimitigasi) |

### 3. Analisis Berdasarkan Karakteristik NIST SP 800-145

| Karakteristik | Kebutuhan Sistem | Penerapan pada Hybrid Cloud |
|---|---|---|
| **On-demand self-service** | Ribuan instansi perlu onboarding cepat | Portal self-service untuk registrasi instansi, penerbitan API key, dan pengaturan kuota. Provisioning otomatis, persetujuan akses tetap diverifikasi pemerintah. |
| **Broad network access** | Diakses dukcapil daerah, polisi, bank dari banyak lokasi | API terstandar (REST/HTTPS) melalui API gateway. Instansi kritis memakai jalur privat (VPN/leased line); akses publik wajib mTLS dan autentikasi kuat. |
| **Resource pooling** | Sumber daya dipakai bersama banyak instansi | Multi-tenancy dengan isolasi ketat per instansi. Pool di Public Cloud hanya memproses data non-sensitif atau data yang sudah di-tokenisasi. |
| **Rapid elasticity** | Lonjakan saat pemilu dan pendaftaran sekolah | **Cloud bursting**: beban dasar di Private Cloud, kelebihan beban diteruskan ke Public Cloud lewat auto-scaling pada lapisan aplikasi dan cache. |
| **Measured service** | Akuntabilitas pemakaian dan audit | Metering per instansi (jumlah query, bandwidth) untuk kuota/penagihan, serta **audit trail** siapa mengakses NIK siapa (kepatuhan UU PDP). |

### 4. Pembagian Beban Kerja (Workload Placement)

#### Private Cloud (kerahasiaan)

- Database kependudukan dan biometrik
- Layanan pencocokan biometrik
- Manajemen kunci enkripsi (HSM) dan log audit

#### Public Cloud (skalabilitas)

- API gateway, load balancer, rate limiting
- Cache respons non-sensitif dan portal informasi
- Antrean permintaan saat lonjakan

### 5. Titik Tegang: Kerahasiaan vs Skalabilitas

| Tuntutan | Kecenderungan arsitektur |
|---|---|
| Kerahasiaan: data tidak boleh keluar dari kendali negara | Condong ke **Private** |
| Skalabilitas: kapasitas elastis dan murah | Condong ke **Public** |

**Solusi Hybrid:** memisahkan *data* (tetap di private) dari *beban komputasi akses* (elastis di public). Rapid elasticity hanya diterapkan pada lapisan yang tidak menyimpan data sensitif, sehingga risiko kebocoran tetap terkendali.

---

### 6. Mitigasi Risiko Hybrid

1. **Enkripsi** data at-rest dan in-transit, dengan kunci dipegang pemerintah.
2. **Tokenisasi/pseudonimisasi** bila data harus melintas ke public.
3. **Zero-trust** dan segmentasi jaringan antar-lingkungan.
4. **Data minimization:** instansi (misalnya bank untuk KYC) hanya menerima jawaban verifikasi (cocok/tidak cocok), bukan data mentah.
5. **Residensi data** di wilayah Indonesia sesuai regulasi.

---

### 7. Kesimpulan

**Hybrid Cloud berbasis Private Cloud pemerintah** adalah pilihan paling tepat karena:

- Kelima karakteristik NIST terpenuhi.
- Kontrol penuh atas data rahasia tetap terjaga.
- Lonjakan akses musiman ditangani lewat cloud bursting pada lapisan non-sensitif.

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
