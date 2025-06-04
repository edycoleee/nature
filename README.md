### BELAJAR NATURE OF CODE WITH PYTHON

### GITHUB

```git
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/edycoleee/nature.git
git push -u origin main
```

## 1. PERSIAPAN

```py
#project-folder/
#│
#├── nature.ipynb.py
#└── README.md

# 1. Membuat Virtual Environtment
python -m venv venv
source venv/bin/activate  #Linux / Macbook
venv\Scripts\activate # Windows

#2. Install Flask
pip install perlin-noise pillow matplotlib numpy
```

📦 1. VARIABEL
Paham bahwa variabel menyimpan nilai yang bisa berubah, seperti kecepatan, posisi, warna.

```py
x = 10  # posisi horizontal
speed = 5  # kecepatan ke kanan

print(x + speed)  # hasilnya 15
```

🧒 Penjelasan:
"Bayangkan kamu punya kotak bernama x yang isinya 10. Lalu kamu punya speed yang isinya 5. Kalau kamu tambahkan, hasilnya 15."

- DICT, LIST, TUPLE

```py
#dict di Python = object di JavaScript
user = {
    "nama": "Andi",
    "usia": 25
}
print(user["nama"])  # Output: Andi

#tuple di Python ≈ array dengan const di JavaScript
#array (tidak diubah)
lokasi = ("Jakarta", -6.2)
print(lokasi[0])  # Output: Jakarta

#Contoh list (mutable)
#array (bisa diubah)
buah = ["apel", "jeruk", "pisang"]
buah[0] = "mangga"           # Bisa diubah
buah.append("anggur")        # Bisa ditambah
print(buah)

```

- DICT, LIST, TUPLE

| Konsep Python | Bentuk             | Mirip JavaScript           |
| ------------- | ------------------ | -------------------------- |
| `dict`        | `{ "key": value }` | object literal             |
| `tuple`       | `("val1", "val2")` | const array (tidak diubah) |
| `list`        | `[ "a", "b" ]`     | array                      |

- List of Dict di Python

| Tujuan        | Python                       | JavaScript setara           |
| ------------- | ---------------------------- | --------------------------- |
| Tambah item   | `list.append(dict)`          | `array.push(object)`        |
| Ubah isi dict | `list[i]["key"] = new_value` | `array[i].key = new_value`  |
| Loop          | `for item in list:`          | `for (const item of array)` |

- Kenapa Class Lebih Baik?

| Fitur                     | List of Dict            | List of Object (Class)        |
| ------------------------- | ----------------------- | ----------------------------- |
| Struktur konsisten        | ❌ Bisa tidak beraturan | ✅ Terjamin oleh `__init__()` |
| Bisa punya method         | ❌ Tidak                | ✅ Bisa (`tampilkan()`, dll)  |
| Validasi / aturan atribut | ❌ Tidak bisa           | ✅ Bisa diatur di dalam class |

- Perbedaan self dan super()

| Fungsi    | Artinya                                                                   |
| --------- | ------------------------------------------------------------------------- |
| `self`    | menunjuk ke objek itu sendiri                                             |
| `super()` | menunjuk ke **kelas induk (parent)**, berguna saat kita extend kelas lain |

- Fungsi dengan \*args dan \*\*kwargs

| Fitur        | Penjelasan                                  |
| ------------ | ------------------------------------------- |
| `*args`      | Menangkap banyak argumen biasa (tuple)      |
| `**kwargs`   | Menangkap banyak argumen kunci-nilai (dict) |
| `return`     | Mengembalikan nilai dari fungsi             |
| Method class | Fungsi dalam class, selalu punya `self`     |

- Rangkuman Fungsi Populer:

| Fungsi     | Kegunaan                         |
| ---------- | -------------------------------- |
| `max()`    | Ambil data dengan nilai terbesar |
| `min()`    | Ambil data dengan nilai terkecil |
| `sum()`    | Jumlahkan semua nilai            |
| `len()`    | Hitung jumlah item dalam list    |
| `sorted()` | Urutkan data                     |

- Operasi Aritmatika (Matematika)

  | Operator | Arti            | Contoh   | Hasil |
  | -------- | --------------- | -------- | ----- |
  | `+`      | Penjumlahan     | `5 + 2`  | `7`   |
  | `-`      | Pengurangan     | `5 - 2`  | `3`   |
  | `*`      | Perkalian       | `5 * 2`  | `10`  |
  | `/`      | Pembagian       | `5 / 2`  | `2.5` |
  | `//`     | Pembagian bulat | `5 // 2` | `2`   |
  | `%`      | Sisa bagi (mod) | `5 % 2`  | `1`   |
  | `**`     | Pangkat         | `2 ** 3` | `8`   |

