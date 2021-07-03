#!/usr/bin/env python
import pyfiglet 
from sty import fg, bg, ef, rs
import sys

class printer:
	def banner(self, brand, user, team):
		ascii_banner = pyfiglet.figlet_format(brand) 
		print(ascii_banner)
		print("                 "+user+" "+bg.blue+ fg.black + team + fg.rs + bg.rs + "\r\n\r\n")
	
	def error(self, message):
		result = bg(255, 10, 10) + fg.black + message + fg.rs + bg.rs
		print(result)

	def highlight(self, message, info):
		result =  message + fg.green + info + fg.rs 
		print(result)

	def ehighlight(self, message, info):
		result =  message + fg.red + info + fg.rs 
		print(result)

	def equit(self):
		result =   fg.red + "Quiting..." + fg.rs 
		print(result)
		sys.exit()



#baz = ef.italic + 'This is italic text' + rs.italic
#qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
#qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs