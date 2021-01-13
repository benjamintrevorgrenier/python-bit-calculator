import sys, datetime

#This function will obtain the 256-bit binary representation of the parameter passed

#This sets the maximum possible integer value for entry
IntStr = ''
while len(IntStr) < 256:
    IntStr += '1'
Max256Val = int(IntStr,2)

#This flag enables or disables time-tracking
TimeTrack = False

#This flag ensures that the process continues until the user wants to exit.
StillGoing = True

#This will loop until the StillGoing flag is set to false
while StillGoing == True:
    #Obtain the input from the user
    BitIn = input('Please enter the integer value to be calculated (or press enter to quit):> ')

    #If the input is empty, exit
    if BitIn == '': sys.exit()

    #This conducts error checking on the input
    Continue = True
    if BitIn.isnumeric() == False:
        Continue = False
        print('\t** Error: The value input was not a valid number **')
    elif int(BitIn) > Max256Val:
        Continue = False
        print('\t** Error: The number value entered is greater than a 256-bit value **') 

    if Continue == True:
        #Optional time-tracking
        if TimeTrack == True:
            CurTime = datetime.datetime.now()
            print(f'Started at {CurTime.strftime("%H:%M:%S.%f")}')

        #This obtains the binary representation of the input value
        Result = '{0:b}'.format(int(BitIn))

        #This ensures that the returned value is a 256-bit binary number by adding leading zeros
        while len(Result) < 256:
            Result = '0' + Result

        #Optional time-tracking:
            if TimeTrack == True:
                CurTime = datetime.datetime.now()
                print(f'Ended at {CurTime.strftime("%H:%M:%S.%f")}')

        #Display the result for the user
        print(Result)

    #Add in a couple of spaces before the next Input query
    print()
    print()
