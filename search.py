import requests
import json 


user_input = input()
#making input into url ready thingy

x = '-'.join(user_input.split())
url = requests.get('https://www.dnd5eapi.co/api/spells/' + x)

#making it look pretty
pretty_spells = json.dumps(url.json(), indent=2)

#making it so I can get values from json 
resp = json.loads(pretty_spells)

print(resp['name'])
print(resp['range'])
#getting the components out of a list
components_list = resp['components']
components_strings = ''.join(str(x) for x in components_list)
print(components_strings)

#print only if it has a material component
if 'material' in resp:
    print(resp['material'])

print(resp['duration'])
print("Concentration: ", resp['concentration'])
print("Ritual: ", resp['ritual'])

#getting the description out of a list
description_list = resp['desc']
description_strings = ''.join(str(x) for x in description_list)
print(description_strings)

#getting higher levels out of a list
higher_level_list = resp['higher_level']
higher_level_strings = ''.join(str(x) for x in higher_level_list)
print(higher_level_strings)

print("Level: ", resp['level'])
print(resp['school']['name'])
