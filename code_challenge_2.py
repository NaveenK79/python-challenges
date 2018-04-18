import pandas as pd
from datetime import timedelta, date


header_list=['LastName','FirstName', 'MiddleInitial','Gender','DateOfBirth','ProviderType']
dfcomma = pd.read_csv('comma_delimited.txt', sep=',', header=None)
dfcomma.columns = ['LastName','FirstName','Gender','ProviderType','DateOfBirth']
dfcomma=dfcomma.reindex(columns = header_list)

dfspace=pd.read_csv('space_delimeted.txt', sep=' ',header=None)
dfspace.columns = ['LastName','FirstName', 'MiddleInitial','Gender','DateOfBirth','ProviderType']

dfpipe=pd.read_csv('pipe_delimeted.txt', sep='|', header=None)
dfpipe.columns = ['LastName','FirstName', 'MiddleInitial','Gender', 'ProviderType','DateOfBirth']
col = 'DateOfBirth'
dfpipe[col] = pd.to_datetime(dfpipe[col])
future = dfpipe[col] > date(year=2020,month=1,day=1)
dfpipe.loc[future, col] -= timedelta(days=365.25*100)

merged_frame = pd.concat([dfpipe,dfspace,dfcomma], ignore_index=True)
merged_frame["DateOfBirth"]=pd.to_datetime(merged_frame["DateOfBirth"])
merged_frame.to_csv('merged_file.txt',date_format='%m/%d/%Y',index=False)

merged_frame.sort_values(by=["ProviderType","LastName"]).to_csv('merged_file_by_ptypelast_asc.txt', index=False)

merged_frame.sort_values("DateOfBirth").to_csv('merged_file_by_birth_asc.txt', index=False)

merged_frame.sort_values("LastName", ascending=False).to_csv('merged_file_by_lastname_descending.txt', index=False)

