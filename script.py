import requests
import re
from urllib.request import urlopen
from tkinter import filedialog
import os.path

#get url from a user
print("Unesite punu URL adresu predmeta: \n")
print("Primer :\n")
print("https://blanketi.sicef.info/elfak/155-distribuirani-sistemi")

url = input()
download_url = "https://blanketi.sicef.info"

#get which files to download from a user
print("Da li zelite 1-usmeni/2-pismeni/3-oba (unesite zeljeni broj)")

num = int(input())

#entire html page into string
response = urlopen(url)
html_bytes = response.read()
html = html_bytes.decode("utf-8")

#get url to download specific file
pattern = "<a.*?>preuzimanje.*?</a.*?>"
match_results = re.findall(pattern, html, re.IGNORECASE)
links = match_results
downloading = "Preuzimanje"

if num == 3:
	folder =filedialog.askdirectory(initialdir=os.path.expanduser('~'))
	print("Preuzimanje oba blanketa...")
	#download every file
	for link in links:
		link = re.search('/elfak/download/.*?"', link)
		link = link.group(0)
		link = link[:-1]
		final_url = download_url + link
		
		#download file from link
		r = requests.get(final_url, allow_redirects=True)
		response = urlopen(final_url)
		filename = response.headers.get_filename()
		if(filename):
			fullname = os.path.join(folder, filename)
			open(fullname, 'wb').write(r.content)
			print(downloading + '->' + filename)
		else:
			fullname = os.path.join(folder, "Random_ime")
			open(fullname, 'wb').write(r.content)
			print(downloading + '-> Random_ime')
	os._exit(0)
		

if num == 1:
	folder =filedialog.askdirectory(initialdir=os.path.expanduser('~'))
	print("Preuzimanje usmenih blanketa...")
	#download every file
	for link in links:
		link = re.search('/elfak/download/.*?"', link)
		link = link.group(0)
		link = link[:-1]
		final_url = download_url + link
		
		#download file from link
		r = requests.get(final_url, allow_redirects=True)
		response = urlopen(final_url)
		filename = response.headers.get_filename()
		
		if(filename):
			#check if file is u or p or pu
			u = filename[-7:-4]
			if(u[-1] == "."):
				u = u[:-1]
			if(u == " u" or u == "pu" or u == "- u" or u == " pu"):
				fullname = os.path.join(folder, filename)
				open(fullname, 'wb').write(r.content)
				print(downloading + '->' + filename)
		else:
			fullname = os.path.join(folder, "Random_ime")
			open(fullname, 'wb').write(r.content)
			print(downloading + '-> Random_ime')
	os._exit(0)

if num == 2:
	folder =filedialog.askdirectory(initialdir=os.path.expanduser('~'))
	print("Preuzimanje pismenih blanketa...")
	#download every file
	for link in links:
		link = re.search('/elfak/download/.*?"', link)
		link = link.group(0)
		link = link[:-1]
		final_url = download_url + link
		
		#download file from link
		r = requests.get(final_url, allow_redirects=True)
		response = urlopen(final_url)
		filename = response.headers.get_filename()
		
		if(filename):
			#check if file is u or p or pu
			p = filename[-7:-4]
			if(p[-1] == "."):
				p = p[:-1]
			if(p == " p" or p == "pu" or p == "- p" or p == " pu"):
				fullname = os.path.join(folder, filename)
				open(fullname, 'wb').write(r.content)
				print(downloading + '->' + filename)
		else:
			fullname = os.path.join(folder, "Random_ime")
			open(fullname, 'wb').write(r.content)
			print(downloading + '-> Random_ime')
	os._exit(0)
	

