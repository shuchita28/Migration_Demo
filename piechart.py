import matplotlib.pyplot as pt
import pandas as pd

#take the .csv file as an input from the user
csv_path = input("Enter the path of your .csv file : ") 

#read the .csv file
data = pd.read_csv(csv_path)

#groupBy the data into Success, Failure and Skipped categories
result = data.groupby('status')['status'].count()

def total_count (data_frame):
    total = len(data_frame)
    return total
    
def name_columns(data_frame):
    data_frame.columns = ['account_number', 'Status', 'error_msg', 'Last Migration Date']

#display the total analysis
print()
print()
print("Total number of attempted accounts : ",total_count(data))
print("--------------------------------------------------------------------------------------")
print(result)
print("--------------------------------------------------------------------------------------")


#create separate dataframe for Failure cases to analyse them further
data2 = data[(data.status == "FAILURE")]
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
      'CHANGE_AUTH_ID'
      ]

#Create a list of all the known/major Skipped reasons (this part needs Optimization)
s1 = ['Delinquent',
      'NPO',
      'payment',
      'getOpt.optBool("approved")',
      'no equivalent NP mapping',
      'active on multiple accounts',
      'Account Closed',
      'zipfleet',
      'remaining balance',
      'unmapped_cp_rate_plan',
      'SUSPENDED',
      ]
    
def do_analysis(reasons,data_frame):
    #Initialize list of count of each type of failure reason
    e2 = []
    #Initialize list of account_ids for each type of failure reason
    e3 = []
    #Loop over reasons in order to:
    #A. Find the count of each error_type seen in Failure category
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
print()
print()
print("Total number of Failed accounts:", total_f)
print("---------------------------------------------------------------------------------")
do_analysis(e1,data2)

#Outside the function, display Total Skipped accounts
print()
print()
print("Total number of Skipped accounts:", total_s)
print("---------------------------------------------------------------------------------")
do_analysis(s1,data3)


#Plot the pie-chart
#fig, (totalpt,failurept) = pt.subplots(1,2, figsize=(15,10))
#pt.set_title('Results of Analysis')

#Pie chart for total analysis
labels = ['Failed','Skipped','Success']
colors = ['red','yellow','green']
values = result
"""
totalpt.pie(values,labels = labels, colors = colors, autopct='%1.1f%%')
totalpt.title.set_text('Total Accounts Analysis')
"""
pt.pie(values,labels = labels, colors = colors, autopct='%1.1f%%')
pt.title('Total Accounts Analysis')

"""
#sizes,labels = [i[1] for i in errors], [i[0] for i in errors]
#values1 = errors[(errors.Count != 0)]
#values = values1.iloc[:,0]

#piechart for failure analysis
values = values1['Count']
values = values.to_list()

labels = values1['error_type']
labels = labels.to_list()

#sizes_to_plot = sizes.loc[lambda df: df['score'] == 0]
failurept.pie(values, labels = labels, autopct='%1.1f%%')
failurept.title.set_text('Failed Accounts Analysis')


#display both piecharts as subplots
"""
pt.show()
