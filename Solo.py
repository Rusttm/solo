import pandas as pd
import os
import configparser  # импортируем библиотеку
configure = configparser.ConfigParser()  # создаём объекта парсера
configure.read('config.ini')  # читаем конфиг

#configure['Mainer']['data2']='mydata'
a=configure['Mainer']['data']
print(a)
