import random

def primary():
  print("Keep it Logically Awesome!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1 #No. of Lines in Quotes  File 
  rnd = random.randint(0, last)
  
  print(quotes[rnd])

if __name__== "__main__":
  primary()
