letter = "Hey my name is {1} and I am from {0}"
country = "India"
name= "Dustin"

print(letter.format(country,name))
print(f"Hey my name is {{name}} and I am from {{country}}")
print(f"Hey my name is {name} and I am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09908482))
