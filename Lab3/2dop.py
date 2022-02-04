import re
tests = ["artur-stepanov-03@mail.ru",
         "sAtret@niuitmo.ru",
         "timurzykov@gmail.com",
         "dhfiheihgi@yandex.ru",
         "oao@oaocom",
         ".....@...",
         "@.e"]
for testnumber in range(len(tests)):
    str = tests[testnumber]
    exemple = re.match( r'(.[a-zA-Z0-9\-\_]*)\@(.[a-zA-Z0-9\-\_]*)\.(.[a-zA-Z0-9\-\_]*)', str, re.M|re.I)
    if exemple:
        print(exemple.group(2),'.',exemple.group(3), sep="")
    else:
        print("Fail!")
