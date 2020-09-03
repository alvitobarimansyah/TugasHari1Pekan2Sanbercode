# soal no 1

import pandas as pd

dict = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat"],
       "Ibu Kota": ["Jakarta", "Tokyo", "New Dehli", "Beijing", "Washington, D.C."],
       "Luas": [1905, 377972, 3287, 9597, 9834],
       "Populasi": [264, 143, 1252, 1357, 5298] }

brics = pd.DataFrame(dict)
print(brics)

# soal no 2

import pandas as pd

df = pd.read_csv('diamonds-1.csv')

df

# soal no 3

# Apa perbedaan Series dengan list dan dictionary

Series dengan list :
series indexnya tidak harus bertipe integer, sedangkan list indexnya bertipe integer
    
# Series dengan dictionary :
series dia bisa mempunyai data yang duplikat, sedangkan dictionary dia tidak bisa mempunyai data yang duplikat

# Apa perbedaan dataframe dan series

Series adalah suatu objek satu dimensi yang dapat menyimpan berbagai jenis tipe data seperti integer, string, dan lain sebagainya, sedangkan DataFrame adalah suatu objek 2 dimensi tempat menyimpan data dengan lebih terstruktur. 

# Buatlah suatu data series

import pandas as pd
obj_series = pd.Series([1, 2, 3, 4, 5])

obj_series

# soal no 4

import pandas as pd

df = pd.read_csv('diamonds-1.csv')

# baris pertama dari column price
df['price'].head(1)

# baris terakhir dari column color
df['color'].tail(1)

# soal no 5

Jelaskan apa itu deskriptis statistik!

deskriptif statistik adalah seperti central tendency, dispersi dan bentuk distributsi dari data. 

# soal no 6

import pandas as pd

df = pd.read_csv('diamonds-1.csv')

# Berapa nilai rata-rata dari column price
df['price'].mean()

# Berapa nilai standar deviasi dari column depth
df['depth'].std()

# Berapa nilai maximum dari column carat
df['carat'].max()
