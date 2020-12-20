def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])
# Don't change __main__
if __name__== "__main__":
  primary()
