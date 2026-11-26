# Jurnal Proses — Tugas 9

## Diskusi deployment model
- Opsi yang dipertimbangkan dan kenapa akhirnya memilih salah satu: Hybrid cloud menjadi opsi yang kami pertimbangkan,kenapa? karena menggabungkan keamanan dan kontrol dari Private Cloud dengan fleksibilitas serta skalabilitas dari Public Cloud,selain itu Hybrid Cloud merupakan model yang memungkinkan pemerintah menyimpan dan memproses data kependudukan yang bersifat rahasia pada Private Cloud yang sepenuhnya dikendalikan negara.

## Diskusi service model per komponen
- ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 24/11/2026 | claude | Saya mengerjakan tugas Cloud Computing tentang Sistem Data Kependudukan pemerintah (NIK, alamat, biometrik) yang sangat rahasia, diakses ribuan instansi dengan lonjakan saat pemilu dan pendaftaran sekolah, dan datanya tidak boleh berada di infrastruktur yang tidak dikendalikan penuh negara. Bantu analisis deployment model mana (Public, Private, Hybrid, atau Community) yang paling tepat, lalu jelaskan alasannya dengan mengaitkan lima karakteristik esensial cloud menurut NIST SP 800-145 dengan kebutuhan kerahasiaan vs skalabilitas. | Menyarankan Hybrid Cloud dengan inti Private Cloud pemerintah: data biometrik dan database di Private, API gateway dan cache non-sensitif di Public (cloud bursting saat lonjakan). Menjelaskan alasan menolak Public, Private, dan Community, memetakan 5 karakteristik NIST ke penerapan Hybrid, serta mitigasi risiko (enkripsi, tokenisasi, zero-trust, data minimization). | Membaca dan memahami alur argumen, memverifikasi definisi karakteristik NIST dengan NIST SP 800-145 dan materi kuliah, menulis ulang dengan bahasa sendiri, mendiskusikan dengan kelompok, lalu memilih poin yang relevan dan menambahkan rujukan UU PDP. |
|26/11/2026| Chatgpt |Private Cloud sama Hybrid secara kerahasiaan kan sama tuh kyknya trus misal aku mau memberdakannya gimana?| Chatgpt membenarkan namun juga mengkoreksi bahwasanya secara kerahasiaan Hybrid Cloud kemanan Tambahan untuk mencegah data bocor|Secara kerahasiaan jika menggunakan Private Cloud Seluruh data berada dalam lingkungan yang dikendalikan negara,memang terlihat sama kyk Hybrid Cloud namun, dengan hybrid Cloud dapat memberikan keamanan plus untuk memastikan data sensitif tetap disimpan dan diproses pada Private Cloud.|
