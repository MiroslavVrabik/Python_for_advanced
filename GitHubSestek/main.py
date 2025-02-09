# 1. možnost - zdlouhavější zápis
import data
print(data.my_data)

# 2. možnost - doporučovaná
from data import  my_data
print(my_data)

# 3. možnost - moc se nepoužívá, matoucí
from data import * #importuje vše

# 4. možnost - alia (jiný název)
import data as d
print(d.my_data)