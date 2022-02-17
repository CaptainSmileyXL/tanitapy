# tanitapy

Introduction:
-------------
This is a Python script that enables the user to extract the data from a Tanita
scale's SD card.

This has been tested to work on the BC-601 model.


Supported Platforms
-------------------
```
Tested on python 3.9.1 on OS X but should work on any platform that supports
the requierments listed below.
```

Usage:
------
```
I recommend you make the script executable (chmod 755 tanita.py) then you can:  
./tanita.py -f <file> [optional var]
OTHERWISE
python3 tanita.py -f <csv file> [optional] -c 0
-f <csv file>
-c 0 [enables questions to manually calculate DCI using Cunningham equation]

```
