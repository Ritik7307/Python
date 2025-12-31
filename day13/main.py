# strings are immutable
a= " Ritik"
print(a.upper())
print(a.lower())

b= " !! DUSTIN !!!! !!!!!  DUSTIN"
print(b.strip(" !"))  # removes leading and trailing spaces and exclamation marks
print(b.replace("DUSTIN", "Dustin"))  # replaces DUSTIN with Dustin
print(b.split(" "))  # splits the string at spaces and returns a list

blogHeading = "welcome to day13 of python"
print(blogHeading.capitalize())  # Capitalizes the first letter of the string

print(b.count("DUSTIN"))  # counts occurrences of DUSTIN in the string