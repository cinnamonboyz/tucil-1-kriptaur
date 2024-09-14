# Ragam Cipher Klasik
## II4031 Kriptografi dan Koding
- 18220012 Fikri Muhammad Fahreza
- 18220086 Aldi Fadlian Sunan

# 🔍 Introduction 
Program ini merupakan program ragam cipher klasik yang dapat dijalankan dengan GUI.
Ragam cipher yang berhasil diimplementasikan pada program ini yaitu:
1. Vigenere Cipher (26 huruf alfabet)
2. Extended Vigenere Cipher (256 karakter ASCII)
3. Playfair Cipher (26 huruf alfabet)
4. One-time pad Cipher (26 huruf alfabet)
5. Enigma Cipher (3 rotor, 26 huruf alfabet)

# 👨‍💻Specifications
- Program dapat menerima pesan berupa file sembarang (file text maupun file biner) atau pesan yang diketikkan dari papan-ketik.
- Program dapat mengenkripsi plainteks. Khusus untuk Vigenere Cipher dengan 26 huruf alfabet, Playfair Cipher dengan 26 huruf alfabet, dan One-time pad dengan 26 huruf alfabet, program hanya mengenkripsi karakter alfabet saja. Angka, spasi, dan tanda baca lainnya diabaikan dan dibuang saat cipherteks ditampilkan atau disimpan.
- Untuk One-time pad, kunci dibaca dari file teks yang berisi huruf-huruf yang dibangkitkan secara acak. Jumlah huruf di dalam file kunci sebaiknya banyak (misalnya puluhan ribu huruf). Huruf-huruf kunci yang digunakan adalah sepanjang karakter di dalam pesan, sisa huruf yang tidak terpakai dibiarkan begitu saja.
- Program dapat mendekripsi cipherteks menjadi plainteks semula.
- Untuk pesan berupa text, program dapat menampilkan plainteks dan cipherteks di layar. Cipherteks dapat ditampilkan dalam dua cara: (a) tanpa spasi, (b) kelompok 5-huruf.
- Program dapat menyimpan cipherteks ke dalam file.
- Kunci dimasukkan oleh pengguna. Panjang kunci bebas.
- Untuk enkripsi plainteks sembarang file (khusus untuk extended Vigenere Cipher), setiap file diperlakukan sebagai file of bytes. Program membaca setiap byte di dalam file (termasuk byte-byte header file) dan mengenkripsinya. Hanya saja file yang sudah terenkripsi tidak bisa dibuka oleh program aplikasinya karena header file ikut terenkripsi. Namun dengan mendekripsinya kembali maka file tersbut dapat dibuka oleh aplikasinya.

# 💻How to Run This Program?
1. Clone repositori ini
2. Buka file main.py
3. Jalankan dengan mengetikkan uvicorn main:app di terminal
4. Akses IP Adress yang muncul
5. Pilih dan eksplorasi ragam cipher yang ingin dicoba pada program
