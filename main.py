import pandas as pd

df = pd.read_csv('tablo.csv', header=None)

df.columns = ['MMSI', 'Lon', 'Lat', 'SOG', 'COG', 'HDG', 'ROT', 'ReportDate', 'Name', 'IMO', 'CallSign', 'ShipandCargo', 'Draught', 'Type', 'NavigationalStatus', 'DimA', 'DimB', 'DimC', 'DimD']

sog_mean = df['SOG'].mean()
sog_median = df['SOG'].median()
sog_mode = df['SOG'].mode()[0]
sog_std = df['SOG'].std()

cog_mean = df['COG'].mean()
cog_median = df['COG'].median()
cog_mode = df['COG'].mode()[0]
cog_std = df['COG'].std()

draught_mean = df['Draught'].mean()
draught_median = df['Draught'].median()
draught_mode = df['Draught'].mode()[0]
draught_std = df['Draught'].std()

ship_loa_mean = df[['DimA', 'DimB', 'DimC', 'DimD']].sum(axis=1).mean()
ship_loa_median = df[['DimA', 'DimB', 'DimC', 'DimD']].sum(axis=1).median()
ship_loa_mode = df[['DimA', 'DimB', 'DimC', 'DimD']].sum(axis=1).mode()[0]
ship_loa_std = df[['DimA', 'DimB', 'DimC', 'DimD']].sum(axis=1).std()

ship_type_sog_corr = df[['Type', 'SOG']].groupby(['Type']).corr().iloc[0::2,-1].reset_index(level=1, drop=True).reset_index()
ship_loa_sog_corr = df[['DimA', 'DimB', 'DimC', 'DimD', 'SOG']].sum(axis=1).corr(df['SOG'])

print('SOG mean:', sog_mean)
print('SOG median:', sog_median)
print('SOG mode:', sog_mode)
print('SOG standard deviation:', sog_std)

print('COG mean:', cog_mean)
print('COG median:', cog_median)
print('COG mode:', cog_mode)
print('COG standard deviation:', cog_std)

print('Draught mean:', draught_mean)
print('Draught median:', draught_median)
print('Draught mode:', draught_mode)
print('Draught standard deviation:', draught_std)

print('Ship LOA mean:', ship_loa_mean)
print('Ship LOA median:', ship_loa_median)
print('Ship LOA mode:', ship_loa_mode)
print('Ship LOA standard deviation:', ship_loa_std)

print('Correlation between ship type and SOG:\n', ship_type_sog_corr)
print('Correlation between ship LOA and SOG:', ship_loa_sog_corr)
