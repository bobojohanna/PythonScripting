
# Scenario: When to go to the beach:
# If it is not a weekday and you have more than half a tank 
# of gas and it is a summer day or the temperature is above 80 degrees




a = input( "Is it a week day? (yes or no)")
b = input("Is there less than half a tank of gas? (yes or no)")
c = input("Is it a rainy day (yes or no)")
temp = input("Is the temperature > than 80 degrees? (yes or no)")
response = ["Go to the beach", "Do not go to the beach"]
def beach_response():
 if a == "yes" and b == "yes" and c == "yes" and temp == "no" or a == "no" and b == "no" and c == "no" and temp == "yes":
   return print(response[0])
 else:
    print(response[1])
beach_response()