import json

with open("waitingSpirits.json") as file:
  data = json.load(file)
  res = []
  for i, height in enumerate(data):
    sight = 0
    later = []
    for new_h in data[i+1:]:
      later.append(new_h)
      if height > new_h:
        if new_h >= max(later):
          sight+=1
      else:
        sight+=1
        break
    res.append(sight)

  print(res)
      
    
