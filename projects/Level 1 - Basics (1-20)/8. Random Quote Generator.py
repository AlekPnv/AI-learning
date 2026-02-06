import random

quotes = ["Code is like humor. When you have to explain it, it's bad.",
          "Programs must be written for people to read, and only incidentally for machines to execute.", 
          "First, solve the problem. Then, write the code.", 
          "Simple is better than complex.", 
          "Errors should never pass silently.", 
          "Talk is cheap. Show me the code.", 
          "Weeks of coding can save you hours of planning.", 
          "If it works, don't touch it.", 
          "There are only two hard things in Computer Science: cache invalidation, naming things, and off-by-one errors.", 
          "Any code of your own that you haven't looked at for six months might as well have been written by someone else."]

def quote_generator():
    not_seen_quotes = quotes.copy()
    
    while True: 
        quote = random.choice(not_seen_quotes)
        print(f"\n- {quote}")
        
        not_seen_quotes.remove(quote)
        
        if not not_seen_quotes:
            print("\nYou've seen all available quotes!")
            print("Ending programm...\n")
            break
        
        if input("\nGenerate another quote? [y/n]: ").lower() != "y":
            break
            
if __name__ == "__main__":
    quote_generator()