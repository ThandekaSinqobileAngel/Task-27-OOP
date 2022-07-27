class Email:
    self.has_been_read = False
    self_is_spam = False
    
    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.email_contents = email_contents
        
        def mark_as_read(self):
          self.has_been_read = True
        
    def mark_as_spam(self):
        self.is_spam = True

    inbox = []
      
    def add_email(Email, email_contents, from_address):
        inbox.append(Email(email_contents, from_address))
        
    def get_count(inbox):
        return len(inbox)
    
    
    def get_email(inbox,index_email):
        inbox[index_email].mark_as_read()
        return inbox[index_email].email_contents
        
    def get_unread_email (inbox):
        unread_inbox = []
        for email in inbox:
            if email.has_been_read == False:
                unread_inbox.append(email)
        
    def get_spam_emails (inbox):
        spam_list = []
        for email in inbox:
            if email.mark_as_spam():
                spam_list.append(email)
        
        
    def delete (inbox, index_email):
        return inbox.pop(index_email)
        
userChoice = ""    
while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?").lower()
    if user_choice == "read":
        print(int(input("Enter index of email you want to read: ")) 
        print(get_email(inbox, index_email))
    elif user_choice == "mark spam":
        print(get_spam_emails(inbox))
    elif user_choice == "send":
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email content: ")
        print(add_email(Email, email_contents, from_address))
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
