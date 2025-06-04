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

| Cara                     | Apa yang terjadi                     | Cocok untuk                   |
| ------------------------ | ------------------------------------ | ----------------------------- |
| `create_oval(...)`       | Membuat objek baru **setiap kali**   | Jejak, lintasan, "path"       |
| `move()` atau `coords()` | **Memindahkan** objek yang sudah ada | Bola bergerak **tanpa jejak** |

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

Penjelasan tentang `random` di Python sangat penting karena sering digunakan untuk membuat simulasi, permainan, atau perilaku acak seperti pergerakan bola.

Berikut adalah penjelasan **sederhana dan mudah dipahami** untuk masing-masing fungsi `random` yang kamu sebutkan:

---

## 📌 1. `random.randint(0, 3)`

- **Artinya:** Menghasilkan bilangan bulat **acak** dari 0 sampai 3 (termasuk 0 dan 3).
- 📦 Contoh output: `0`, `1`, `2`, atau `3`
- ✅ Cocok untuk memilih angka secara pasti, misalnya posisi awal di antara beberapa tempat.

```python
import random
angka = random.randint(0, 3)
print(angka)  # bisa jadi 0, 1, 2, atau 3
```

---

## 📌 2. `random.uniform(-1, 1)`

- **Artinya:** Menghasilkan bilangan **desimal (float)** acak antara -1 dan 1.
- 📦 Contoh output: `-0.57`, `0.33`, `0.99`, `-0.12`
- ✅ Cocok untuk kecepatan, arah, atau gerakan acak.

```python
arah = random.uniform(-1, 1)
print(arah)  # contoh: 0.62345 atau -0.8312
```

---

## 📌 3. `random.choice([-1, 0, 1, 1])`

- **Artinya:** Memilih satu **elemen secara acak** dari daftar yang kamu berikan.
- 📦 Daftar ini berisi `[-1, 0, 1, 1]`

  - Karena angka `1` muncul dua kali, **kemungkinan keluar 1 lebih besar**.

- 📦 Contoh output: `-1`, `0`, atau `1` (dengan 1 paling sering)

```python
arah_x = random.choice([-1, 0, 1, 1])
print(arah_x)
```

---

## 📌 4. `random.random()`

- **Artinya:** Menghasilkan angka desimal (float) antara **0.0 dan 1.0**
- 📦 Contoh output: `0.1234`, `0.9999`, `0.0`, `0.8765`
- ✅ Cocok untuk peluang (probabilitas), misalnya 50% kemungkinan bergerak.

```python
nilai = random.random()
print(nilai)  # antara 0.0 dan 1.0
```

---

## 📌 5. `random.gauss(0, 1)`

- **Artinya:** Menghasilkan angka acak berdasarkan **distribusi Gaussian (Normal)**.

  - `0` adalah **mean (rata-rata)**
  - `1` adalah **standard deviation (simpangan baku)**

- 📦 Contoh output: `-0.85`, `1.1`, `0.0`, `2.3` (bisa negatif atau positif)
- ✅ Cocok untuk simulasi realistis seperti variasi kecepatan manusia atau data medis.

```python
angka = random.gauss(0, 1)
print(angka)
```

---

## 🧠 Ringkasan Tabel

| Fungsi                    | Jenis Output | Contoh Output  | Kegunaan Umum                               |
| ------------------------- | ------------ | -------------- | ------------------------------------------- |
| `random.randint(a, b)`    | Integer      | `2`            | Angka bulat acak dalam rentang              |
| `random.uniform(a, b)`    | Float        | `-0.5`, `0.72` | Gerakan/desimal acak antara dua angka       |
| `random.choice(list)`     | Dari daftar  | `-1`, `0`, `1` | Memilih dari opsi tertentu (termasuk bobot) |
| `random.random()`         | Float (0-1)  | `0.44`, `0.99` | Probabilitas, peluang                       |
| `random.gauss(mean, std)` | Float        | `-1.2`, `2.5`  | Data realistis berbasis statistik           |

---

Baris berikut dari kode #SCRIPT6:

```python
stepx = 1 if self.mouse_x > self.x else -1 if self.mouse_x < self.x else 0
stepy = 1 if self.mouse_y > self.y else -1 if self.mouse_y < self.y else 0
```

Jika mouse_x lebih besar dari x (mouse ada di kanan walker) → stepx = 1 (gerak ke kanan)

