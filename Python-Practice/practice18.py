#command = " "
started = False
#stopped = False

while True:
 command = input('> ').lower()

 if command == 'start':

   if started:
    print('Car is already started!')

else:
    started = True
    print('Car Started.....')

elif command == "stop":
        if not started:
            print('Car is already stopped!')

     else:
            stopped = True
             print('Car Stopped....')

elif command == 'help':
            print ("""
Start - Start the car.
Stop - To stop the car.
Quit - To quit the program
         """)

     elif command == 'quit':
        break

       else:
         print('Invalid command.')

