"""
Tugas 6 - Simulasi Chord DHT (single-process, tanpa jaringan sungguhan)

Fungsi hashing & struktur data ring sudah disediakan.
Lengkapi TODO untuk lookup(), join(), dan leave().
"""

import hashlib

M_BITS = 8               # ruang identifier 0..255 (disederhanakan dari Chord asli yang pakai 160-bit)
RING_SIZE = 2 ** M_BITS


def hash_id(key: str) -> int:
    """Hash string (ID node atau ID kurir) ke ruang identifier 0..RING_SIZE-1."""
    digest = hashlib.sha1(key.encode()).digest()
    return int.from_bytes(digest, "big") % RING_SIZE


class ChordRing:
    def __init__(self):
        # node_id (hasil hash) -> alamat IP node tersebut
        self.nodes: dict[int, str] = {}
        # key kurir (hasil hash) -> IP kurir yang disimpan node yang bertanggung jawab
        self.data: dict[int, tuple[str, str]] = {}  # hash -> (kurir_id, ip_kurir)

    def join(self, node_name: str, node_ip: str):
        """Tambahkan node baru ke ring. Pindahkan data yang seharusnya
        menjadi tanggung jawab node baru ini dari successor lamanya."""
        node_id = hash_id(node_name)

        # TODO 1: tambahkan node_id -> node_ip ke self.nodes.
        # TODO 2: cari successor LAMA dari node_id ini (successor sebelum node
        # baru bergabung, gunakan find_successor() dengan node_id INI dikecualikan
        # dulu dari self.nodes saat mencari).
        # TODO 3: pindahkan semua key di self.data yang seharusnya menjadi
        # tanggung jawab node baru (key dengan hash <= node_id, tapi masih
        # dipegang oleh successor lama) ke bawah tanggung jawab node baru.
        # (Untuk simulasi sederhana, cukup print log siapa mengambil alih apa -
        # tidak perlu benar-benar memindahkan struktur data kompleks.)
        print(f"[TODO] Node '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")

    def leave(self, node_name: str):
        """Keluarkan sebuah node dari ring. Data yang dipegangnya harus
        berpindah ke successor-nya."""
        node_id = hash_id(node_name)

        # TODO 4: hapus node_id dari self.nodes.
        # TODO 5: cari successor BARU untuk tiap key yang tadinya dipegang
        # node ini, pindahkan ke successor tersebut.
        print(f"[TODO] Node '{node_name}' (id={node_id}) keluar dari ring")

    def find_successor(self, key_hash: int) -> int:
        """Cari node_id dengan nilai hash TERKECIL yang >= key_hash
        (successor menurut aturan Chord). Jika tidak ada, wrap-around
        ke node dengan hash terkecil di ring (karena ring melingkar)."""
        # TODO 6: implementasikan logika successor di atas menggunakan
        # self.nodes.keys(). Kembalikan node_id (bukan IP).
        if not self.nodes:
            raise ValueError("Ring kosong: belum ada node")
        for node_id in sorted(self.nodes.keys()):
            if node_id >= key_hash:
                return node_id
        return min(self.nodes.keys())  # wrap-around
 
    def register_kurir(self, kurir_id: str, ip_kurir: str):
        """Simpan mapping ID Kurir -> IP di node yang bertanggung jawab."""
        key_hash = hash_id(kurir_id)
        # TODO 7: panggil find_successor(key_hash) untuk menentukan node
        # penanggung jawab, lalu simpan (kurir_id, ip_kurir) ke self.data[key_hash].
        node_id = self.find_successor(key_hash)
        self.data[key_hash] = (kurir_id, ip_kurir)
        print(f"[REGISTER] {kurir_id} (hash={key_hash}) -> {ip_kurir}, "
              f"disimpan di {self._label(node_id)}")
 
    def lookup(self, kurir_id: str) -> str | None:
        """Cari alamat IP terkini untuk sebuah ID Kurir."""
        key_hash = hash_id(kurir_id)
        # TODO 8: gunakan find_successor(key_hash) untuk menemukan node
        # penanggung jawab, lalu kembalikan ip_kurir dari self.data jika ada.
        if not self.nodes:
            return None
        node_id = self.find_successor(key_hash)
        entry = self.data.get(key_hash)
        print(f"  (lookup {kurir_id}: hash={key_hash} -> node penanggung jawab "
              f"{self._label(node_id)})")
        if entry is not None and entry[0] == kurir_id:
            return entry[1]
        return None
 
    def print_ring(self):
        """(tambahan) Cetak isi ring berurutan + kurir yang dipegang tiap node."""
        print("  Isi ring (urut searah jarum jam):")
        for node_id in sorted(self.nodes):
            kurir = [f"{self.data[h][0]}(hash={h})" for h in sorted(self.data)
                     if self.find_successor(h) == node_id]
            print(f"    id={node_id:3d}  {self.names.get(node_id, '?'):16s} "
                  f"{self.nodes[node_id]:10s} memegang: {', '.join(kurir) or '-'}")
 
 
def main():
    ring = ChordRing()
 
    # Skenario awal: 4 node bergabung
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")
 
    # Daftarkan beberapa kurir
    ring.register_kurir("kurir-001", "192.168.1.10")
    ring.register_kurir("kurir-002", "192.168.1.11")
    ring.register_kurir("kurir-003", "192.168.1.12")
 
    print("\n--- Kondisi ring awal ---")
    ring.print_ring()
 
    print("\n--- Lookup sebelum perubahan topologi ---")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))
 
    print("\n--- Node baru bergabung ---")
    ring.join("node-medan-1", "10.0.0.5")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    ring.print_ring()
 
    print("\n--- Sebuah node keluar ---")
    ring.leave("node-jakarta-1")
    print("kurir-001 ->", ring.lookup("kurir-001"))
    print("kurir-002 ->", ring.lookup("kurir-002"))
    ring.print_ring()
 
    # --- Tambahan: skenario di atas kebetulan tidak memindahkan data apa pun
    # (node-medan-1 id=123 dan node-jakarta-1 id=177 tidak menjadi penanggung
    # jawab kurir manapun). Dua langkah berikut memperlihatkan perpindahan nyata.
    print("\n--- [Tambahan] Node baru yang mengambil alih data (join) ---")
    ring.join("node-semarang-1", "10.0.0.6")   # id=77, di antara hash 50 dan 102
    print("kurir-001 ->", ring.lookup("kurir-001"))
    ring.print_ring()
 
    print("\n--- [Tambahan] Node pemegang data keluar (leave) ---")
    ring.leave("node-bandung-1")               # id=40, memegang kurir-002
    print("kurir-002 ->", ring.lookup("kurir-002"))
    ring.print_ring()
 
 
if __name__ == "__main__":
    main() 