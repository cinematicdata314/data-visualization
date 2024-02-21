
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://data.ontario.ca/dataset/752ce2b7-c15a-4965-a3dc-397bf405e7cc/resource/274b819c-5d69-4539-a4db-f2950794138c/download/vac_status_hosp_icu.csv')
print(df.head(300))

fig, ax = plt.subplots(figsize=(16, 10))
cols = ['hospitalnonicu_unvac',  'hospitalnonicu_partial_vac',  'hospitalnonicu_full_vac']
for col in cols:
    ax.plot(df['date'], df[col], label=col)

ax.set_xlabel('Date')
ax.set_ylabel('Number of patients')
ax.set_title('COVID-19 Vaccination Status of Hospital and ICU Patients in Ontario')
ax.legend()

plt.show()






# df = pd.read_csv('https://data.ontario.ca/dataset/c43fd28d-3288-4ad2-87f1-a95abac706b8/resource/3273c977-416f-407e-86d2-1e45a7261e7b/download/deaths_fatality_type.csv')
# print(df.head(300))



# df['date'] = pd.to_datetime(df['date'])

# # group data by date and sum death_covid column
# df_covid = df.groupby('date')['death_covid'].sum().reset_index()

# # plot death_covid column
# plt.plot(df_covid['date'], df_covid['death_covid'])
# plt.xlabel('Date')
# plt.ylabel('Deaths due to COVID-19')
# plt.title('Deaths due to COVID-19 in Ontario over time')
# plt.show()


# Question: 
# The question that we are trying to investigate is weather there 
# is a clear link between vaccines helping with COVID-19 rates
# of either infection or hospitaliztion during the pandemic?

