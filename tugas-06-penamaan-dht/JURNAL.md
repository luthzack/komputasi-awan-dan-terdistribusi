# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): waktu mau implementasi fungsi find_successor program sempat error AttributeError: 'ChordRing' object has no attribute 'lookup'
- Cara memperbaikinya: indentasinya kurang maju dikit hehe

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: 

### Sebelum gabung:
id_kurir 132 bergabung dengan id_node 136, 
id_kurir 50 bergabung dengan id_node 102,
id_kurir 28 bergabung dengan id_noed 40.
![](../tugas-06-penamaan-dht/bukti/Sebelum%20Gabung.png)
### Sesudah gabung:
Tidak ada yang berubah karena tidak ada id_kurir yang nilainya lebih kecil atau sama dengan id_node. 
(id_kurir 132 tetap dengan id_node 136,
id_kurir 50 tetap dengan id_node 102).
![](../tugas-06-penamaan-dht/bukti/Setelah%20Bergabung.png)


### Sebelum keluar
id_kurir 132 bergabung dengan id_node 136, 
id_kurir 50 bergabung dengan id_node 102,
id_kurir 28 bergabung dengan id_noed 40.
![](../tugas-06-penamaan-dht/bukti/Sebelum%20Gabung.png)

# Sesudah keluar
Kondisi original skeleton. Node Jakarta 1 keluar dan tidak ada pengaruh apapun karena node ini tidak memegang data apapun, sehingga tidak ada perpindahan data
![](../tugas-06-penamaan-dht/bukti/Keluar%201.png)
Kondisi dimana node pemegang data keluar ring. Node Bandung 1 keluar maka id_kurir 28yang awalnya di bandung pindah ke id node 102.
![](../tugas-06-penamaan-dht/bukti/Keluar%202.png)

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 23-10-2026 | Gemini | Jelaskan konsep dari Chord DHT mulai dari penjelasan cara kerja, ada aturan apa aja, dan perbedaan node server dan node data | Gemini menjelaskan konsep dht itu peletekan server yang berurutan gitu hubungannya dan melingkar. ada aturan wrap around yang hubungan servernya itu selalu ke depan gabisa kebelakang untuk tanggung jawab memegang datannya dan pemindahan data itu ke server mana/node mana | paham alur kerja dari CHORD DHT ini dan dimanfaatkan untuk merancang kodenya |
| 25-10-2026 | Deepseek  | (mengirimkan screenshoot eror) ini kenapa saat aku running kok eror ya padahal seharusnya udah bener loh  | Ai sempat memberikan saran untuk mengubah code bagian todo 8, dan udah dicoba tetep eror lalu dia meminta screenshootkan codenya dan dia kasih tau bahwa indentasi pada todo 8 perlu diperbaiki | menekan TAB untuk menambahkan spasi agar indentasinya benar |


## Bukti diskusi
Diskusi awal (Pemahaman tugas dan pembagian)
![](../tugas-06-penamaan-dht/bukti/Diskusi%20Awal%20Pembagian%20tugas.png)
![](../tugas-06-penamaan-dht/bukti/Hasil%20diskusi%2025%20oktober.png)
