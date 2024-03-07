
# importing
import numpy as np # Numpy kütüphanesinin eklenmesi

# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*15 vektör oluşturma

print(array.shape) # vektörümüzün kaça kaç olduğunu gösterir

a = array.reshape(3,5) # arrayimizi 
print("shape: ",a.shape)
print("dimension: ", a.ndim) # arrayimizin kaç boyutlu olduğunu gösterir

print("data type: ",a.dtype.name) # arrayin içindeki verilerin türünü gösterir
print("size: ",a.size) # arrayin boyutunu gösterir

print("type: ",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

zeros = np.zeros((3,4)) # sıfırlardan oluşan 3'e 4'lük bir matrix oluşturur

zeros[0,0] = 5 # eleman güncelleme
print(zeros)

np.ones((3,4)) # birlerden oluşan 3'e 4'lük bir matrix oluşturur

np.empty((2,3)) # rasgele sayılardan oluşan 3'e 4'lük bir matrix oluşturur
np.full((3,4),3 ) # sadece 3'lerden oluşan 3'e 4'lük bir matrix oluşturur

a = np.arange(10,50,5) # 10'dan 50'ye kadar 5'er 5'er sayıları arttırıp yazar
print(a)

a = np.linspace(10,50,20) # 10'dan 50'ye kadar 20 sayı oluşturur
print(a)

a= np.array([3.14,4,12.7,2,7.9],dtype=int) # elemanların typelarını kontrol etmek için dtype kullanılır


# %% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

print(a<2)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

# element wise prodcut
print(a*b)

# matrix prodcut
a.dot(b.T)

print(np.exp(a))

a = np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())


print(a.sum(axis=0))
print(a.sum(axis=1))

print(np.sqrt(a))
print(np.square(a)) # a**2


print(np.add(a,a))


# %% indexing and slicing
import numpy as np
array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

# array[başlangıç indexi:bitiş indexi: adım ]

print(array[0])

print(array[0:4:])

reverse_array = array[::-1]
print(reverse_array)


array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1])

print(array1[:,1])


print(array1[1,1:4])


print(array1[-1,:])
print(array1[:,-1])

# %%
# shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# flatten
a = array.ravel() # arrayi dümdüz bir hale getirir

array2 = a.reshape(3,3)

arrayT = array2.T # arrayin transpozunu alır

print(arrayT.shape)


array5 = np.array([[1,2],[3,4],[4,5]])


#array5 = np.column_stack((array1,array1))


# %% stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# veritical
#array([[1, 2],
#       [3, 4]])
#array([[-1, -2],
#       [-3, -4]])
array3 = np.vstack((array1,array2))

# horizontal
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

array4 = np.hstack((array1,array2))

array5= np.concatenate([array1, array2] , axis=0) # axis=0 satır bazında birleştirir
array6= np.concatenate([array1, array2] , axis=1) # axi=1 sütun bazında birleştirir

#%% convert and copy

liste = [1,2,3,4]   # list

array = np.array(liste) #np.array

liste2 = list(array)

a = np.array([1,2,3])

b = a
b[0] = 5
c = a

d =  np.array([1,2,3])

e = d.copy()

f = d.copy()