- Assignment (Pengisian Nilai)

  | Bentuk    | Sama dengan  |
  | --------- | ------------ |
  | `x += 1`  | `x = x + 1`  |
  | `x -= 1`  | `x = x - 1`  |
  | `x *= 2`  | `x = x * 2`  |
  | `x /= 2`  | `x = x / 2`  |
  | `x //= 2` | `x = x // 2` |

- Operasi Logika (and, or, not)

| Operator | Arti                      | Contoh           | Hasil   |
| -------- | ------------------------- | ---------------- | ------- |
| `and`    | True jika keduanya True   | `True and False` | `False` |
| `or`     | True jika salah satu True | `True or False`  | `True`  |
| `not`    | Kebalikan                 | `not True`       | `False` |

- Operator Perbandingan

  | Operator | Arti             | Contoh   | Hasil   |
  | -------- | ---------------- | -------- | ------- |
  | `==`     | Sama dengan      | `3 == 3` | `True`  |
  | `!=`     | Tidak sama       | `3 != 4` | `True`  |
  | `>`      | Lebih dari       | `5 > 2`  | `True`  |
  | `<`      | Kurang dari      | `5 < 2`  | `False` |
  | `>=`     | Lebih atau sama  | `5 >= 5` | `True`  |
  | `<=`     | Kurang atau sama | `4 <= 5` | `True`  |

---

### ✅ Tabel Fungsi Dasar `canvas` Tkinter

| Fungsi             | Kegunaan                             | Sintaks Contoh                                               |
| ------------------ | ------------------------------------ | ------------------------------------------------------------ |
| `create_oval`      | Gambar lingkaran atau bola           | `canvas.create_oval(x1, y1, x2, y2, fill="red")`             |
| `create_rectangle` | Gambar persegi atau persegi panjang  | `canvas.create_rectangle(x1, y1, x2, y2, fill="blue")`       |
| `create_line`      | Gambar garis lurus                   | `canvas.create_line(x1, y1, x2, y2, fill="black")`           |
| `move`             | Menggerakkan objek ke arah tertentu  | `canvas.move(objek_id, dx, dy)`                              |
| `coords`           | Mengubah posisi/ukuran objek         | `canvas.coords(objek_id, x1, y1, x2, y2)`                    |
| `delete`           | Menghapus objek dari canvas          | `canvas.delete(objek_id)`                                    |
| `itemconfig`       | Mengubah warna, teks, dll dari objek | `canvas.itemconfig(objek_id, fill="green")`                  |
| `create_text`      | Menampilkan teks di canvas           | `canvas.create_text(x, y, text="Halo!", font=("Arial", 12))` |

---

### 📌 Penjelasan Tambahan

| Perintah         | Artinya                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| `x1, y1, x2, y2` | Koordinat kiri-atas dan kanan-bawah area gambar                        |
| `fill="warna"`   | Warna isi bentuk                                                       |
| `dx, dy`         | Jarak gerak di sumbu x dan y (misal `dx=5` artinya maju 5 pixel kanan) |
| `objek_id`       | Nomor ID objek yang diberikan oleh `canvas.create_*` saat membuat      |

---

### 🔍 Contoh Gabungan

```python
bola = canvas.create_oval(10, 50, 30, 70, fill="red")
canvas.move(bola, 5, 0)  # Bola digeser ke kanan 5px
canvas.coords(bola, 50, 50, 70, 70)  # Ubah posisi bola ke titik lain
canvas.itemconfig(bola, fill="blue")  # Ganti warna bola jadi biru
canvas.delete(bola)  # Hapus bola dari layar
```

---

Tentu! Mari kita bahas lebih lanjut perbedaan dan penggunaan `coords()` vs `move()` **secara sederhana**,

---

## 🟢 Inti Masalah: Gimana Caranya Menggerakkan Gambar di Tkinter?

Ketika kamu menggambar sesuatu di **Canvas** (seperti bola), kamu bisa **memindahkannya** dengan dua cara:

### 1. `canvas.coords(item, x1, y1, x2, y2)`

- Artinya: "Ubah posisi gambar jadi **tepat di sini**."
- Kamu harus tahu posisi **kiri atas (x1, y1)** dan **kanan bawah (x2, y2)**.
- Biasanya digunakan saat kamu tahu posisi pasti suatu objek.

### 2. `canvas.move(item, dx, dy)`

