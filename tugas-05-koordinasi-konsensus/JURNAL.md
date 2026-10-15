# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-4: **Kendala terjadi di TODO 4**

**todo 4**: ada sedikit terkendala dengan logika saat run, yang dimana permasalah tersebut menyebabkan saat node 4 dibunuh node 3 2 dan 1 tidak ada respon dan tidak melakukan election ulang untuk menjadi leader.

 Ada kode yang tidak di deklarasikan di def init sehingga menyebabkan hasil yang terlihat error (kalau di C++ atau GO jika ada variabel yang tidak didefinisikan tapi digunakan nanti tidak bisa di compile, kalau di python kode jalan dulu kalau emang kesalahannya itu tidak fatal tapi pasti ada pengaruhnya seperti di kasus ini), kemudian terjadinya 2 kali pemanggilan fungsi ELECTION (di bagian monitor_leader pengecekan awal (cek status diri sendiri) dan pengecekan kedua yang digunakan untuk PING ke node leader) yang menyebabkan proses election tertimpa. Solusinya adalah cukup menghapus variabel yang tidak dideklarasikan dan menambahkan kondisi pengecekan pertama (cek apakah node leader itu ada dan apakah node itu sendiri adalah node leader) 


## Skenario 1: Start normal
- Leader yang terpilih: Node 5
- Log/observasi: Disini konsepnya saya menyalakan/menjalankan terminal itu dari node 1 sampai 5 secara berurutan. dan setiap node dengan ID lebih tinggi itu di summon/aktifkan maka dia akan langsung melakukan election ke node lebih tinggi (misal node 1 sudah aktif kemudian node 2 diaktifkan maka dia akan langsun kirim election untuk cek balasan dari node ID lebih tinggi, konsep ini berjalan sampai ke node ID tertinggi disini 5), nah setelah menjadi `Node Leader` node lain akan aktif untuk mengirim `PING` setiap 3 detik untuk cek apakah `Node Leader (5)` masih hidup.
![](../tugas-05-koordinasi-konsensus/bukti/Bukti%20skenario%201.png)
**Kotak Hijau:** Menunjukkan kalau setiap node pernah melakukan election karena saya aktifkannya itu berurutan dari node 1 sampai node 5.
**Kotak Biru:** Menunjukkan kalau Node 5 adalah `Node Leader`
**Kotak Kuning:** Mendukung pernyataan dari Kotak biru kalau node 5 adalah `Node Leader` dimana mereka menerima pesan kalau node 5 adalah Leadernya
**Kotak Merah:** Mendukung pernyataan kotak biru dimana node 5 itu menerima PING dari node lain yang menunjukkan kalau dia adalah node Leader 

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: leader dengan node id paling tinggi misal node 5 jadi leader lalu dimatikan leader setelahnya adalah node 4 begitu seterusnya node 4 dimatikan 3 menjadi leader
- Berapa lama waktu sampai leader baru terdeteksi: 2.0 detik pada saat node sebelumnya melakukan ping dan tidak ada respond dari leader sebelumnya dan melakukan election dengan memilih leader dengan id paling tinggi
![](../tugas-05-koordinasi-konsensus/bukti/bukti%20saat%20melakukan%20percobaan%20dan%20saat%20leadernya%20dimatikan%20satu%20persatu.png)

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 14/10/2026 | Gemini | Apakah Algoritma Bully itu hanya ada 1 jenis atau ada banyak seperti algoritma searching, kalau ada banyak sebutkan jenisnya dan mekanismenya masing-masing | Ternyata yang jadi pusat itu election algoritma bukan bullynya, bully algorithm itu ada 3 jenis setelah optimasi (Klasik, modified dan fast) kemudian ada jenis algoritma election lainnya yaitu ring algorithm, raft election, paxos-based-election. | karena di tugas ini hanya memberikan 2 opsi (Bully dan Raft) dan secara spesifik disuruh menggunakan bully algorithm maka saya hanya fokus pada penjelasan mekanisme kedua algoritma itu untuk dibandingkan dan dianalisis lebih lanjut kemudian dituliskan ke README |
| 15/10/2026| claude | pada saat mematikan node 5 sebagai leader node 4 langusng election dan melakukan deklarasi menjadi leader namun kenapa saat node 4 dimatikan node 3 2 1 tidak ada respond? | claude mencarankan untuk cek lagi logika code pada todo 4 dan menyarankan untuk menghapus code logic yang tidak diperlukan | setelah dilihat ulang untuk bagian monitor_leader/todo 4, ternyata di kodenya ada variabel yang tujuannya untuk mengecek diri sendiri malah melakukan election sehingga terjadi 2 kali election dalam 1 kali pengecekan di monitor leader dan menyebabkan error selain itu ada variabel yang tidak didefiisikan di def init, hal ini juga yang menyebabkan terjadi error (kalau di C++ atau GO jika ada variabel yang tidak didefinisikan tapi digunakan nanti tidak bisa di compile, kalau di python kode jalan dulu kalau emang kesalahannya itu tidak fatal tapi pasti ada pengaruhnya seperti di kasus ini)


## Bukti Diskusi
Diskusi awal dan pembagian tugas
![](../tugas-05-koordinasi-konsensus/bukti/bukti%20saat%20awal%20brainstroming%20dan%20pembagian%20tugas%20ebelum%20pengerjaan.png)

Bahas pengerjaan todo dan error
![](../tugas-05-koordinasi-konsensus/bukti/Bukti%20Diskusi%20setelah%20mengerjakan%20todo%20masing-masing%20&%20bahas%20error.jpeg)