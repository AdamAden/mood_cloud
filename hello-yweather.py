import yweather

client = yweather.Client()
place1 = raw_input("Name place 1: ")
place2 = raw_input("Name place 2: ")
place1_id = client.fetch_woeid(place1)
place2_id = client.fetch_woeid(place2)

print place1_id
print place2_id