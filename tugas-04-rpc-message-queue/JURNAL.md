# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- MQ, alasannya: Message Queue(MQ) adalah sistem antrian pesan yang menghubungkan 2 modul secara asinkron dan persisten. kami memilih MQ karena sesuai dengan kebutuhan FoodGo dimana saat modul pembayaran mengirim pesan ke modul Notifikasi_kurir, Modul pembayaran ini tidak boleh menunggu modul Notifikasi_kurir untuk membalas. Dengan MQ modul pembayaran tetap lancar dan tidak perlu menunggu modul Notifikasi_kurir membalas pesan, sedangkan pesan notifikasi untuk kurir tersimpan aman di antrean RabbitMQ meski kurir sedang tidak aktif.

## Kendala teknis
- Error Saat Mengunduh Library pika, setelah diselidiki ternyata pika terinstall di evironment lain sehingga solusinya adalah mengganti ke interpreter python yang sudah terunduh library pika didalamnya.

## Uji "pesan tidak hilang" (khusus Jalur B)
- **Langkah uji: matikan consumer → jalankan publisher beberapa kali → nyalakan consumer**
- **Hasil yang diamati:** 

Saat Consumer dimatikan dan publisher dijalankan beberapa kali (disini kami memutuskan menjalankan sebanyak 3 kali dengan total ada 9 pesan), pesan pembayaran tidak hilang dan modul pembayaran tidak mengalami eror. Pesan-pesan tersebut disimpan oleh RabbitMQ di antrian `pembayaran_berhasil`(kalau di dashboard ada tulisan **ready** dan **total** dan ada aktivitas **Disk Write** yang artinya menuliskan pesan yang belum tersampaikan ke consumer di disk server karena bersifakt persisten, dikonteks ini penyimpanan laptop saya). 

Ketika `consumer.py` dinyalakan kembali, terjadi aktivitas **Disk Read** di mana RabbitMQ membaca kembali data pesan yang sebelumnya tersimpan di disk, lalu mengirimkannya ke consumer melalui proses **Deliver (manual ack)**. disini **manual ack** maksudnya adalah memastikan bahwa pesan tidak langsung dihapus oleh broker saat dikirim, tapi menunggu konfirmasi dari consumer. Setelah consumer selesai menerima seluruh pesan, consumer mengirimkan konfirmasi **(Consumer ack)** ke RabbitMQ. Barulah setelah konfirmasi diterima, antrean di dashboard kembali menjadi 0 di akhir proses dan seluruh 9 transaksi berhasil diproses tanpa ada data yang hilang.

**Jadi Alurnya adalah:**
**Publisher jalan (Consumer mati) >>> terjadi Publish & Disk Write:** Pesan ditulis dan disimpan aman di penyimpanan disk antrean.
**Consumer dinyalakan >>> Disk Read & Deliver (manual ack):** RabbitMQ membaca pesan dari disk (Disk Read) lalu mengirimkannya (Deliver) dengan metode menunggu konfirmasi manual agar pesan tidak hilang di jalan jika consumer tiba-tiba mati.
**Consumer selesai proses → Consumer ack:** Consumer mengirim konfirmasi balik (ack), antrean di RabbitMQ baru dihapus/kembali jadi 0.

#### Menjawab pertanyaan "ke mana pesan "hilang sementara" tersimpan saat consumer mati (Jalur B) "
Pesan `hilang sementara` tersimpan di dalam antrean **pembayaran_berhasil** pada broker RabbitMQ, berstatus Ready di memori dan ditulis secara persisten ke hard disk (terbukti dari grafik Disk Write)

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 10-11-2026 | Gemini | Di dashboard rabbitmq ada tulisan Publish, Deliver (Manual ack), Consumer ack, Disk Read, Disk Write itu gunanya apa  | AI menjawab masing-masing kegunaan dari hal yang kusebut misal Consumer Ack yang mengirim konfirmasi ke rabbitMq bahwa pesan sudah diterima dan dapat menghapus dari antrian | tulisan diolah menjadi kalimat analisis dan bertambahnya pengetahuan saya  |
|10-10-2026|Chatgpt|Saya diberikan sebuah tugas yang dimana berkaitan dengan materi Remote Procedure Call (RPC), Message-Oriented Middleware (MOM)/Message Queue. Saya berkelompok dua orang berikan saya pilihan terbaik dan mudah untuk dikerjakan minimal satu. Pilihan : MQ(message Queue) dan RPC| chatgpt menyarankan menggunakan jalur MQ| menambahkan code yang kurang lengkap pada TODO 1 2 3 4 consumer maupun publisher|


## Bukti Diskusi
![](bukti/Bukti%20Diskusi.jpeg)

## Dashboard Awal RabbitMQ
![](bukti/Dashboard%20RabbitMq.png)
## Bukti Test Awal Sesuai skeleton Jalur B
![](bukti/Test%20Awalan%201.0.png)
![](bukti/Test%20Awalan%201.1.png)
## Bukti Tugas Jalur B (Pesan tetap di proses)
bukti saat publisher dijalankan beberapa kali, pesan tertahan dilihat pada total(9)
![](bukti/Dashboard%20Bukti%20Tugas%20V1.jpeg)
bukti pada dashboard utama (ada total dan nilainya 9)
![](bukti/Dashboard%20Bukti%20Tugas%20V1.1.jpeg)
bukti saat consumer dinyalakan
![](bukti/Dashboard%20Bukti%20Tugas%20.jpeg)
terminal
![](bukti/Terminal%20Bukti%20Tugas.png)
