# import time as t
import datetime as t
import os
print("Last accessed time:",os.path.getatime('./dir.py'))
print("Last accessed time:",os.path.getmtime('./dir.py'))

access_date=t.datetime.fromtimestamp(os.path.getatime('./dir.py')).strftime("%Y-%M-%D")
# access_date=t.datetime.fromtimestamp(os.path.getatime('./dir.py'))
print("Accesed Date:",access_date)