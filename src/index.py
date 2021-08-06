# author Ravi Mukti
# created 12-07-2021
# to install this library please run this command
# pip3 install numpy
# pip3 install matplotlib
# pip3 install scikit-learn
# pip3 install pandas
# pylint: disable=unsubscriptable-object
# pylint: disable=no-member

from numpy import number
import pandas as pd
import os
import numbers
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# import data set
BASEDIR = os.getcwd()
df = pd.read_csv(os.path.join(BASEDIR, 'resource/Data-Penerima-Beasiswa-Sekolah-A.csv'))

print("### 5 Data Teratas ###")
print(df.head())
print("#######################")

# menghapus kolom status_kelayakan dan nama
inputs = df.drop(['status_kelayakan','nama'], axis='columns')
# menentukan target hasil
target = df['status_kelayakan']

# karena library hanya mampu menganalisa angka
# maka kita perlu mengubah kolom jk menjadi angka
# kita ubah menggunakan labelencoder
le_jk = LabelEncoder()
inputs['jk_n'] = le_jk.fit_transform(inputs['jk'])
print()

# membuat data frame baru
inputs_n = inputs.drop('jk', axis='columns')
print("### 5 Data Teratas Setelah Diganti Menjadi Angka ###")
print(inputs_n.head())
print("#######################")

print()

# membuat model decision tree
model = tree.DecisionTreeClassifier()
# kemudian kita train model dengan data inputs_n yg sudah bernilai angka semua
model.fit(inputs_n, target)
# kemudian kita akan menentukan score / nilai pengaruh prediksi jika 1 maka akan sangat akurat
model.score(inputs_n, target)

print("#######################")
print("Masukan Data Calon Penerima Beasiswa")
print("#######################")
print("HANYA MENERIMA INPUTAN ANGKA")
print("1. Jenis Tinggal (jt) ")
inputJenisTinggal = input()
print("2. Alat Transportasi (at) ")
inputAlatTransportasi = input()
print("3. Pekerjaan Ayah (pka) ")
inputPekerjaanAyah = input()
print("4. Penghasilan Ayah (pha) ")
inputPenghasilanAyah = input()
print("5. Pekerjaan Ibu (pki) ")
inputPekerjaanIbu = input()
print("6. Penghasilan Ibu (phi) ")
inputPenghasilanIbu = input()
print("7. Jenis Kelamin - 0 Untuk laki laki 1 untuk perempuan ")
inputJenisKelamin = input()

try:
    nJenisTinggal = float(inputJenisTinggal)
    nAlatTransportasi = float(inputAlatTransportasi)
    nPekerjaanAyah = float(inputPekerjaanAyah)
    nPenghasilanAyah = float(inputPenghasilanAyah)
    nPekerjaanIbu = float(inputPekerjaanIbu)
    nPenghasilanIbu = float(inputPenghasilanIbu)
    nJenisKelamin = float(inputJenisKelamin)

    pred = model.predict([[nJenisTinggal, nAlatTransportasi, nPekerjaanAyah, nPenghasilanAyah, nPekerjaanIbu, nPenghasilanIbu, nJenisKelamin]])

except:
    print("Input anda invalid")
    exit()

print()
print(f"Dapet Beasiswa Gak Nih? (Ya/Tidak) : {pred}")