Jika mouse_x lebih kecil dari x (mouse ada di kiri walker) → stepx = -1 (gerak ke kiri)

Jika mouse_x == x (mouse sejajar horizontal dengan walker) → stepx = 0 (tidak gerak horizontal)

Jika mouse_y lebih besar dari y (mouse ada di bawah walker) → stepy = 1 (gerak ke bawah)

Jika mouse_y lebih kecil dari y (mouse ada di atas walker) → stepy = -1 (gerak ke atas)

Jika mouse_y == y (mouse sejajar vertikal dengan walker) → stepy = 0 (tidak gerak vertikal)

adalah cara singkat (ternary expression) dalam Python untuk **menentukan arah gerak walker agar menuju ke posisi mouse**.

Baris tersebut membuat walker bergerak **1 piksel lebih dekat ke mouse** secara deterministik, hanya dalam arah horizontal dan/atau vertikal (bisa diagonal juga jika perlu).

Kalau kamu ingin versi yang lebih panjang dan mudah dibaca:

```python
if self.mouse_x > self.x:
    stepx = 1
elif self.mouse_x < self.x:
    stepx = -1
else:
    stepx = 0

if self.mouse_y > self.y:
    stepy = 1
elif self.mouse_y < self.y:
    stepy = -1
else:
    stepy = 0
```

Mari kita bahas **perhitungan dan logika `update()`** dari class `Ball` pada script kamu dengan **penjelasan bertahap** yang cocok untuk anak SMP dan pemula:

---

## 📌 Fungsi `update()` Lengkap

```python
def update(self):
    # Ambil nilai noise (antara -1 sampai 1)
    noise_val = self.noise(self.t)
    angle = noise_val * 2 * math.pi  # Ubah jadi sudut arah (0–360 derajat)

    # Hitung arah gerak berdasarkan sudut
    dx = math.cos(angle) * self.speed
    dy = math.sin(angle) * self.speed
    self.pos.add(Vector(dx, dy))  # Tambahkan arah ke posisi

    self.t += 0.01  # Geser waktu untuk noise agar arah berubah perlahan
```

---

## 🧠 Penjelasan SIMPLE PERLIN NOISE MOVING BALL

### 1. `noise_val = self.noise(self.t)`

- Mengambil nilai **Perlin noise** berdasarkan waktu `t`.
- Nilainya antara **-1 sampai 1**.
- Karena `t` akan bertambah setiap update (`t += 0.01`), maka arah pergerakan bola akan **berubah perlahan** dari frame ke frame.

> 🧪 Misal: `noise_val = 0.25` pada saat tertentu

---

### 2. `angle = noise_val * 2 * math.pi`

- Noise yang awalnya `-1..1` diubah menjadi **sudut arah**.
- `2π` (≈ 6.28 radian) adalah **satu lingkaran penuh** (360 derajat).

### Contoh perhitungan:

Misal:

- `noise_val = 0.25`
- Maka `angle = 0.25 × 2π ≈ 0.25 × 6.28 ≈ 1.57 rad` → setara 90° (arah atas)

Jika:

- `noise_val = -1` → `angle = -2π` (360° ke kiri)
- `noise_val = 1` → `angle = +2π` (360° ke kanan)

Dengan kata lain:

> Nilai noise dipetakan ke arah gerak di bidang 2D, seolah-olah bola bergerak dalam arah acak tapi halus seperti kompas yang berubah perlahan.

---

### 3. `dx = math.cos(angle) * self.speed`

### 4. `dy = math.sin(angle) * self.speed`

- Mengubah sudut `angle` menjadi gerakan horizontal (`dx`) dan vertikal (`dy`).
- Fungsi `cos(angle)` memberi **gerakan di sumbu X**.
- Fungsi `sin(angle)` memberi **gerakan di sumbu Y**.
- Dikalikan `self.speed` (misalnya 2) agar bola bergerak dengan kecepatan tetap.

#### Misal:

Jika `angle = 90°` (π/2 rad):

- `cos(π/2) = 0` → `dx = 0`
- `sin(π/2) = 1` → `dy = 2`

> Bola akan bergerak ke atas (sumbu Y naik)

Jika `angle = 0°`:

- `dx = 2`, `dy = 0` → bola ke kanan

---

