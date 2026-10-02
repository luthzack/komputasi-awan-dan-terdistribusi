# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: 
![](../tugas-03-multithreading-container/bukti/hasil_tanpa_lock.png)

# Codenya
![](../tugas-03-multithreading-container/bukti/TANPA_LOCK.png)

- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Hal ini dapat terjadi karena "processed_count" dipakai bersama oleh 10 thread.Yang dimana increment sebenarnya terdiri dari tiga langkah (baca nilai, tambah 1, tulis kembali), karena tidak adanya proteksi dengan memberikan lock, dua thread bisa membaca nilai lama yang sama lalu keduanya menulis hasil yang sama dan satu pesanan hilang, nah karena itu increment dibungkus pakai "with lock" agar hanya satu thread yang dapat menjalankan langkah baca, tambah, dan tulis dalam satu waktu sehingga hasilnya konsisten tepat 100


## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: ![](../tugas-03-multithreading-container/bukti/PAKE_LOCK.png)

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
|03-10-2026|chatgpt |ini untuk todo 2 maksudnya itu aku disuruh run dulu sebelum diubah sama setelah di tambahkan increment lock kah apa kek mana? | ringkasan/saran/ide AI adalah pendapatku hampir benar tapi ai menambahkan "bukan berarti kamu menjalankan kode kosong namun tidak perlu memanggil fungsi "with_lock" yang sudah kamu buat" | jadi saya langsung masukin current = processed_count
        time.sleep(0)
        processed_count = current + 1
tidak menggunakan "with_lock" agar jalan tanpa lock |
