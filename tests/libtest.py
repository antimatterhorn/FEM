import ctypes

libVectorMath = ctypes.CDLL('../build/libVectorMath.so')
print(libVectorMath)