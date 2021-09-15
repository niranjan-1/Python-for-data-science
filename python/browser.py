import webbrowser

chrome= webbrowser.get('chrome %s').open_new_tab("https://www.python.org/")
# chrome.open_new("https://www.python.org/")

for i in range(1,20):
	if i == 12:
		continue
	print(i, end=" ")