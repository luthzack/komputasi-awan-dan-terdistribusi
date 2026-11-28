# Jurnal Proses — Tugas 10

## Setup Nginx & multi-instance
- Kendala saat konfigurasi upstream: ...

## Hasil Load Test Horizontal (3 instance)
- Distribusi request per instance: ...

## Hasil Setelah Scale-up (4 instance)
- Distribusi request per instance: ...

## Hasil Vertical Scaling (1 instance besar)
- Latensi/kegagalan dibanding horizontal: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
|28/11/2026| chatgpt | apakah ada cara lain yang lebih efisien secara waktu untuk membatasi concurency? | chatgpt menyarankan menggunakan semaphore | memanggil semaphore, semaphore = threading.Semaphore(CONCURRENCY) |