### 5. `self.pos.add(Vector(dx, dy))`

- Update posisi bola berdasarkan perubahan arah dan kecepatan.
- `self.pos` adalah vektor posisi saat ini.
- `add(Vector(dx, dy))` menambahkan perubahan arah ke posisi bola.

---

### 6. `self.t += 0.01`

- Menambahkan waktu sedikit demi sedikit.
- Tujuannya: agar saat `self.noise(self.t)` dipanggil lagi, outputnya berubah sedikit.
- Karena Perlin noise itu smooth, perubahan kecil pada `t` → arah berubah perlahan → gerakan alami.

---

## 🧭 Analogi

Bayangkan kamu jalan di hutan sambil memegang kompas:

- Kompas pelan-pelan berubah arah tiap beberapa detik.
- Kamu selalu bergerak ke arah jarum kompas.
- Kompas = fungsi noise.
- Gerakanmu = `dx, dy` berdasarkan sudut dari noise itu.

---

## 🧮 Simulasi Perhitungan

Misalnya:

- `self.t = 0.5`
- `noise_val = 0.25`
- `angle = 0.25 × 2π ≈ 1.57 rad`
- `speed = 2`

Maka:

- `dx = cos(1.57) × 2 ≈ 0 × 2 = 0`
- `dy = sin(1.57) × 2 ≈ 1 × 2 = 2`

Posisi baru:

- `pos.x = pos.x + 0`
- `pos.y = pos.y + 2`

---

## ✨ Kesimpulan

| Langkah              | Fungsi                                  |
| -------------------- | --------------------------------------- |
| `noise(t)`           | Menghasilkan arah dari waktu            |
| `angle = noise × 2π` | Ubah noise menjadi sudut                |
| `cos/sin(angle)`     | Hitung gerakan berdasarkan sudut        |
| `add(dx, dy)`        | Gerakkan bola sesuai arah dan kecepatan |
| `t += 0.01`          | Buat arah berubah halus setiap frame    |

---

Penjelasan lengkap tentang **tahapan gerakan dan perhitungan** dalam `SCRIPT18: Perlin Noise Moving Triangle with Border` dibagi menjadi tiga bagian besar:

---

## 🧠 **Konsep Dasar**

Skrip ini adalah simulasi visual dari _“kawanan segitiga”_ yang mengikuti medan aliran (flow field) berbasis **Perlin noise**, seolah-olah mereka seperti partikel di dalam medan angin yang berubah-ubah arah. Setiap segitiga adalah **kendaraan (Vehicle)**, dan medan vektor (FlowField) dihasilkan oleh noise untuk memastikan arah gerakan tampak alami dan halus.

---

## 🧩 **Tahapan Gerakan per Frame**

### 1. **Inisialisasi `FlowField`**

```python
angle = self.noise([i * 0.1, j * 0.1]) * 2 * math.pi
v = Vector(math.cos(angle), math.sin(angle))
```

- Per titik grid `(i, j)` dibuat arah berbasis **Perlin noise**.
- `noise()` menghasilkan angka antara `-1` dan `1`, lalu diubah jadi sudut `angle` (dalam radian) dengan `× 2π`.
- Sudut tersebut dikonversi ke vektor arah `(cos(angle), sin(angle))`, lalu disimpan di grid `self.field`.

---

### 2. **Setiap Kendaraan Memanggil `follow()`**

```python
desired = flowfield.lookup(self.position)
desired.mult(self.maxspeed)
steer = Vector.sub_vec(desired, self.velocity)
steer.limit(self.maxforce)
self.apply_force(steer)
```

#### a. **Ambil arah aliran dari grid flowfield di posisi saat ini**

- `lookup()` menentukan grid mana yang dilalui `self.position` dan mengambil vektor arah `desired` dari grid tersebut.

#### b. **Buat vektor target arah gerakan**

- `desired` diskalakan ke `maxspeed`, karena kita ingin kendaraan bergerak cepat ke arah aliran.

#### c. **Hitung gaya steering**

- `steer = desired - current velocity` → kendaraan mencoba mengubah arah menuju vektor flowfield.
- `steer` dibatasi dengan `maxforce` untuk mencegah perubahan arah yang ekstrem (smooth movement).

#### d. **Terapkan gaya ke kendaraan**

```python
self.apply_force(steer)
```

