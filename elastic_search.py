import random , requests
import subprocess

carnames = ["AUDI","HONDA","CITROEN","ACURA","BMW","LEXUS","FORD","FERARi","LAMBORGINI"]
years = ["1990","1993","1995","2006","2007","2015","2014"]
powers  = ["190","210","150","105","121","340","92","350"]
status = ["new","old"]
skills = ["great","power","confort","fast","nice","boaring"]


#subprocess.call
shell=True
for i in xrange(20000):
    carname = random.choice(carnames)
    year = random.choice(years)
    power = random.choice(powers)
    st = random.choice(status)
    skill = random.choice(skills)

    subprocess.call('curl -PUT \'http://localhost:9200/test_data/%s\' -d \'{"carname":"%s","year":"%s","power":"%s","state": "%s","skills":"%s"}\'' %(i+23,carname, year, power, st, skill),shell=True)
    #print ('curl -PUT \'http://localhost:9200/test_data/%s\' -d \'{"carname":"%s","year":"%s","power":"%s","state": "%s","skills":"%s"}\'' %(i+2,carname, year, power, st, skill))
