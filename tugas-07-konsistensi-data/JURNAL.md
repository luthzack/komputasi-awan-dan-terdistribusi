# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan:  Royul kekeh dengan Sequential Consistency lebih tepat karena semua replika perlu melihat urutan operasi yang sama agar data saldo tidak berbedan nah aku(luthfi) memberikan saran menggunakan Read-Your-Writes sebagai solusi supaya pelanggan tetap dapat melihat saldo terbaru setelah melakukan top-up.
- Kesimpulan akhir & alasan: Kami memutuskan menggunakan Eventual Consistency yang dilengkapi Read-Your-Writes. karena proses replikasi tetap dapat berjalan secara bertahap, tetapi pelanggan tidak akan membaca perubahan saldo miliknya yang masih tertinggal.

## Simulasi (jika dikerjakan)
- Hasil skenario naif vs Read-Your-Writes: 

- Skenario Naif saat user1 melakukan top up server jakarta langsung tulis saldo 50k sementara bandung tertunda 2 detik. Karena pembacaan di Bandung dilakukan sebelum 2.0 detik selesai, Bandung masih mengembalikan saldo 0k. Diakhir-akhir bandung baru mendapat updatenya namun transaksi user terlanjur sudah dilakukan dan ditolak

- Skenario Read-Your-Write Saat Top-up kedua dilakukan server jakarta langsung catat total saldonya 70k dan replikasi bandung ditunda lagi 2 detik (Repliacation_Delay variabel global), kemudian server bandung cek ke server jakarta apakah ada perubahan dengan time sleep 0.5 artinya dalam 2 detik itu dilakukan pengecekan setiap 0.5 detik ke server jakarta untuk cek apakah ada write terbaru dan berjalan sebanyak 5 kali karena di detik ke 2 itu masih belum terdeteksi perubahan sehingga 2.5 detik baru dapat perubahan dan emang ada perubahan terbaru berjkumlah 70k. Akhirnya sistem menampilkan 70k untuk usernya

- Perbandingan: Skenario naif merespons cepat tapi rawan membaca data lama (0.0), sedangkan Read-Your-Writes dengan strategi polling menjamin saldo selalu benar (70000.0) dengan konsekuensi adanya jeda tunggu ~2 detik hingga replika lokal sinkron.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17-11-2026 | gpt | berikan aku bantuan memahami penerapan Read-Your-Writes Consistency sebagai solusi terhadap masalah keterlambatan replikasi data. | memberikan penjelasan | dipahami dan dijelaskan lebih mendetail |
17-11-2026|Gemini|Perbedaan polling dan redirek langsung|gemini memberikan jawaban perbedaannya kelebihan dan kekurangan kedua hal itu juga, juga menyarankan bentuk kombinasi ataupun terpisah|saya memilih bentuk polling saja untuk kodenya|
|17-11-2026|Gemini|apa perbedaan Sequential, Eventual, dan client-centric (read-yout-write) dengan contoh dunia nyata|Gemini Menjelaskan semuanya mulai konsep dengan contoh kasus nyata| saya jadi memahami konsepnya

### Bukti Diskusi
![](../tugas-07-konsistensi-data/bukti/Pembahasan%20tgl%2017.png)

### Bukti Simulasi 
![](../tugas-07-konsistensi-data/bukti/Bukti%20Simulasi.png)