# Tugas 10 (Pekan 10) – Arsitektur Cloud yang Skalabel

**Materi terkait:** Workload Distribution, Resource Pooling, Dynamic/Horizontal/Vertical Scalability, Load Balancing.

## Studi Kasus

Situs web tiket konser "TicketGo" **mogok total** karena tidak mampu menangani lonjakan **1 juta pengguna dalam 1 menit** saat penjualan tiket dibuka (fenomena *thundering herd*). Server tunggal mereka kehabisan koneksi dan CPU 100% dalam hitungan detik.

## Tugas Kelompok

Simulasikan (di laptop, memakai Docker Compose) sebuah arsitektur dengan **Load Balancer** di depan **beberapa instance aplikasi identik**, lalu buktikan dengan load test sederhana bahwa distribusi beban benar-benar terjadi.

### Yang Sudah Disediakan

- `app/app.py` – skeleton server HTTP super sederhana yang mengembalikan ID instance-nya sendiri (supaya kalian bisa melihat request mana ditangani instance mana).
- `nginx/nginx.conf` – skeleton konfigurasi Nginx sebagai Load Balancer, dengan 3 backend (`app1`, `app2`, `app3`).
- `docker-compose.yml` – skeleton yang menjalankan 3 instance `app` + 1 `nginx` sebagai LB.
- `load_test.py` – skeleton script pengirim request konkuren untuk menguji distribusi beban.

### Langkah Kerja

1. Lengkapi `# TODO` di `app/app.py` (kembalikan `INSTANCE_ID` dari environment variable di response).
2. Lengkapi `# TODO` di `nginx/nginx.conf` (buat `upstream` block berisi 3 backend, gunakan di `proxy_pass`).
3. Jalankan:
   ```bash
   docker compose up --build
