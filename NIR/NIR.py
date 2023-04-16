import ctypes

lib = ctypes.CDLL('D:/учеба/уник/labs/6 sem/gmpPractice')

class gmpArray(ctypes.Structure):
    _fields_ = [('count', ctypes.c_int)]

lib.gmpArray_resize.restype = ctypes.POINTER(gmpArray)
lib.gmpArray_resize.argtypes = [ctypes.c_void_p]

lib.gmpArray_sumOMP.restype = ctypes.POINTER(gmpArray, gmpArray, ctypes.c_int)
lib.gmpArray_sumOMP.argtypes = [ctypes.c_void_p]

lib.gmpArray_mulOMP.restype = ctypes.POINTER(gmpArray, gmpArray, ctypes.c_int)
lib.gmpArray_mulOMP.argtypes = [ctypes.c_void_p]

lib.gmpArray_get_len.restype = ctypes.POINTER(gmpArray)
lib.gmpArray_get_len.argtypes = [ctypes.c_int]

arr1=gmpArray(100)
arr2=gmpArray(100)

print(lib.gmpArray_sumOMP(arr1, arr2))
print(lib.gmpArray_mulOMP(arr1, arr2))