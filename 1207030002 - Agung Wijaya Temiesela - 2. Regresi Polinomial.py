'''
PRAKTIKUM FISIKA KOMPUTASI
01 Desember 2022
Agung Wijaya Temiesela
1207030002
Fisika 2020
Regresi Polinomial
'''
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy as np
#import warnings
from warnings import simplefilter
#Database
# x = Data, y = Target
x = [[1],[3],[5],[7],[9],[11],[13],[15],[17],[19],[21],[23],[25],[27],[29],[31],[33],[35],[37],[39]]
y = [2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78]

#Data Uji
#predict = np.array([[12.86]])
if __name__ == '__main__':
    while 1:
        print("Prediksi")
        predict = input("Input Prediksi: ")
        predict = np.array([[predict]])
        poly = PolynomialFeatures(degree=2)
        # ignore all future warnings
        simplefilter(action='ignore', category=FutureWarning)
        x_ = poly.fit_transform(x)
        predict_ = poly.fit_transform(predict)
        regr = linear_model.LinearRegression()
        regr.fit(x_,y)
        #Menampilkan data prediksi
        #print("Prediksi")
        #print("Input = ", predict)
        #print("Output = ", regr.predict(predict_))
        print("Output = ", regr.predict(predict_).astype(int), "\n----------------------------")
