import json
import random
import math

min = 300000
while True:
  with open('trickOrTreat.json') as file:
    locations = json.load(file)
    x = 0
    y = 0
    visited = []
    current_location = locations[0]
    total_distance = 0
    while len(locations) != 1:
      locations.remove(current_location)
      distances = [math.sqrt((e.get('x')-x)**2 + (e.get('y')-y)**2) for e in locations]
      dest = random.choices(locations, distances)[0]
     
      total_distance += math.sqrt((dest.get('x')-x)**2 + (dest.get('y')-y)**2) 
      x = dest.get('x')
      y = dest.get('y')
      visited.append(dest.get('id'))
      current_location = dest
    
    if total_distance < min:
      min = total_distance
      print(total_distance) 
      print(visited)
