import matplotlib.pyplot as pt
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 10000)

n = input("Enter the path of your .csv file : ")

data = pd.read_csv(n)

def find_count(keyword,data_set):
    count_c = len(data_set[(data_set.status == keyword)])
    return count_c

Success = find_count("SUCCESS",data)
Skipped = find_count("SKIPPED",data)
Failure = find_count("FAILURE",data)
In_Progress = find_count("IN_PROGRESS",data)

l_status = [Success,Failure,Skipped,In_Progress]
l_status = [i for i in l_status if i!=0]

#groupBy the data into Success, Failure and Skipped categories
result = data.groupby('Status')['Status'].count()

def total_count (data_frame):
    total = len(data_frame)
    return total

def name_columns(data_frame):
    data_frame.columns = ['account_number', 'Status', 'error_msg', 'Last Migration Date']

#display the total analysis
def print_analysis(t,r):
    print()
    print()
    print("Total number of accounts : ",t)
    print("--------------------------------------------------------------------------------------")
    print(r)
    print("--------------------------------------------------------------------------------------")

print_analysis(total_count(data),result)

#create separate dataframe for Failure cases to analyse them further
data2 = data[(data.Status == "FAILURE")]
#data2.columns = ['account_number', 'Status', 'error_msg', 'Last Migration Date']
name_columns(data2)

#create a separate dataframe for Skipped cases to analyse them further
data3 = data[(data.status == "SKIPPED")]
#data3.columns = ['account_number', 'Status', 'error_msg', 'Last Migration Date']
name_columns(data3)

#Get the total no. of Failed accounts
total_f = total_count(data2)

#Get the total no. of Skipped accounts
total_s = total_count(data3)

#Create a list of all the known/major Failed reasons (this part needs Optimization)
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
      'membership_next_charge_date'
      ]

#Create a list of all the known/major Skipped reasons (this part needs Optimization)
s1 = ['Delinquent',
      'NPO',
      'payment',
      'getOpt',
      'no equivalent NP mapping',
      'active on multiple accounts',
      'Account Closed',
      'zipfleet',
      'remaining balance',
      'unmapped_cp_rate_plan',
      'SUSPENDED',
      "Missing key 'plan_key'",
      'on_account_status',
      'needs approval',
      'coreApiService',
      'applied',
      'BANNED',
      "Couldn't find Driver",
      'no active users'
      ]


def do_analysis(reasons,data_frame):
    #Initialize list of count of each type of reason
    e2 = []
    #Initialize list of account_ids for each type of reason
    e3 = []
    #Loop over reasons in order to:
    #A. Find the count of each error_type seen in Failure/Skipped category
    #B. Pick out some account_ids for analysis on QAWEB1
    for i in reasons:
        a = data_frame.error_msg.str.count(i).sum()
        e2.append(a)
        b = data_frame.error_msg.str.count(i)
        b.index = data_frame.account_number
        b = b[b!=0]
        c = b.index.tolist()
        e3.append(c)
    #Count no. of unspecified errors
    other_errors = total_count(data_frame)-(sum(e2))
    #Make e1,e2,e3 all into a nice table format
    errors = pd.DataFrame(list(zip(reasons,e2,e3)))
    errors.columns = ['error_type','Count','Account_id']
    #Skip out the zero values (if the particular error_type did not occur at all, we need
    #not display it
    values1 = errors[(errors.Count != 0)]
    a_result = values1.sort_values(by=['Count'], ascending = False)
    print(a_result)
    print("Other errors : ",other_errors)
    print("---------------------------------------------------------------------------------")

#Outside the function, display Total Failed accounts
print("Total number of Failed accounts:", total_f)
print("---------------------------------------------------------------------------------")
do_analysis(e1,data2)

#Outside the function, display Total Skipped accounts
print()
print()
print("Total number of Skipped accounts:", total_s)
print("---------------------------------------------------------------------------------")
do_analysis(s1,data3)

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

pt.axis('equal')

if((len(l_status))==2):
    pt.pie(
        l_status,
        colors=['green', 'yellow'],
        autopct='%1.1f%%')
    pt.legend(title='Migration',labels = ['SUCCESS', 'SKIPPED'])
    pt.show()
if((len(l_status))==3):
    pt.pie(
        l_status,
        colors=['green', 'red', 'yellow'],
        autopct='%1.1f%%')
    pt.legend(title='Migration',labels = ['SUCCESS', 'FAILURE' , 'SKIPPED'])
    pt.show()
else:
    pt.pie(
        l_status,
        colors=['green', 'red', 'yellow','BLUE'],
        autopct='%1.1f%%')
    pt.legend(title='Migration',labels = ['SUCCESS', 'FAILURE' , 'SKIPPED', 'IN_PROGRESS'])
    pt.show()
