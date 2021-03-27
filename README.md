# Migration_Demo

Created when I was working at TCS, for Zipcar - Avis Budget Client. 

My Project involved a lot of manual analysis of user accounts and we used to do the whole process of batch analysis manually 
-filtering data, 
-sorting out Success and Failed accounts, 
-filtering out the error messages 
-typing out the results on Slack
I have created a script in Python which takes the .csv file and counts the number of Success, Failure and Skipped accounts and also analyses the Failed accounts to show how many have failed due to some major reason. 
This script reduces the:
time to analyze each batch from ~20 minutes to ~5 seconds, saving up a lot of time
manual effort put into each batch 
It also gives a visual representation of the accounts in form of pie-chart. 
