class Person:
  person_type = "Homosapien" #this is a class variable 
  def __init__(self, height, weight, sex):
        self.height=height   #<<<< instance attribute
        self.weight=weight   #<<<< instance attribute
        self.sex=sex         #<<<< instance attribute
  def lb_to_kg(self):
      weight_in_kg = self.weight/2.205
      print(weight_in_kg)
  def dominate_hand(self, hand):
        if hand in ["right", "Right", "r", "R" ]:
          print("You are right handed")
        elif hand in ["left", "Left", "l", "L"]:
          print("You are left handed")
        else:
          print("You are no handed?")
  def __str__(self):
        return f"I am a person, I am { self.height } ft tall, I weigh {self.weight} lbs. I am also a {self.sex} "



class Friends:
    members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]
    def __len__(self):
        return len(self.members)
    def __contains__(self, friend):
        return friend in self.members


my_list_friends = Friends()
len(my_list_friends)

if 'adam' in my_list_friends:
    print ('adam is in the list')
else:
    print('adam is not a friend. :( ')