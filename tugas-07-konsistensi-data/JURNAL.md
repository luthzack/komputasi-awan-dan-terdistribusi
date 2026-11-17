# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan:  Royul kekeh dengan Sequential Consistency lebih tepat karena semua replika perlu melihat urutan operasi yang sama agar data saldo tidak berbedan nah aku(luthfi) memberikan saran menggunakan Read-Your-Writes sebagai solusi supaya pelanggan tetap dapat melihat saldo terbaru setelah melakukan top-up.
- Kesimpulan akhir & alasan: Kami memutuskan menggunakan Eventual Consistency yang dilengkapi Read-Your-Writes. karena proses replikasi tetap dapat berjalan secara bertahap, tetapi pelanggan tidak akan membaca perubahan saldo miliknya yang masih tertinggal.

## Simulasi (jika dikerjakan)
- Hasil skenario naif vs Read-Your-Writes: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17-11-2206 | gpt | berikan aku bantuan memahami penerapan Read-Your-Writes Consistency sebagai solusi terhadap masalah keterlambatan replikasi data. | memberikan penjelasan | dipahami dan dijelaskan lebih mendetail |
