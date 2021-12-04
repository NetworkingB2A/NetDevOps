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


#my_list_friends = Friends()
#len(my_list_friends)

#if 'adam' in my_list_friends:
#    print ('adam is in the list')
#else:
#    print('adam is not a friend. :( ')

class Student:
  
  def __init__(self, name, studentnum):
    self._name = name
    self._studentnum = studentnum
  
  @property
  def name(self):
    return self._name
  
  @property
  def studentnum(self):
    return self

  @name.setter
  def name(self, name):
        if len(name) < 2:
              raise ValueError("Name must be at least 2 characters or more!")
        self._name = name

  @studentnum.setter
  def studentnum(self, studentnum):
        if not isinstance(studentnum, int):
              raise ValueError("Student number must be an integer")
        self._studentnum = studentnum



class StudentGrade:
      
  def __init__(self, grade):
      self._grade = grade 

  @property
  def grade(self):
        return self._grade

  @staticmethod
  def random_grade():
      return StudentGrade(random.choice(grades))



    """This first part is without the property decorator and you see you have to call the name as a function. """
#   In [8]: adam = Student("adam", 4567)                                                                                
#   
#   In [9]: adam.name()                                                                                                 
#   Out[9]: 'adam'
#   
#   In [10]: adam._name                                                                                                 
#   Out[10]: 'adam'
#   
#   In [11]: adam.name                                                                                                  
#   Out[11]: <bound method Student.name of <__main__.Student object at 0x7fb18c59d940>>
#   
"""This next part is with the property decorator and you no longer have to call it as a function """
#   In [13]: chewy = Student("Chewy", 123456789)                                                                        
#   
#   In [14]: chewy.name()                                                                                               
#   ---------------------------------------------------------------------------
#   TypeError                                 Traceback (most recent call last)
#   <ipython-input-14-bb72fd232431> in <module>
#   ----> 1 chewy.name()
#   
#   TypeError: 'str' object is not callable
#   
#   In [15]: chewy.name                                                                                                 
#   Out[15]: 'Chewy'
#   
#   In [16]: chewy._name                                                                                                
#   Out[16]: 'Chewy'
"""This next part is with the property setter, and will allow you to update the name without calling a function. """

# In [12]: bill = Student("bill", 123)                                                                                
# 
# In [13]: bill.name                                                                                                  
# Out[13]: 'bill'
# 
# In [14]: bill.name = "apple"                                                                                        
# 
# In [15]: bill.name                                                                                                  
# Out[15]: 'apple'

""" this part will show the use of a static method"""
# In [9]: class StudentGrade: 
#    ...:        
#    ...:   def __init__(self, grade): 
#    ...:       self._grade = grade  
#    ...:  
#    ...:   @property 
#    ...:   def grade(self): 
#    ...:         return self._grade 
#    ...:  
#    ...:   @staticmethod 
#    ...:   def random_grade(): 
#    ...:       return StudentGrade(random.choice(grades)) 
#    ...:                                                                                                             
# 
# In [10]: new_student = StudentGrade.random_grade()                                                                  
# 
# In [11]: new_student.grade                                                                                          
# Out[11]: 'A'
# 
# In [12]: new_student.grade                                                                                          
# Out[12]: 'A'
# In [17]: new_student = StudentGrade.random_grade()                                                                  
# 
# In [18]: new_student.grade                                                                                          
# Out[18]: 'B'
# 
# In [19]: new_student.grade                                                                                          
# Out[19]: 'B'
