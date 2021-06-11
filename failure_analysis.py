import matplotlib.pyplot as pt
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def find_error_in_df(df,acct):
    presentCheck = df[df['account_number']==acct].index.values.astype(int)[0]
    print(df.loc[presentCheck,['error_msg']])

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

#take the .csv file as an input from the user
csv_path = input("Enter the path of your .csv file : ")

#read the .csv file
data = pd.read_csv(csv_path)
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
      "Missing 'membership_next_charge_date'",
      "Missing key 'user'",
      'billing_expired',
      'import-user',
      'DELETE_UNAUTHORIZED_DEVICES',
#      'retrieve legacy user',
      'account credit'
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


print("-----------------------------------------------------------------------------------------------------")
print("Total number of Failed accounts:", total)
print("-----------------------------------------------------------------------------------------------------")


errors = pd.DataFrame(list(zip(e1,e2,e3)))
errors.columns = ['error_type','Count','Account_id']
filtered_errors = errors[(errors.Count != 0)]

print(filtered_errors)
if(other_errors>=0):
    print('New errors       ',other_errors)
#print("---------------------------------------------------------------------------------")
#print(e3)


li3 = Diff(e4, e5)
print("These accounts failed due to some new error:")
print(li3)
print(len(li3))

for i in li3:
#   print(i)
    find_error_in_df(data2,i)

values = filtered_errors['Count']
values = values.to_list()
#print(type(values))
labels = filtered_errors['error_type']
labels = labels.to_list()
#print(type(labels))
"""
pt.pie(values, labels = labels, autopct='%1.1f%%')
pt.title('Failed Accounts Analysis')

pt.show()
"""
# creating the bar plot
#Figure size
fig , ax = pt.subplots(figsize = (16, 9))

width = 0.3
#Horizontal Bar Plot
ax.barh(labels , values , width)

#splines removed
for s in ['top' , 'bottom' , 'left' , 'right']:
    ax.spines[s].set_visible(False)

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')


# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 10)
ax.yaxis.set_tick_params(pad = 10)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    pt.text(i.get_width()+0.2,
            i.get_y()+0.2,
            str(round((i.get_width()), 1)),
            fontsize = 10,
            fontweight ='bold',
            color ='grey')

# Add Plot Title
ax.set_title('Account failure reasons')

# Add Text watermark
fig.text(0.9, 0.15, 'QA @ Zipcar, Inc.', fontsize = 12,
         color ='green', ha ='right', va ='bottom',
         alpha = 0.7)

#reduce padding
pt.tight_layout()
# Show Plot
pt.show()

"""
pt.bar(labels, values, color ='maroon',
        width = 0.4)

pt.xlabel("Error Types")
pt.ylabel("No. of accounts failed")
pt.title("Account failure reasons")
pt.show()
"""
