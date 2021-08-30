# pip install countryinfo
from countryinfo import CountryInfo

country_name = "India"    # country's name whose details need
a = CountryInfo(country_name)

#info_1 = a.calling_codes()
#print(info_1)

#info_2 = a.area()
#print(info_2)

#info_3 = a.borders()
#print(info_3)

#info_4 = a.currencies()
#print(info_4)

#info_4 = a.area()
#print(info_4)

# to run all the things in one go without writing much codes
info_10 = a.info()     # all the info about the country
for p,q in info_10.items():
    print(f"{p}       ---        {q}")