- Menambahkan `steer` ke percepatan (`acceleration`).

---

### 3. **Update Fisika Kendaraan**

```python
self.velocity.add(self.acceleration)
self.velocity.limit(self.maxspeed)
self.position.add(self.velocity)
self.acceleration.mult(0)
```

- `velocity` ditambah `acceleration`, lalu dibatasi `maxspeed`.
- Posisi diperbarui berdasarkan `velocity`.
- Percepatan di-reset (`mult(0)`) agar tidak menumpuk.

---

### 4. **Cek dan Bungkus Batas Layar**

```python
if self.position.x > WIDTH: self.position.x = 0  # dst
```

- Jika kendaraan melewati tepi layar, ia muncul kembali dari sisi berlawanan (seperti torus space).

---

### 5. **Gambar Kendaraan sebagai Segitiga**

```python
theta = self.velocity.heading() + math.pi / 2
```

- Hitung sudut arah gerakan `velocity`, lalu tambahkan `π/2` agar segitiga menghadap arah gerak.
- Tiga titik segitiga dihitung berdasarkan rotasi sudut `theta`.

---

## 📐 **Contoh Perhitungan Langkah**

Misalnya:

- `noise([i=5, j=7]) = 0.25`
- `angle = 0.25 * 2π ≈ 1.57 rad ≈ 90°`
- Maka vektor `desired = (cos(1.57), sin(1.57)) ≈ (0.00, 1.00)` → arah ke atas.

Jika:

- `maxspeed = 3`
- `velocity = (1.0, 0.5)`

Maka:

- `desired = (0, 1) * 3 = (0, 3)`
- `steer = desired - velocity = (0 - 1.0, 3 - 0.5) = (-1.0, 2.5)`
- `steer` dibatasi `maxforce = 0.5` → `normalize` → `(x, y) * 0.5`
- `acceleration = steer`
- Kemudian dihitung `velocity += acceleration`, `position += velocity`.

---

## 🎯 Kesimpulan Visual & Konseptual

| Komponen           | Fungsi                                                  |
| ------------------ | ------------------------------------------------------- |
| **Perlin Noise**   | Membuat medan aliran smooth alami dan tidak acak tajam. |
| **FlowField**      | Grid arah vektor berbasis Perlin noise.                 |
| **Vehicle**        | Segitiga yang bergerak mengikuti arah vektor.           |
| **Steering Force** | Gaya untuk mengarahkan kendaraan ke arah `flowfield`.   |
| **Borders**        | Membungkus kendaraan ke sisi berlawanan layar.          |

---

### Asal Usul Rumus Jarak antara Dua Koordinat

#### 1. **Teorema Pythagoras (Untuk Ruang 2D)**

- **Asal Usul**: Teorema Pythagoras berasal dari matematikawan Yunani kuno, Pythagoras, yang menyatakan bahwa dalam segitiga siku-siku, kuadrat panjang sisi miring (hipotenusa) sama dengan jumlah kuadrat panjang kedua sisi lainnya.
- **Rumus Jarak 2D**: Jika kita memiliki dua titik dalam bidang 2D, $$\( P_1 = (x_1, y_1) \)$$ dan $$\( P_2 = (x_2, y_2) \)$$, jarak antara keduanya dapat dihitung dengan:

$$\text{d} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$

Ini berasal dari membayangkan segitiga siku-siku dengan kaki-kaki $$\( (x_2 - x_1) \)$$ dan $$\( (y_2 - y_1) \)$$.

#### 2. **Rumus Euclidean (Untuk Ruang n-D)**

- **Asal Usul**: Rumus Euclidean adalah generalisasi dari teorema Pythagoras ke ruang berdimensi lebih tinggi (3D, 4D, dst.). Konsep ini dikembangkan dari geometri Euclidean, yang dinamai dari matematikawan Yunani Euclid.
- **Rumus Jarak n-D**: Untuk dua titik dalam ruang n-dimensi, $$\( P_1 = (x_1, x_2, \dots, x_n) \)$$ dan $$\( P_2 = (y_1, y_2, \dots, y_n) \)$$, jarak Euclidean adalah:

$$ \text{d} = \sqrt{(y_1 - x_1)^2 + (y_2 - x_2)^2 + \dots + (y_n - x_n)^2} $$

- Contoh 3D:

$$ \text{d} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} $$

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
