import ctypes


class IniSsm(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("num", ctypes.c_int),
        ("num2", ctypes.c_int),
        ("time", ctypes.c_double),
        ("array", ctypes.c_int * 5),
        ("array2d", (ctypes.c_int * 5) * 3),
    ]

    def __repr__(self):
        return (f"IniSsm(num={self.num}), num2={self.num2}, time={self.time}, "
                f"array=({self.array[0]}, {self.array[1]}, {self.array[2]}, {self.array[3]}, {self.array[4]}), "
                f"array2d=(({self.array2d[0][0]}, {self.array2d[0][1]}, {self.array2d[0][2]}, {self.array2d[0][3]}, {self.array2d[0][4]}), "
                f"({self.array2d[1][0]}, {self.array2d[1][1]}, {self.array2d[1][2]}, {self.array2d[1][3]}, {self.array2d[1][4]}), "
                f"({self.array2d[2][0]}, {self.array2d[2][1]}, {self.array2d[2][2]}, {self.array2d[2][3]}, {self.array2d[2][4]}))")


class IniSsmProperty(ctypes.Structure):
    _fields_ = [
        ("property", ctypes.c_int),
        ("property_text", ctypes.c_char * 256),
    ]

    def __repr__(self):
        return f"IniSsmProperty(property={self.property}, property_text={self.property_text})"