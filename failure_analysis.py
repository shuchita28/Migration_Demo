import pprint
import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv('/Users/shuchitamishra/Desktop/Prod-Migration/failures-22-03.csv')

#print(data)

total = len(data)

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
e3 = 
errors = pd.DataFrame(list(zip(e1,e2)))
errors.columns = ['error_type','Count']
filtered_errors = errors[(errors.Count != 0)]
print(filtered_errors)
print("---------------------------------------------------------------------------------")



values = filtered_errors['Count']
values = values.to_list()
#print(type(values))
labels = filtered_errors['error_type']
labels = labels.to_list()
#print(type(labels))
pt.pie(values, labels = labels, autopct='%1.1f%%')
pt.title('Failed Accounts Analysis')

pt.show()

 

 