- Artinya: "Geser gambar sejauh `dx` ke kanan dan `dy` ke bawah."
- **Tidak perlu tahu posisi awal.**
- Cocok untuk gerakan **berkelanjutan** atau seperti "meluncur".

---

## 🔴 Perbandingan Sehari-hari

### Bayangkan kamu sedang bermain game mobil:

- `coords()` itu seperti **teleportasi**: langsung loncat ke lokasi tertentu.
- `move()` itu seperti **mengemudi**: pelan-pelan geser mobil ke kanan/kiri sesuai arah.

---

## 🟢 Dalam Kode Kamu

### Versi `coords()`:

```python
# Ganti seluruh posisi bola berdasarkan nilai mutlak (x, y)
self.canvas.coords(
    self.shape,
    self.position.x,
    self.position.y,
    self.position.x + self.radius*2,
    self.position.y + self.radius*2
)
```

> Kamu hitung posisi **lengkap** bola dari awal setiap kali.

---

### Versi `move()`:

```python
# Geser bola berdasarkan pergerakan (delta x, delta y)
self.canvas.move(self.shape, self.velocity.x, self.velocity.y)
```

> Kamu cukup bilang, “geser sejauh ini”, tanpa harus hitung ulang semua koordinatnya.

---

## 🟡 Kapan Gunakan yang Mana?

| Kondisi                                     | Gunakan     |
| ------------------------------------------- | ----------- |
| Kamu tahu posisi akhir objek                | `coords()`  |
| Kamu ingin menggeser perlahan atau dinamis  | `move()` ✅ |
| Kamu ingin animasi halus seperti bola jatuh | `move()` ✅ |
| Kamu ingin langsung loncat ke posisi X,Y    | `coords()`  |

---

## 💡 Kenapa `move()` Lebih Mudah

Karena kamu hanya perlu tahu:

> “Bola digeser sejauh berapa ke kanan dan ke bawah.”

Itu **lebih masuk akal** dibanding harus menghitung koordinat kiri atas dan kanan bawah setiap saat (seperti di `coords()`).

---

## 🧠 Penutup (Kesimpulan)

- `move()` = **gerakan relatif**, cocok untuk animasi, lebih mudah dipahami anak-anak.
- `coords()` = **gerakan absolut**, cocok kalau kamu ingin kontrol penuh atas posisi objek.
- Kode kamu akan lebih **sederhana dan ringan** kalau pakai `move()` untuk animasi seperti bola berjalan.

---

## 🔹 1. `@staticmethod`

```python
@staticmethod
def hitung_jarak(bola1, bola2):
    dx = bola1.position.x - bola2.position.x
    dy = bola1.position.y - bola2.position.y
    return (dx**2 + dy**2) ** 0.5
```

### 📌 Penjelasan:

- `@staticmethod` adalah **dekorator** di Python yang menunjukkan bahwa fungsi tersebut **tidak bergantung pada objek (tidak pakai `self`)**.
- Artinya, fungsi ini bisa dipanggil **langsung lewat nama class**, misalnya:

```python
Bola.hitung_jarak(bola1, bola2)
```

### 📦 Fungsi `hitung_jarak`:

- Tujuannya untuk menghitung **jarak antara dua bola** berdasarkan posisi vektor mereka.
- Rumusnya adalah **jarak Euclidean** (seperti di matematika):

$$
\text{jarak} = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
$$

- `dx` dan `dy` adalah selisih posisi `x` dan `y` dari dua bola:

  - `dx = bola1.position.x - bola2.position.x`
  - `dy = bola1.position.y - bola2.position.y`

- Kemudian `return (dx**2 + dy**2) ** 0.5` artinya **akar kuadrat dari penjumlahan kuadrat dx dan dy**.

---

## 🔹 2. `hasattr(self.canvas, 'bola2')`

```python
if self.nama == "bola1" and hasattr(self.canvas, 'bola2'):
```

### 📌 Penjelasan:

- `hasattr(objek, 'atribut')` digunakan untuk **mengecek apakah objek punya atribut tertentu**.

- Dalam hal ini:

  - `self.canvas` adalah objek canvas Tkinter.
  - `'bola2'` adalah atribut yang kita tambahkan manual ke canvas dengan:

    ```python
    canvas.bola2 = bola2
    ```

- Jadi, baris ini **mengecek apakah canvas memiliki atribut bernama `bola2`**. Jika **ya**, berarti kita boleh akses `canvas.bola2`.

### 🔍 Kenapa dicek dulu?

- Supaya program **tidak error** kalau `bola2` belum dibuat atau belum disimpan ke canvas.
- Kalau tidak dicek dan langsung diakses `canvas.bola2`, akan muncul error: `AttributeError: 'Canvas' object has no attribute 'bola2'`.

