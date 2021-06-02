import random

def primary():  
  
  print("Here is the Quote of the Moment! ")

  quotes = open("quotes.txt").readlines()
  open("quotes.txt").close()
  
  last = len(quotes) - 1 #No. of Lines in Quotes File   
  
  print(" ", quotes[random.randint(0, last)])

if __name__== "__main__":
  primary()
