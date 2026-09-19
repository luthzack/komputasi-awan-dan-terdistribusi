# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [17 September 2026]
- Peserta: Ro'yul dan Luthfi
- Poin diskusi: 
  1.Memahami case yang diberikan,
  2.Mendiskusikan apakah laporan case ini "im menemukan bahwa kode mereka menulis asumsi seperti `# network is always reliable, no need for retry` dan tidak ada *timeout* sama sekali pada pemanggilan antar service" itu ada 2 atau 1 pitfall, kami sepakat ada 2
- Perbedaan pendapat (jika ada): 
  1.Pada poin 2 awalnya luthfi berpikir hanya ada 1 pitfall dalam 1 kalimat penuh namun setelah ro'yul lihat sepertinya lebih dari 1

## [18 September 2026]
- Peserta: Ro'yul dan Luthfi 
- Poin diskusi: Apakah Pitfall disini hanya yang ada pada daftar *Fallacies of Distributed Computing* atau boleh diluar dari daftar disitu, akhirnya kami sepakat bahwa boleh diluar itu karena ada tulisan **DAN/ATAU** Masalah desain
- Perbedaan pendapat (jika ada): -

## Review Silang
- [luthfi] mengomentari analisis [ro'yul]: garis besarnya pitfall yang diambil hampir mirip antara network is realible sama latency is zero.
- [Ro'yul] Mengomentari analisis [Luthfi]: Pada nomor 1 tradeoff nya tidak jelas ditunjukkan kesiapa awalmya dan bukan ke FoodGo.
- [Ro'yul] Mengomentari analisis [Luthfi]: Pada nomor 3 Bagian "Kenapa ini keliru" dan "Dampak Ke FoodGo" itu kalimatnya agak kurang jelas mengarah crash/error ke bagian mananya.  
- [luthfi] mengomentari analisis [ro'yul]: pedapat pribadi untuk waktu peberian timeout pada pitfall 2 mungki aga terlalu lama jika 10 detik jadi mungkin bisa direndahin dikit mas, 5 detik mungkin?
## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17 September 2026 | Claude Sonnet | Pada tugas tersebut, jelaskan apa goals utama yang diinginkan oleh tugas tanpa memberi tahu saya jawabannya, namun berikan poin-poin penting yang dapat saya perhatikan dalam mengerjakan tugas ini. | Claude membantu saya (Luthfi) dalam memahami soal dan pitfall-pitfall utama. | Tidak ada, karena hanya digunakan untuk memahami tujuan dan poin-poin penting dari tugas. | 
| 17 September 2026 | ChatGPT | Coba jelaskan apa itu secara singkat konsep dari 8 fallacies of distributed computing | GPT memberikan saya penjelasan untuk setiap 8 fallacies secara singkat bagaimana konsepnya | Saya melihat bahwa latency is zero konsepnya cocok dengan laporan pengujian tim FoodGo bagian "tidak ada timeout sama sekali pada bagian service" sedangkan di laporan lain ada timeout yang berarti kode bagian service itu aneh
| 18 September 2026 | DeepSeek | Layered, SOA, Peer-to-Peer, Publish-Subscribe, dari 4 arsitektur jaringan ini coba jelaskan dan berikan contoh penerapannya | Ai memberikan penjelasan untuk 4 arsitektur yang saya minta (contoh: Layered itu sistem dibagi menjadi beberapa bagian dan tidak bisa menghubungi layer  yang tidak bersebelahan dengan layer itu sendiri) | Disini saya melihat ada poin pemecahan sistem menjadi sebuah service terpisah pada penjelasan AI bagian SOA (Service-Oriented Architcture), dan ini akan menjadi sebuah arsitektur yang cocok untuk case FoodGo selain itu saya melihat contoh di README.md yang mengatakan pemisahan modul service dan itu terlihar seperti konsep dari SOA.