---

## 🔚 Kesimpulan

| Bagian                      | Fungsi/Penjelasan                                                            |
| --------------------------- | ---------------------------------------------------------------------------- |
| `@staticmethod`             | Fungsi yang **tidak akses `self`**, bisa dipanggil lewat class (umum/global) |
| `hitung_jarak(b1, b2)`      | Hitung jarak Euclidean antara posisi dua bola                                |
| `hasattr(self.canvas, ...)` | Mengecek apakah `canvas` punya atribut tertentu (`bola2`) sebelum digunakan  |

---

### Asal Usul Rumus Jarak antara Dua Koordinat

#### 1. **Teorema Pythagoras (Untuk Ruang 2D)**
   - **Asal Usul**: Teorema Pythagoras berasal dari matematikawan Yunani kuno, Pythagoras, yang menyatakan bahwa dalam segitiga siku-siku, kuadrat panjang sisi miring (hipotenusa) sama dengan jumlah kuadrat panjang kedua sisi lainnya.
   - **Rumus Jarak 2D**: Jika kita memiliki dua titik dalam bidang 2D, \( P_1 = (x_1, y_1) \) dan \( P_2 = (x_2, y_2) \), jarak antara keduanya dapat dihitung dengan:
     $$
     d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
     $$
     Ini berasal dari membayangkan segitiga siku-siku dengan kaki-kaki \( (x_2 - x_1) \) dan \( (y_2 - y_1) \).

#### 2. **Rumus Euclidean (Untuk Ruang n-D)**
   - **Asal Usul**: Rumus Euclidean adalah generalisasi dari teorema Pythagoras ke ruang berdimensi lebih tinggi (3D, 4D, dst.). Konsep ini dikembangkan dari geometri Euclidean, yang dinamai dari matematikawan Yunani Euclid.
   - **Rumus Jarak n-D**: Untuk dua titik dalam ruang n-dimensi, \( P_1 = (x_1, x_2, \dots, x_n) \) dan \( P_2 = (y_1, y_2, \dots, y_n) \), jarak Euclidean adalah:
     \[
     d = \sqrt{(y_1 - x_1)^2 + (y_2 - x_2)^2 + \dots + (y_n - x_n)^2}
     \]
   - Contoh 3D:
     \[
     d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
     \]

### Implementasi dalam Python
Berikut adalah contoh implementasi rumus jarak Euclidean dalam Python untuk 2D dan 3D, serta generalisasi untuk n-D:

#### 1. Jarak Euclidean 2D
```python
import math

def jarak_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Contoh penggunaan
titik1 = (1, 2)
titik2 = (4, 6)
print(jarak_2d(titik1[0], titik1[1], titik2[0], titik2[1]))  # Output: 5.0
```

#### 2. Jarak Euclidean 3D
```python
def jarak_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Contoh penggunaan
titik1_3d = (1, 2, 3)
titik2_3d = (4, 6, 9)
print(jarak_3d(*titik1_3d, *titik2_3d))  # Output: 7.0710678118654755
```

#### 3. Jarak Euclidean untuk n-D (Umum)
```python
def jarak_nd(titik1, titik2):
    if len(titik1) != len(titik2):
        raise ValueError("Dimensi titik tidak sama")
    total = sum((p2 - p1)**2 for p1, p2 in zip(titik1, titik2))
    return math.sqrt(total)

# Contoh penggunaan
titik1_nd = (1, 2, 3, 4)
titik2_nd = (5, 6, 7, 8)
print(jarak_nd(titik1_nd, titik2_nd))  # Output: 8.0
```

#### 4. Menggunakan NumPy (Lebih Efisien)
Untuk perhitungan numerik yang lebih kompleks, NumPy sangat direkomendasikan:
```python
import numpy as np

def jarak_numpy(titik1, titik2):
    titik1 = np.array(titik1)
    titik2 = np.array(titik2)
    return np.linalg.norm(titik2 - titik1)

# Contoh penggunaan
titik1 = np.array([1, 2, 3])
titik2 = np.array([4, 6, 9])
print(jarak_numpy(titik1, titik2))  # Output: 7.0710678118654755
```

### Penjelasan Singkat:
- **Teorema Pythagoras** adalah dasar untuk jarak 2D.
- **Rumus Euclidean** menggeneralisasi konsep ini ke dimensi lebih tinggi.
- Dalam Python, kita dapat mengimplementasikannya dengan `math.sqrt` untuk kasus sederhana atau `numpy.linalg.norm` untuk efisiensi dan kemudahan.