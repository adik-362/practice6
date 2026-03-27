from datetime import datetime
import math
t1 = datetime.strptime(input(),"%Y-%m-%d")
t2 = datetime.strptime(input(),"%Y-%m-%d")
diff = abs((t1-t2).total_seconds())
print(int(diff/86400))
