class person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def myfunction(self):
    print("Hello my name is" + self.name,self.age) 
p1 = person("alero", 21)
p1.age=100
p1.myfunction()
 