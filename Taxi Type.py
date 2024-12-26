def taxi(number):
  if number < 11:
    return "It's Econom Car"
  elif number < 21:
    return "It's Comfort Car"
  else:
    return "It's Buisness Car"
  

print(taxi(30));