import pyshorteners
url = input("Enter your URL")
shorted_url = pyshorteners.Shortener().tinyurl.short(url)
print("Your shorted url is -", shorted_url)