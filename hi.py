import turtle, random

colors=["blue","red","yellow","cyan","orange","green","gray","pink","purple","white","GOLD","silver","firebrick","lime","palegreen","darksalmon","mediumspringgreen","crimson","darkslategray","goldenrod","seagreen","maroon","hotpink"]
turtle.width(10) #What does this line do?

length = 5

for count in range(1000):
  color = random.choice(colors) #Choose a random color
  turtle.forward(length)
  turtle.right(150)
  turtle.color(color) # Why is color spelt like this?
  length = length + 5
  
  
