import pandas as pd

#переменные для путей к файлам
read_data_a = 'in_data_a.csv'
read_data_p = 'in_data_p.csv'
data_out = 'out.csv'

data_a = pd.read_csv(read_data_a, sep = ',', header = 0)
data_p = pd.read_csv(read_data_p, sep = ',', header = 0)
        
data_a_2 = pd.DataFrame(data_a)
data_p_2 = pd.DataFrame(data_p)

#удалил столбец с id
data_a_2.drop(['id'], axis = 'columns', inplace = True)
#изменил название стобцов и удалил campaign
data_a_2.rename(columns = {'Date' : 'date', 'Campaign' : 'campaign', 'Installs' : 'installs'}, inplace = True)
data_p_2.drop(['campaign'], axis = 'columns', inplace = True)
#Объеденил по ad_id и Date
data_3 = data_a_2.merge(data_p_2, on = ['ad_id', 'date'], how = 'outer')
#удаляю столбец ad_id, так как он больше не нужен
data_3.drop(['ad_id'], axis = 'columns', inplace = True)
df = data_3[['app', 'date', 'campaign', 'os', 'installs', 'spend']]
#группирую, суммирую столбцы installls и spend и округляю значения в spend до 2 знач. цифр
df = pd.DataFrame(data_3).groupby([ 'app', 'date', 'campaign', 'os']).sum().round({'spend' : 2})
#добавляю столбец cpi
df['cpi'] = round(df['spend'] / df['installs'])
#сохраняю
df.to_csv(data_out, index = True, header = True)