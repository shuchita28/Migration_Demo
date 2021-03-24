import matplotlib.pyplot as pt
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv('/Users/shuchitamishra/Desktop/Prod-Migration/failures-22-03.csv')

total = len(data)
print(total)

e1 = ['interrupted','RollBackInfo','forced_reset_status',"Missing 'market_id'", 'missing_key']
e2 = []
e3 = []
for i in e1:
    a = data.error_msg.str.count(i).sum()
    e2.append(a)

other_errors = total-(sum(e2))

print("Total number of Failed accounts:", total)
print("---------------------------------------------------------------------------------")

for i in e1:
    a = data.error_msg.str.count(i)
    a.index = data.account_number
    a = a[a!=0]
    b = a.index.tolist()
    e3.append(b)


errors = pd.DataFrame(list(zip(e1,e2,e3)))
errors.columns = ['error_type','Count','Account_id']
filtered_errors = errors[(errors.Count != 0)]
print(filtered_errors)
print("---------------------------------------------------------------------------------")

values = filtered_errors['Count']
values = values.to_list()
labels = filtered_errors['error_type']
labels = labels.to_list()
pt.pie(values, labels = labels, autopct='%1.1f%%')
pt.title('Failed Accounts Analysis')

pt.show()
