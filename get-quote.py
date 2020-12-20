import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])
# Don't change __main__
if __name__== "__main__":
  primary()
