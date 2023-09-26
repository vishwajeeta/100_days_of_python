import time
greeting=time.strftime('%H:%m:%S')
print(greeting)
if time.strftime('%H:%m')>='0:00' and time.strftime('%H')<='11:59':
   print("good morning!")
elif time.strftime('%H:%m')>='12:00' and time.strftime('%H')<='18:00':
   print("good evening!")
elif time.strftime('%H:%m')>='18:01' and time.strftime('%H')<='24:00':
   print("good night!")
else:
   print("good day!!")
