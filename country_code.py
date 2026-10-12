country_code={"India":"0091",
              "Australia":"0025",
              "Nepal":"00917"}

print("The country of code of Australia is: ")
print(country_code.get("Australia","Not Found"))

print("The country of code of Japan is: ")
print(country_code.get("Japan","Not Found"))