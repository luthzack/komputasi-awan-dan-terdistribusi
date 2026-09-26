# Jurnal Proses — Tugas 2

## [Tanggal]
- Opsi arsitektur yang dipertimbangkan: ...
- Kenapa akhirnya pilih [SOA/Pub-Sub]: ...
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 25/09/2026 | ChatGPT | Jelaskan padaku dalam arsitektur SOA dan Publish-Subscribe itu ada apa aja komponen didalamnya kalau aku mau gambar diagram arsitekturnya dan jelaskan perbedaan komunikasi secara sinkron dan asinkron  | AI memberikan ada komponen seperti message broker, ESB, Service Registry Dll. Untuk sinkron dan asinkron singkatnya, sinkron itu komunikasi yang menunggu sedangkan asinkron komunikasi yang tidak perlu menunggu  | Saya berpikir bahwa SOA saja sudah cukup untuk FoodGo saat ini agar tidak menambah kesulitan dalam pengembangannya jadi pada diagram hanya memanfaatkan API gateway (tidak pakai message broker yang sepaham saya itu adalah komponen dari Pub-Sub) |
