import ctypes


class IniSsm(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("num", ctypes.c_int),
        ("num2", ctypes.c_int),
        ("time", ctypes.c_double),
        ("array", ctypes.c_int * 5),
    ]

    def __repr__(self):
        return (f"IniSsm(num={self.num}), num2={self.num2}, time={self.time}, "
                f"array=({self.array[0]}, {str(self.array[1])}, {self.array[2]}, {self.array[3]}, {self.array[4]}))")
