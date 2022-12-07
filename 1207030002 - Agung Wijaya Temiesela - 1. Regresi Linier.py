'''
PRAKTIKUM FISIKA KOMPUTASI
01 Desember 2022
Agung Wijaya Temiesela
1207030002
Fisika 2020

Materi : |"PREDIKSI"|
Input -> Proses -> Output
Input <- Gambar, Timeframe, Audio, Tubular
Proses -><- Database

Prediksi: Semakin banyak data, semakin baik

Kelebihan: Memiliki probabilitas
Kekurangan: Ketepatan kurang akurat, 90% benar, diluar rentan yang tersesdia.
'''
import numpy as np
from sklearn.linear_model import LinearRegression
#import warnings
from warnings import simplefilter
#Database
# x = Data, y = Target
x = [[1],[3],[5],[7],[9],[11],[13],[15],[17],[19],[21],[23],[25],[27],[29],[31],[33],[35],[37],[39]]
y = [2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78]

regr = LinearRegression().fit(x,y)
regr.score(x,y)

#Data Uji
#predict = np.array([[3]])
if __name__ == '__main__':
    while 1:
        print("Prediksi")
        predict = input("Input Prediksi: ")
        predict = np.array([[predict]])
        # ignore all future warnings
        simplefilter(action='ignore', category=FutureWarning)
        #Menampilkan data prediksi
        print("Output = ", regr.predict(predict).astype(int), "\n----------------------------")

'''
Tugas nya Ganti Database nya minimal 10
'''

