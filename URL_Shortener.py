import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
#Bitly shortener service
type_bitly = pyshorteners.Shortener(api_key='01b6c587cskek4kdfijsjce4cf27ce2')
short_url = type_bitly.bitly.short('https://www.google.com')
 
print("The Shortened URL is: " + short_url)
