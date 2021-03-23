import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv('/Users/shuchitamishra/Desktop/Prod-Migration/Cron Job 16_03-Table 1.csv')

result = data.groupby('Status')['Status'].count()

print("Total attempted: ",len(data))
print("---------------------------------------------------------------------------------")
print(result)
print("---------------------------------------------------------------------------------")


data2 = data[(data.Status == "FAILURE")]

data2.columns = ['Account Number', 'Status', 'error_msg', 'Last Migration Date',
       'Unnamed: 4']
print()
print()
print("Failed accounts: ")
print("---------------------------------------------------------------------------------")
print(data2)
print("---------------------------------------------------------------------------------")
print()
print()
total = len(data2)

interrupted_error    = data2.error_msg.str.count("interrupted").sum()
RollBack_error       = data2.error_msg.str.count("RollBackInfo").sum()
forced_reset_error   = data2.error_msg.str.count("forced_reset_status").sum()
market_id_error      = data2.error_msg.str.count("Missing 'market_id'").sum()
missing_key_error    = data2.error_msg.str.count("missing_key").sum()

other_errors         = total-(interrupted_error+RollBack_error+forced_reset_error+market_id_error+missing_key_error)

print("Total number of Failed accounts:", total)
print("---------------------------------------------------------------------------------")

e1 = ['interrupted_error','RollBackInfo_error','forced_reset_error','market_id_error', 'missing_key_error','Other']
e2 = [interrupted_error,RollBack_error,forced_reset_error,market_id_error, missing_key_error,other_errors]
errors = pd.DataFrame(list(zip(e1,e2)))
errors.columns = ['error_type','Count']
values1 = errors[(errors.Count != 0)]
print(values1)
print("---------------------------------------------------------------------------------")

"""
values1 = errors[(errors.Count != 0)]
print(values1)
print("---------------------------------------------------------------------------------")
#values = values1.iloc[:,0]
values = values1['Count']
values = values.to_list()
print(values)
print(type(values))
print("---------------------------------------------------------------------------------")
labels = values1['error_type']
labels = labels.to_list()
#values = errors[(errors.Count != 0)]
#print(values)
#labels = values['error_type']
#labels = labels.to_list()
print(labels)
"""

fig, (totalpt,failurept) = pt.subplots(1,2, figsize=(15,10))
#pt.set_title('Results of Analysis')

#pt.figure(0)
labels = ['Failure','Skipped','Success']
#print(type(labels))
colors = ['red','yellow','green']
values = result
#print(type(values))
totalpt.pie(values,labels = labels, colors = colors, autopct='%1.1f%%')
totalpt.title.set_text('Total Accounts Analysis')

#pt.figure(1)
#sizes,labels = [i[1] for i in errors], [i[0] for i in errors]
values1 = errors[(errors.Count != 0)]
#values = values1.iloc[:,0]
values = values1['Count']
values = values.to_list()
#print(type(values))
labels = values1['error_type']
labels = labels.to_list()
#print(type(labels))
#sizes_to_plot = sizes.loc[lambda df: df['score'] == 0]
failurept.pie(values, labels = labels, autopct='%1.1f%%')
failurept.title.set_text('Failed Accounts Analysis')

pt.show()