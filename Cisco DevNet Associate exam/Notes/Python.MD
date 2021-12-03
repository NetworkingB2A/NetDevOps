You can style you code with different types of standards. Two of the most popular are:
- Pep8 
- Black

The zen of python is the commandments of python. it can be accessed by typing <code> import this </code> in a python interpreter. 

You can use  <code>  help (module-name) </code> to find out how to use a module.

If you want to avoid doing a bunch of escape characters you can us the use a raw string. 

<code>\_\_name__</code> Specially named variable allowing us to detect whether a module is run as a script or imported into anther module.
When you call the module while in a python interpreter, the name of the module will print out. when you call the module from a bash shell, the name \_\_main__ will print out. 

if you add the following code the your script, when you call the module from a bash shell. you will be able to define a function that you want to have run right away.

<code>if \_\_name__ == '\_\_main__';  
&nbsp;&nbsp;&nbsp;&nbsp;module_name()</code>

if you import this module into a python interpreter, python will know just to import the functions and not call any of them. if you call this module into a bash shell python will call whatever function you define in your if statement. 


Check out how to use command line arguments. 



An non empty string will always return true.
Watch out for the following. it will return true, because what you are really saying is that if apples is equal to bananas or if peach print true.
if "apples" == "bananas" or "peach"
    print("this is true")
else:
    print ("this is false")

instead do the following. 
if "apples" in ["bananas", "peach"]
    print("this is true")
else:
    print ("this is false")




## Classes
What is an object?
A object is two things
- Attributes
  - data about a object
- Methods
  - What a object can really do


### Attributes
Class Attributes
- All instances of a object of the class type will receive this attribute
 example
In [1]: class Person(): 
   ...:   person_type = "Homosapien" 

adam = Person() 
adam.person_type
Out[2]: 'Homosapien'


Instance Attributes
This uses an initializer. This is unique to each object



class Person:
  person_type = "Homosapien" #this is a class attribute 
  def __init__(self, height, weight, sex):
        self.height=height #<<<< instance attribute
        self.weight=weight #<<<< instance attribute
        self.sex=sex       #<<<< instance attribute

What is a magic method?

A magic method is a special method that you can define to add 'magic' to your classes. you can add built in methods to you classes  
example  

error with no length method  
<code>
\>>> class Friends:
...     members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]
...   
\>>> my_list_friends = Friends()  
\>>> len(my_list_friends)  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'Friends' has no len()  
</code>  
no error with length method  

<code>
>>> class Friends:  
...     members=['Ross', "Phoebe",   'Chandler', 'Joey', 'Monica', "Rachel"]  
...     def __len__(self):  
...         return len(self.members)  
...

\>>> my_list_friends = Friends()  
\>>> len(my_list_friends)  
6
</code>

Here is another example. but this time I am trying to see if a name is in the list of friends  

\>>> class Friends:  
...     members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]  
...     def __len__(self):  
...         return len(self.members)  
...   
\>>> if 'adam' in my_list_friends:  
...     print ('adam is in the list')  
... else:  
...     print('adam is not a friend. :( ')  
...   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: argument of type 'Friends' is not iterable  
>>>   
KeyboardInterrupt  
>>>   

### Here is a version of the check to see if adam is a friend.  

\>>> class Friends:  
...     members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]  
...     def __len__(self):  
...         return len(self.members)  
...     def __contains__(self, friend):  
...         return friend in self.members  
...   
\>>> if 'adam' in my_list_friends:  
...     print ('adam is in the list')  
... else:  
...     print('adam is not a friend. :( ')  
...   
adam is not a friend. :( 


You can also do a string magic method and make your class look even prettier.
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

\>>> adam=Person(6,250,"Male")  
\>>> print(adam)  
I am a person, I am 6 ft tall, I weigh 250 lbs. I am also a Male   


Best practices
- Use uppercase letters for a class name
- Use self as the first positional argument. You could use others besides self, but don't do it. just use self.
