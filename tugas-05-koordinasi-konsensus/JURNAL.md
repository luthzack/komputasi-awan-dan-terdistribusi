# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: 
todo 4: ada sedikit terkendala dengan logika saat run, yang dimana permasalah tersebut menyebabkan saat node 4 dibunuh node 3 2 dan 1 tidak ada respon dan tidak melakukan election ulang untuk menjadi leader


## Skenario 1: Start normal
- Leader yang terpilih: ...
- Log/observasi: ...

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: leader dengan node id paling tinggi misal node 5 jadi leader lalu dimatikan leader setelahnya adalah node 4 begitu seterusnya node 4 dimatikan 3 menjadi leader
- Berapa lama waktu sampai leader baru terdeteksi: 2.0 detik pada saat node sebelumnya melakukan ping dan tidak ada respond dari leader sebelumnya dan melakukan election dengan memilih leader dengan id paling tinggi

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 14/10/2026 | Gemini | Apakah Algoritma Bully itu hanya ada 1 jenis atau ada banyak seperti algoritma searching, kalau ada banyak sebutkan jenisnya dan mekanismenya masing-masing | Ternyata yang jadi pusat itu election algoritma bukan bullynya, bully algorithm itu ada 3 jenis setelah optimasi (Klasik, modified dan fast) kemudian ada jenis algoritma election lainnya yaitu ring algorithm, raft election, paxos-based-election. | karena di tugas ini hanya memberikan 2 opsi (Bully dan Raft) dan secara spesifik disuruh menggunakan bully algorithm maka saya hanya fokus pada penjelasan mekanisme kedua algoritma itu untuk dibandingkan dan dianalisis lebih lanjut kemudian dituliskan ke README |
|  15/10/2026| claude | pada saat mematikan node 5 sebagai leader node 4 langusng election dan melakukan deklarasi menjadi leader namun kenapa saat node 4 dimatikan node 3 2 1 tidak ada respond? | claude mencarankan untuk cek lagi logika code pada todo 4 dan menyarankan untuk menghapus code logic yang tidak diperlukan |
