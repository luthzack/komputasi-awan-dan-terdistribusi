# Jurnal Proses — Tugas 2

## 25 September 2026
- Opsi arsitektur yang dipertimbangkan: SOA
- Kenapa akhirnya pilih [SOA]: Karena ditugas satu kami hanya memilih SOA, selain itu menurut kami mengkombinasikan SOA dan Pub-Sub akan meningkatkan kompleksitasnya menjadi lebih tinggi untuk tim FoodGo, karena itu SOA untuk sekarang sudah cukup menurut kami 

## 27 September 2026
- Review Silang: [Ro'yul] Mengomentari [Luthfi]: ada kalimat yang kurang tepat untuk menjelaskan alur diagramnya, jadi dibetulkan bersama didiscord (bukti ada di bawah) sekaligus membahas analisis trade-off


## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 25/09/2026 | ChatGPT | Jelaskan padaku dalam arsitektur SOA dan Publish-Subscribe itu ada apa aja komponen didalamnya kalau aku mau gambar diagram arsitekturnya dan jelaskan perbedaan komunikasi secara sinkron dan asinkron  | AI memberikan ada komponen seperti message broker, ESB, Service Registry Dll. Untuk sinkron dan asinkron singkatnya, sinkron itu komunikasi yang menunggu sedangkan asinkron komunikasi yang tidak perlu menunggu  | Saya berpikir bahwa SOA saja sudah cukup untuk FoodGo saat ini agar tidak menambah kesulitan dalam pengembangannya jadi pada diagram hanya memanfaatkan API gateway (tidak pakai message broker yang sepaham saya itu adalah komponen dari Pub-Sub) |


## Bukti Diskusi
![](../tugas-02-perancangan-arsitektur/diagram/Bukti%20Diskusi%202.1.png)