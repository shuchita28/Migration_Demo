import matplotlib.pyplot as pt
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv('<filename.csv>')

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


data2 = data[(data.status == "FAILURE")]
data2.columns = ['account_number', 'Status', 'error_msg', 'Last Migration Date']
total = len(data2)

e1 = ['interrupted',
      'RollBackInfo',
      'forced_reset_status',
      "Missing 'market_id'",
      "Missing 'rate_plan_key'",
      "Missing 'user_start_date'",
      'missing_key',
      'membership_details_not_found',
      'members_user_not_found',
      'core-api',
      'CHANGE_AUTH_ID',
      "Missing 'membership_next_charge_date'"
      ]

e2 = []
e3 = []

#Initialize a list of all account_ids in the list
e4 = data2.account_number.tolist()
"""
print(type(e4))
print("This is e4 ***",e4,"***End of e4")
"""
e5 = []
#total = len(data)
#print(total)

for i in e1:
    a = data2.error_msg.str.count(i).sum()
    e2.append(a)
    b = data2.error_msg.str.count(i)
    b.index = data2.account_number
    b = b[b!=0]
    #b_f = b.index
    #print("This is b***",b_f,"End of b")
    c = b.index.tolist()
    e5.extend(c)
    #print("This is e5***",e5,"End of e5")
    #print(len(e5))
    e3.append(c)

other_errors = total-(sum(e2))


print("---------------------------------------------------------------------------------")
print("Total number of Failed accounts:", total)
print("---------------------------------------------------------------------------------")


errors = pd.DataFrame(list(zip(e1,e2,e3)))
errors.columns = ['error_type','Count','Account_id']
filtered_errors = errors[(errors.Count != 0)]

print(filtered_errors)
print('Other errors       ',other_errors)
#print("---------------------------------------------------------------------------------")
#print(e3)

#For debugging purposes
li3 = Diff(e4,e5)
print("The difference comes in >> ",len(li3)," accounts")
print(li3)


values = filtered_errors['Count']
values = values.to_list()
labels = filtered_errors['error_type']
labels = labels.to_list()
pt.pie(values, labels = labels, autopct='%1.1f%%')
pt.title('Failed Accounts Analysis')

pt.show()
