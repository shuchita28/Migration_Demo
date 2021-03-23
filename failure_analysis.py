import pprint
import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv('/Users/shuchitamishra/Desktop/zipcar/failures.csv')

print(data)

total = len(data)

interrupted_error    = data.error_msg.str.count("interrupted").sum()
RollBack_error       = data.error_msg.str.count("RollBackInfo").sum()
forced_reset_error   = data.error_msg.str.count("forced_reset_status").sum()
market_id_error      = data.error_msg.str.count("Missing 'market_id'").sum()
missing_key_error    = data.error_msg.str.count("missing_key").sum()

other_errors         = total-(interrupted_error+RollBack_error+forced_reset_error+market_id_error+missing_key_error)

print("------------------------------RESULTS--------------------------------------------")
print("Unable to get user from members due to: interrupted: members/user >> null   ", interrupted_error)
print("---------------------------------------------------------------------------------")
print("RollBackInfo(....stepThatFailed=CREATE_IDP_USER)                            ",RollBack_error)
print("---------------------------------------------------------------------------------")
print("An unexpected response from /users/forced_reset_status                      ",forced_reset_error)
print("---------------------------------------------------------------------------------")
print("illegal_argument: membership/account/migrate >> Missing 'market_id'         ",market_id_error)
print("---------------------------------------------------------------------------------")
print("Migration failure -  members_user_missing_key: Invalid/Missing key 'status' ",missing_key_error)
print("---------------------------------------------------------------------------------")
print("Other errors                                                                ",other_errors)
print("---------------------------------------------------------------------------------")


analysis = [('interrupted_error', interrupted_error),
            ('RollBackInfo_error', RollBack_error),
            ('forced_reset_error', forced_reset_error),
            ('market_id_error', market_id_error),
            ('missing_key_error', missing_key_error),
            ('other', other_errors)
            ]

pprint.pprint(analysis)

sizes,labels = [i[1] for i in analysis], [i[0] for i in analysis]

pt.pie(sizes, labels = labels, autopct='%1.1f%%')

pt.legend(title="Failure Analysis")

pt.show()
 
