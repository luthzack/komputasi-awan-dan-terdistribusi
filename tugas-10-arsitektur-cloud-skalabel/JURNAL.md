# Jurnal Proses — Tugas 10

## Setup Nginx & multi-instance
- Kendala saat konfigurasi upstream: *[Diisi oleh anggota bagian Nginx/Docker Compose]*

## Hasil Load Test Horizontal (3 instance)
- Distribusi request per instance: *[Diisi oleh anggota bagian Load Test Horizontal]*

## Hasil Setelah Scale-up (4 instance)
- Distribusi request per instance: *[Diisi oleh anggota bagian Scale-up 4 Instance]*

## Hasil Vertical Scaling (1 instance besar)
- Latensi/kegagalan dibanding horizontal: Pengujian 1 container tunggal (`ticketgo-vertical`, limit 2 CPU & 1GB RAM pada port 8000, tanpa load balancer) dengan 300 request (20 thread konkuren) menghasilkan **300/300 sukses (0 gagal)**, total waktu **1.46 detik**, rata-rata latensi **73.06 ms**, dan latensi maksimum (*tail latency*) **612.99 ms** akibat seluruh koneksi menumpuk pada satu instance/socket tunggal (pada percobaan awal saat target `localhost` tidak merespons, tercatat 0/500 sukses dan 500 gagal dalam 50.93 detik)[cite: 22, 24].

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline – bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
<<<<<<< HEAD
|28/11/2026| chatgpt | apakah ada cara lain yang lebih efisien secara waktu untuk membatasi concurency? | chatgpt menyarankan menggunakan semaphore | memanggil semaphore, semaphore = threading.Semaphore(CONCURRENCY) |
=======
| 2026-11-27 | Gemini | Diskusi alur melengkapi `INSTANCE_ID` pada `app/app.py` port 8000, cara membatasi resource CPU/RAM untuk simulasi Vertical Scaling, serta kerangka poin perbandingan Vertical vs Horizontal Scaling | Menjelaskan cara membaca `INSTANCE_ID` dari environment variable, penggunaan flag `--cpus` dan `--memory` pada Docker untuk 1 instance besar, serta garis besar poin teknis seperti antrean koneksi tunggal dan *Single Point of Failure* | Mengimplementasikan langsung `INSTANCE_ID` pada `app/app.py` di port 8000, menguji secara lokal, menjalankan load test Vertical Scaling secara mandiri, dan menyusun catatan hasil serta analisis berdasarkan angka eksperimen sendiri |
| ... | ... | ... | ... | ... |
>>>>>>> origin/Naufal
