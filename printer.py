#!/usr/bin/env python
import pyfiglet 
from sty import fg, bg, ef, rs

class printer:
	def banner(self, brand, user, team):
		ascii_banner = pyfiglet.figlet_format(brand) 
		print(ascii_banner)
		print("                 "+user+" "+bg(255,10,10)+ fg.black + team + fg.rs + bg.rs + "\r\n\r\n")
	
	def error(self, message):
		result = bg(255, 10, 10) + fg.black + message + fg.rs + bg.rs
		print(result)



#baz = ef.italic + 'This is italic text' + rs.italic
#qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
#qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs