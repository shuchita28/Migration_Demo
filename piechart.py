
import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv('/Users/shuchitamishra/Desktop/Prod-Migration/Cron Job 15_03-Table 1.csv')

print(data)

result = data.groupby('Status')['Status'].count()

print(result)


pt.axis('equal')

pt.pie(result, colors = ['red','yellow','green'], labels = ['Failure','Skipped','Success'], autopct='%1.1f%%')

pt.legend(title='Analysis')

pt.show()
