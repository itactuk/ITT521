

#!/usr/bin/python3

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)

var2 = 0
if var2 ==0:
   print("2 - Got a true expression value ", var2)
   print("2 - Got a true expression value %d" % var2)
   print("2 - Got a true expression value " + str(var2))
   print (f"2 - Got a true expression value {var2}")
   print (var2 == 0)
print ("Good bye!")
