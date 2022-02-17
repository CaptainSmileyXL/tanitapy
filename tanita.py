#!/usr/local/bin/python3

##  Author: CaptainSmiley
##  Date:   2/14/2022
##  License:    Creative Commons Zero v1.0 Universal

import sys
import csv
import getopt



##  algorithim from:
##  http://users.telenet.be/WBtE/cunning.html
def CunninghamEquation(mass, fat):
    print("\n")
    print("\nIf you eat a moderate protein diet your factor will be 0.10")
    print("(roughly 1g/lb of body weight), for a high protein diet your factor")
    print("will be 0.15 (roughly 1.5 g/lb of body weight).")
    factorTEF = input("Protein intake factor: ")

    print("\nNon Exercise Activity Thermogenesis")
    print("1.2 - 1.3 for bed- or chair-ridden individuals")
    print("1.4 - 1.5 for sedentary occupation without daily movement")
    print("1.5 - 1.6 for sedentary occupation with daily movement")
    print("1.6 - 1.8 for occupation with prolonged standing")
    print("1.9 - 2.1 for strenuous work")
    factorNEAT = input("NEAT factor: ")

    print("\nHow many hours, or less, of exercise, in fractions of hours (eg. 0.75 for 45 min)")
    duration = input("Duration: ")

    print("\nMetabolic Effect of Training")
    print("For instance, free weight lifting MET is 6")
    MET = input("MET factor: ")

    mass = mass * 0.453592
    FM = mass * (fat / 100)
    FFM = mass - FM
    RMR = 370 + 21.6 * FFM
    TEF = RMR * float(factorTEF)
    NEAT1 = RMR * float(factorNEAT)
    NEAT2 = TEF
    NEAT3 = NEAT1 + TEF
    ERAT = mass * float(duration) * float(MET)
    result = NEAT3 + ERAT
#    MJ = result * 4.184 / 1000     #  megaoule
#    KWM = M * 0.2778               #  in kWh

    print("\n")
    return result



def main(argv):
    
    mass = 0.0
    fat = 0.0
    rD = 0.0
    run_CunninghamEquation = False

    try:
        opts, args = getopt.getopt(argv, "f:c:")
    except getopt.GetoptError:
        print(sys.argv[1], ' -f <file> [-c <optional>]')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-f':
            fname = arg
        elif opt == '-c':
            run_CunninghamEquation = True

    thisdict = { "Wk": 0,
                 "FW": 0,
                 "mW": 0,
                 "bW": 0,
                 "MI": 0,
                 "rD": 0,
                 "rA": 0,
                 "ww": 0,
                 "IF": 0,
                 "Fr": 0,
                 "mr": 0,
                 "Fl": 0,
                 "ml": 0,
                 "FR": 0,
                 "mR": 0,
                 "FL": 0,
                 "mL": 0,
                 "FT": 0,
                 "mT": 0
    }
    
    fields = []
    rows = []

    with open(fname, 'r') as csvfile:
        #  creating a csv reader obj
        csvreader = csv.reader(csvfile)

        #  extracting field names through first row
#        fields = next(csvreader)

        #extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        #  get total num of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    #  printing the field names
#    print('Field names:' + ', '.join(field for field in fields))

    #  printing first 5 rows
    print('\nExtracted rows are:\n')
    for row in rows[-3:]:
        print(row)
        for i in range(len(row)):
            if row[i] in thisdict.keys():
                thisdict[row[i]] += float(row[i+1])
#                print("%s:%s" % (row[i], row[i+1]))
#        for col in row:
#            print("%10s" % col)
    print("\n\n")
    for k, v in thisdict.items():
        msg = "";
        
        if k == "Wk":
            mass = round(v / 3, 1)
            msg += "Weight (lbs):"
        if k == "FW":
            fat = round(v / 3, 1)
            msg += "Fat (%):"
        if k == "mW":
            msg += "Muscle (lbs):"
        if k == "bW":
            msg += "Bone (lbs):"
        if k == "MI":
            msg += "BMI:"
        if k == "rD":
            if run_CunninghamEquation:
                rD = CunninghamEquation(mass, fat)
                v = rD * 3
            msg += "DCI:"
        if k == "rA":
            msg += "Metabolic Age:"
        if k == "ww":
            msg += "Water (%):"
        if k == "IF":
            msg += "Viceral Fat:"
        if k == "Fr":
            msg += "Right Arm (%):"
        if k == "mr":
            msg += "Right Arm (lbs):"
        if k == "Fl":
            msg += "Left Arm (%):"
        if k == "ml":
            msg += "Left Arm (lbs):"
        if k == "FR":
            msg += "Right Leg (%):"
        if k == "mR":
            msg += "Right Leg (lbs):"
        if k == "FL":
            msg += "Left Leg (%):"
        if k == "mL":
            msg += "Left Leg (lbs):"
        if k == "FT":
            msg += "Core (%):"
        if k == "mT":
            msg += "Core (lbs):"

#        msg += str(round(v / 3, 1))
#        print(msg)
        print("{:20s} {:5.1f}".format(msg, round(v / 3, 1)))


if __name__ == '__main__':
    main(sys.argv[1:])
