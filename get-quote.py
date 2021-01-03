import random

def primary():
  
  print("Here are the Quotes!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1 #No. of Lines in Quotes File   
  
  print(
    quotes[random.randint(0, last)],
    quotes[random.randint(0, last)],
    quotes[random.randint(0, last)],
    quotes[random.randint(0, last)],
    quotes[random.randint(0, last)],
    quotes[random.randint(0, last)]
    )

if __name__== "__main__":
  primary()
