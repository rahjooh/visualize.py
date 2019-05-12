import pandas as pd ,folium
import locale
locale.setlocale(locale.LC_ALL,'')

pd1 = pd.read_csv('1.csv')
print('============pd1=================')
print(pd1.head())

x1 = pd.ExcelFile("../../data/iran provineces lon lat.xlsx")
df_city = x1.parse("Sheet1")
print('============df_city=================')
print(df_city.head())

x2 = pd.ExcelFile("../../data/CRM-Senf-Merchant.xlsx")
mer_df = x2.parse("Sheet1")
print('============mer_df=================')
print(mer_df.head())

df_all = mer_df.merge(pd1, left_on="MerchantCode", right_on="Merchantnumber")
print('============df_all=================')
print(df_all.head())

print('\n\n\n\n\n\n\n\n\n\n')
df_all2 = df_city.merge(df_all, left_on="city name farsi", right_on="CityName")
print('============df_all2=================')
print(df_all2.head())

df_count_mer = df_all.groupby(df_all2['city name farsi']).agg({'sum_amounts': 'sum','harmonic': 'sum', 'all_transactions': 'sum','Merchantnumber':'count'})
df_count_mer.columns = ['sum_amounts','harmonic', 'all_transactions', 'count']
print('============df_count_mer=================')
print(df_count_mer.head())


writer = pd.ExcelWriter('all.xlsx')
df_count_mer.to_excel(writer,'Sheet1')
writer.save()

x5 = pd.ExcelFile("all.xlsx")
df_all3 = x5.parse("Sheet1")
print('============df_all3=================')
print(df_all3.head())


df = df_city.merge(df_all3, left_on="city name farsi", right_on="city name farsi")
print('============df=================')
print(df_city.head())

map_object = folium.Map(location=[35.6892,51.389], zoom_start=6, tiles="Stamen Terrain")
for i in range(31):
    folium.Marker([float(df['lat'][i]),float(df['lon'][i])], popup=str(df['city name farsi'][i])+'  :  '+str(df['pos count'][i])+' پذیرنده'+'\n  _____________________________________________                   '+'جمع مبلغ تراکنش 18 ماه :'+str(locale.currency(df['sum_amounts'][i], grouping=True )).replace('.00',' ').replace('$',' ')+ ' ریال '+' _____________________________________________ '+'تعداد تراکنش 18 ماه :'+str(locale.currency(df['all_transactions'][i], grouping=True )).replace('.00',' ').replace('$',' ')+ ' تراکنش ').add_to(map_object)


folium.Map.save(map_object, "index1.html")

map_object = folium.Map(location=[35.6892,51.389], zoom_start=6, tiles="Stamen toner")
for i in range(31):
    folium.Marker([float(df['lat'][i]),float(df['lon'][i])], popup=str(df['city name farsi'][i])+'  :  '+str(df['pos count'][i])+' پذیرنده'+'\n  _____________________________________________                   '+'جمع مبلغ تراکنش 18 ماه :'+str(locale.currency(df['sum_amounts'][i], grouping=True )).replace('.00',' ').replace('$',' ')+ ' ریال '+' _____________________________________________ '+'تعداد تراکنش 18 ماه :'+str(locale.currency(df['all_transactions'][i], grouping=True )).replace('.00',' ').replace('$',' ')+ ' تراکنش ').add_to(map_object)

folium.Map.save(map_object, "index.html")

