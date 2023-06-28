capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'Spain': 'Madrid',
            'Russia': 'Moscow'}

capitals.update({'USA': 'Las vegas'})
capitals.update({'Germany': 'Berlin'})
capitals.pop('Spain')
capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany'))

#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())


for key, values in capitals.items():
    print(key, values)




