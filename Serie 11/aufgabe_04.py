import numpy as np

def list_to_numpy(lst):
    arr = np.array(lst)
    
    print("NumPy-Array:")
    print(arr)
    print("Anzahl Dimensionen (ndim):", arr.ndim)
    print("Form (shape):", arr.shape)
    print("Anzahl Elemente (size):", arr.size)
    print("-" * 40)
    
    return arr


view_arr = arr.view()
view_arr[0, 0] = 999

copy_arr = arr.copy()
copy_arr[0, 0] = 555
