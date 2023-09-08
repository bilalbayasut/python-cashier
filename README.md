# Flowchart

graph LR
A[Customer memasukkan ID transaksi] --> B[Customer memasukkan nama item, jumlah item, dan harga barang]
B --> C{Apakah customer ingin menambahkan item lagi?}
C -- Tidak --> D[Customer ingin memeriksa/menambah/mengubah pesanan]
D --> E{Apakah data pesanan sudah benar?}
E -- Ya --> F[Menampilkan pesanan yang sudah dibeli]
E -- Tidak --> D
D --> G{Apakah customer ingin menghitung total harga?}
G -- Ya --> H[Menampilkan total harga sebelum diskon]
G -- Tidak --> D
H --> I[Menampilkan total harga setelah diskon]
I --> J{Apakah customer ingin mereset transaksi?}
J -- Ya --> K[Terima kasih]
J -- Tidak --> D
C -- Iya --> B