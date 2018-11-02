from spreedsheet import Sheet
from github_client import Git
from threading import Thread

g = Git() 
records = g.get_issues_records()
if records is not None:
  MySheet = Sheet(records)
  MySheet.create_table()
  print('Done!')