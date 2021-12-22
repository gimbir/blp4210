import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('covid_data.csv')

df = pandas.DataFrame(data=data, columns=['gender', 'age', 'death', 'country'])

# a)Yaşları 50 ile 60 arasında olan bayan(female) hasta sayısı nedir
dict1 = {'female': [], 'male': []}

for gender, age in zip(df.gender, df.age):
    if gender == 'female' and (age > 50 and age < 60):
        dict1["female"].append(age)

_1a = len(dict1['female'])
print(_1a)

# b) Ölen ve yaşayan hastaların yaş ortalaması nedir
dead_count = 0
alive_count = 0
for death in df.death:
    if death == '1':
        dead_count += 1
    elif death == '0':
        alive_count += 1

print(dead_count)
print(alive_count)

# c) Ölen kadın  ve Ölen erkeklerin yaş ortalaması nedir
dict2 = {'female': [], 'male': []}

for gender, age, dead in zip(df.gender, df.age, df.death):
    if gender == 'female' and dead == '1':
        dict2["female"].append(age)
    elif gender == 'male' and dead == '1':
        dict2["male"].append(age)

# female avegare
female_sum = 0
for i in dict2['female']:
    female_sum += i
female_avg = female_sum / len(dict2['female'])
print(female_avg)

# male average
male_sum = 0
for i in dict2['male']:
    male_sum += i
male_avg = male_sum / len(dict2['male'])
print(male_avg)

# d)20 yaşın altında Çin de (China) bulunan hastaların sayısı nedir
count = 0
for age, country in zip(df.age, df.country):
    if age < 20:
        count += 1

print(count)

# e) 50 yaşından büyük Çinde ölen hastaların , 50 yaşından büyük Almanyada ölen hastalara oranı nedir?
# NOT: kaynaklardaki csv dosyasina gore Almanya'da olen hasta sayisi olmadigi icin degerleri manuel olarak degistirdim.
ch_count = 0
de_count = 0
for age, country, death in zip(df.age, df.country, df.death):
    if age > 50 and country == 'China' and death == '1':
        ch_count += 1
    elif (age > 50) and (country == 'Germany') and (death == '1'):
        de_count += 1

oran = ch_count / de_count
print(ch_count)
print(de_count)
print(oran)