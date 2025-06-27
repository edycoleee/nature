# vector.py
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # ---------- Penambahan ----------
    def add(self, other):
        # Menambahkan nilai vektor lain ke vektor ini (ubah self)
        self.x += other.x
        self.y += other.y
        return self

    def added(self, other):
        # Menghasilkan vektor baru hasil penjumlahan tanpa mengubah self
        return Vector(self.x + other.x, self.y + other.y)

    # ---------- Pengurangan ----------
    def sub(self, other):
        # Mengurangi nilai vektor lain dari vektor ini (ubah self)
        self.x -= other.x
        self.y -= other.y
        return self

    def subbed(self, other):
        # Menghasilkan vektor baru hasil pengurangan tanpa mengubah self
        return Vector(self.x - other.x, self.y - other.y)

    # ---------- Perkalian dengan skalar ----------
    def mult(self, scalar):
        # Mengalikan nilai vektor dengan skalar (ubah self)
        self.x *= scalar
        self.y *= scalar
        return self

    def multed(self, scalar):
        # Menghasilkan vektor baru hasil perkalian dengan skalar
        return Vector(self.x * scalar, self.y * scalar)

    # ---------- Pembagian dengan skalar ----------
    def div(self, scalar):
        # Membagi nilai vektor dengan skalar (ubah self)
        if scalar != 0:
            self.x /= scalar
            self.y /= scalar
            return self

    def dived(self, scalar):
        # Menghasilkan vektor baru hasil pembagian dengan skalar
        if scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return Vector(0, 0)

    # ---------- Magnitudo ----------
    def mag(self):
        # Menghitung panjang (magnitudo) vektor
        return math.sqrt(self.x**2 + self.y**2)

    def magnitude(self):
        return self.mag()  # alias

    # ---------- Normalisasi ----------
    def normalize(self):
        # Mengubah self menjadi unit vector (arah tetap, panjang = 1)
        m = self.mag()
        if m != 0:
            self.div(m)
        else:
            self.x, self.y = 0, 0

    def normalized(self):
        # Menghasilkan vektor unit baru tanpa mengubah self
        m = self.mag()
        if m != 0:
            return Vector(self.x / m, self.y / m)
        return Vector(0, 0)

    # ---------- Limit magnitude ----------
    def limit(self, max_val):
        # Batasi panjang maksimum vektor (ubah self)
        if self.mag() > max_val:
            self.normalize()
            self.mult(max_val)

    def limited(self, max_val):
        # Hasilkan vektor baru dengan panjang maksimum tertentu
        v = self.copy()
        if v.mag() > max_val:
            return v.normalized().multed(max_val)
        return v

    # ---------- Set magnitude ----------
    def set_mag(self, new_mag):
        # Mengubah panjang vektor (ubah self)
        self.normalize()
        self.mult(new_mag)

    # def setted_mag(self, new_mag):
    #     # Menghasilkan vektor baru dengan panjang tertentu
    #     return self.normalized().multed(new_mag)

    def setted_mag(self, value):
        m = self.mag()
        if m != 0:
            return self.copy().dived(m).multed(value)
        return Vector()


    # ---------- Heading (sudut arah vektor) ----------
    def heading(self):
        # Kembalikan sudut dalam radian terhadap sumbu x
        return math.atan2(self.y, self.x) if (self.x != 0 or self.y != 0) else 0

    def heading_deg(self):
        # Sudut dalam derajat
        return math.degrees(self.heading())

    def heading_rad(self):
        # Kembalikan sudut dalam radian terhadap sumbu x
        return math.atan2(self.y, self.x) if (self.x != 0 or self.y != 0) else 0
    # ---------- Copy / clone ----------
    def copy(self):
        # Menghasilkan salinan dari vektor ini
        return Vector(self.x, self.y)

    # ---------- Set nilai ----------
    def set(self, x, y):
        # Menetapkan nilai x dan y
        self.x = x
        self.y = y

    # ---------- Rotasi 90 derajat (hanya horizontal mirror) ----------

        # ---------- Rotasi ----------
    def rotate(self, angle):
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        x = self.x * cos_theta - self.y * sin_theta
        y = self.x * sin_theta + self.y * cos_theta
        self.x, self.y = x, y
        return self

    def rotated(self, angle):
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        x = self.x * cos_theta - self.y * sin_theta
        y = self.x * sin_theta + self.y * cos_theta
        return Vector(x, y)


    def rotate90x(self):
        # Menghasilkan vektor baru dengan x dibalik
        return Vector(self.x, -self.y)
    
    def rotate90y(self):
        # Menghasilkan vektor baru dengan x dibalik
        return Vector(-self.x, self.y)

    @staticmethod
    def fromAngle(angle):
        return Vector(math.cos(angle), math.sin(angle))

    @staticmethod
    def from_angle(angle, length=1):
        return Vector(math.sin(angle) * length, math.cos(angle) * length)

    @staticmethod
    def sub_vectors(v1, v2):
        return Vector(v1.x - v2.x, v1.y - v2.y)

    # ---------- Ambil posisi ----------
    def get_position(self):
        # Mengembalikan posisi vektor sebagai tuple
        return (self.x, self.y)

    # ---------- Representasi ----------
    def __repr__(self):
        return f"Vector({self.x:.2f}, {self.y:.2f})"

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
