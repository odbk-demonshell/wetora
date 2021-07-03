#!/usr/bin/env python
import sys
from printer import printer
from transformations import transformations

info = printer()
info.banner("Wetora","ODBK", "DEMONSHELL")

# Defining a target 
if len(sys.argv) == 2: 
    target = sys.argv[1]
    info.highlight("Target: ", target)
else: 
    print("Invalid ammount of Argument") 

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