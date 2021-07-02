#!/usr/bin/env python
import sys
from printer import printer
from transformations import transformations

intro = printer()
intro.banner("Wetora","ODBK", "DEMONSHELL")

# Defining a target 
if len(sys.argv) == 2: 
    target = sys.argv[1]
    print("Target: "+ target)
else: 
    print("Invalid ammount of Argument") 

scope = transformations()
scope.domainToOrg(target)