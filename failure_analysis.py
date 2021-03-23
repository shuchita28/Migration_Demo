import pprint
import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv('/Users/shuchitamishra/Desktop/Prod-Migration/failures-22-03.csv')

#print(data)

total = len(data)


interrupted_error    = data.error_msg.str.count("interrupted")
interrupted_error.index = data.account_number
interrupted_error = interrupted_error[interrupted_error!=0]
#print(interrupted_error)
flagie = interrupted_error.index.tolist()

rb_info    = data.error_msg.str.count("RollBackInfo")
rb_info.index = data.account_number
rb_info = rb_info[rb_info!=0]
#print(interrupted_error)
flagrb = rb_info.index.tolist()

frs    = data.error_msg.str.count("forced_reset_status")
frs.index = data.account_number
frs = frs[frs!=0]
#print(interrupted_error)
flagfrs = frs.index.tolist()

mkid    = data.error_msg.str.count("Missing 'market_id'")
mkid.index = data.account_number
mkid = mkid[mkid!=0]
#print(interrupted_error)
flagmkid = mkid.index.tolist()

mskey    = data.error_msg.str.count("missing_key")
mskey.index = data.account_number
mskey = mskey[mskey!=0]
#print(interrupted_error)
flagmskey = mskey.index.tolist()

interrupted_error    = data.error_msg.str.count("interrupted").sum()
RollBack_error       = data.error_msg.str.count("RollBackInfo").sum()
forced_reset_error   = data.error_msg.str.count("forced_reset_status").sum()
market_id_error      = data.error_msg.str.count("Missing 'market_id'").sum()
missing_key_error    = data.error_msg.str.count("missing_key").sum()

other_errors         = total-(interrupted_error+RollBack_error+forced_reset_error+market_id_error+missing_key_error)

print("Total number of Failed accounts:", total)
print("---------------------------------------------------------------------------------")
e1 = ['interrupted_error','RollBackInfo_error','forced_reset_error','market_id_error', 'missing_key_error','Other']
e2 = [interrupted_error,RollBack_error,forced_reset_error,market_id_error, missing_key_error,other_errors]
e3 = [flagie , flagrb , flagfrs , flagmkid , flagmskey]
#print(e3)
"""
e3 = []

for i in e1:
    #print(i)
    a = data.error_msg.str.count(str(i))
    print(a)
    a.index = data.account_number
    a = a[a!=0]
    b = a.index.tolist()
    e3.append(b)
"""    
errors = pd.DataFrame(list(zip(e1,e2,e3)))
errors.columns = ['error_type','Count','Sample account_id']
filtered_errors = errors[(errors.Count != 0)]
print(filtered_errors)
print("---------------------------------------------------------------------------------")
#print(e3)


values = filtered_errors['Count']
values = values.to_list()
#print(type(values))
labels = filtered_errors['error_type']
labels = labels.to_list()
#print(type(labels))
pt.pie(values, labels = labels, autopct='%1.1f%%')
pt.title('Failed Accounts Analysis')

pt.show()

 
