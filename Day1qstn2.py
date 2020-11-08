#initialised a dictionary
Country = {
    #Gold, Silver, Bronze
	'IND': [8,4,4],
	'RSA': [4,4,4],
	'USA': [6,0,9],
	'FRA': [4,0,4],
	#if Gold medals are same then silver is counted, then bronze
	
}

sort_Country = sorted(Country.items(), key=lambda x: x[1], reverse=True)

for i in sort_Country:
	print(i[0])
