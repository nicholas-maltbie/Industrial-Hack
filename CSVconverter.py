"""Reads in a CSV file, stores the data in a dictionary, and then prints out the output in a specialized form"""
dict = {'ip': [{'email': [], 'phone':[], 'address':[], 'name':[], 'location':('',''), 'threat':[]}]}

csvfile = open("example.csv")
print('IP: \tEmail: \tPhone: \tAddress: \tName: \tLocation: \tThreat: ')
for readLine in csvfile:
    line = readLine
    ipstr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    emailstr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    phonestr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    addressstr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    namestr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    latitudestr = line.substr(0, line.find('\t'))
    line = line.substr(line.find('\t'))
    longitudestr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    threatstr = line.substr(0, line.find(','))
    line = line.substr(line.find(','))

    dict.update({ipstr: [{'email'.append(emailstr), 'phone'.append(phonestr), 'address'.append(addressstr),
                          'name'.append(namestr), 'location'.append(latitudestr, longitudestr),
                          'threat'.append(threatstr)}]})

    print(ipstr + '\t' + emailstr + '\t' + phonestr + '\t' + addressstr + '\t' + namestr + '\t(' +
          latitudestr + ', ' + longitudestr + ')\t' + threatstr)