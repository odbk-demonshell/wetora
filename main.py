#!/usr/bin/env python
import sys
from printer import printer
from transformations import transformations

info = printer()
info.banner("Wetora","ODBK", " DEMONSHELL ")

# Defining a target 
if len(sys.argv) == 2: 
    target = sys.argv[1]
    info.highlight("Target: ", target)
else: 
    print("Invalid ammount of Argument") 

'''
## BEGIN ##
'''
# FROM DOMAIN TO ORGANIZATION NAME
scope = transformations()
try:
    name = scope.domainToOrg(target)
    if( name ):
        info.highlight("Organization Name: ", name)
    else:
        info.ehighlight("Organization Name: ", "NULL")
        info.equit()

except:
    info.error("  WHOIS ERROR  ")
    info.equit()

# FROM ORG NAME TO NAMELIST
try:
    print("Searching similars organizations: ")
    nameList = scope.orgToNameList("google")
    if( nameList ):
        #Clearing duplicates
        nameList = list(dict.fromkeys(nameList))
        for number, name in enumerate(nameList):
            info.highlight("["+str(number)+"] - ", name)
        #Remove unwanted organizations
        remove = list(map(int, input("Do you want remove any item? ").split(",")))
        nameList = [i for j, i in enumerate(nameList) if j not in remove]
        for number, name in enumerate(nameList):
            info.highlight("["+str(number)+"] - ", name)
    else:
        info.ehighlight("Similars Organizations: ", "NULL")
        info.equit()

except:
    info.error("  ERROR GETTING LIST  ")
    info.equit()


