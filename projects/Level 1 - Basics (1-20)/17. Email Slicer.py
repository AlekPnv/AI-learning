def main():
    while True:
        user_email = input("Enter email: ").strip()
        
        if user_email.count("@") != 1:
            print("Email must contain exactly one @")
            continue
        
        username, domain = user_email.split("@")       
        
        # check if empty
        if not username:
            print("Username cannot be empty")
            continue
        
        if not domain:
            print("Domain cannot be empty")
            continue
        
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        
        if input("Again? [y/n]: ").lower() != "y":
            break
        
if __name__ == "__main__":
    main()