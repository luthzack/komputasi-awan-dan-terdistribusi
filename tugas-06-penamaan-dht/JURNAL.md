# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): waktu mau implementasi fungsi find_successor program sempat error AttributeError: 'ChordRing' object has no attribute 'lookup'
- Cara memperbaikinya: indentasinya kurang maju dikit hehe

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: 

# Sebelum gabung:
kurir-001 -> 192.168.1.10
kurir-002 -> 192.168.1.11
# sesudah gabung:
[JOIN] Node 'node-medan-1' (id=45) bergabung, alamat 10.0.0.5
kurir-001 -> 192.168.1.10
- Hasil sebelum & sesudah node keluar: 

# sebelum
kurir-001 -> 192.168.1.10
kurir-002 -> 192.168.1.11

# sesudah
[LEAVE] Node 'node-jakarta-1' (id=177) keluar dari ring
[PINDAH DATA] Kurir 'kurir-001' (hash=50) dipindahkan ke node 102
[PINDAH DATA] Kurir 'kurir-002' (hash=28) dipindahkan ke node 40
[PINDAH DATA] Kurir 'kurir-003' (hash=132) dipindahkan ke node 136
kurir-001 -> 192.168.1.10
kurir-002 -> 192.168.1.11

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 23-10-2026 | Gemini | Jelaskan konsep dari Chord DHT mulai dari penjelasan cara kerja, ada aturan apa aja, dan perbedaan node server dan node data | Gemini menjelaskan konsep dht itu peletekan server yang berurutan gitu hubungannya dan melingkar. ada aturan wrap around yang hubungan servernya itu selalu ke depan gabisa kebelakang untuk tanggung jawab memegang datannya dan pemindahan data itu ke server mana/node mana | paham alur kerja dari CHORD DHT ini dan dimanfaatkan untuk merancang kodenya |
| 25-10-2026 | Deepseek  | (mengirimkan screenshoot eror) ini kenapa saat aku running kok eror ya padahal seharusnya udah bener loh  | Ai sempat memberikan saran untuk mengubah code bagian todo 8, dan udah dicoba tetep eror lalu dia meminta screenshootkan codenya dan dia kasih tau bahwa indentasi pada todo 8 perlu diperbaiki | menekan TAB untuk menambahkan spasi agar indentasinya benar |


## Bukti diskusi
Diskusi awal (Pemahaman tugas dan pembagian)
![](../tugas-06-penamaan-dht/bukti/Diskusi%20Awal%20Pembagian%20tugas.png)

