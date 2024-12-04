# InputLength Program

# Sets Banner as ASCII Art

banner = """ 
##     ## ######## ##       ##        #######  ###  
##     ## ##       ##       ##       ##     ## ###  
##     ## ##       ##       ##       ##     ## ###  
######### ######   ##       ##       ##     ## ###  
##     ## ##       ##       ##       ##     ##      
##     ## ##       ##       ##       ##     ## ###  
##     ## ######## ######## ########  #######  ###  
 """

# Shows Banner
print(banner)
# Prompt user for their favorite quote
quote = input("What is your favorite quote? ")

# Calculate the number of characters in the quote
length = len(quote)

# Print the result
print(f"That quote has {length} characters.")
