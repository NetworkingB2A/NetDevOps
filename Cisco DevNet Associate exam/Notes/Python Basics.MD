You can style you code with different types of standards. Two of the most popular are:
- Pep8 
- Black

The zen of python is the commandments of python. it can be accessed by typing <code> import this </code> in a python interpreter. 

You can use  <code>  help (module-name) </code> to find out how to use a module.

If you want to avoid doing a bunch of escape characters you can us the use a raw string. 


Parts of a python program
Modules
- Modules are really just a piece code that you import into your program. everything you import is a module.
- Why use modules
  - Easier readability/maintainability
  - Low coupling/high cohesion
    - Modules should written in such a way that they do not have any interdependencies. 
  - Code reusability
  - Collaboration
functions
classes
methods

if you would to to find out more about a module or the methods use the following commands.
- help(module) or help(module.function)
- dir(module)



## list methods
|Method|What it does|
|-|-|
| list.append(element) | Add an element to the end of the list |
| list.clear() | Removes everything from the list |
| list.copy() | Returns a copy of the list. This would be useful when you want to copy the list and you dont just want to create a pointer to the old list. | 
| list.count(element) | shows the number of the elements with the specified value | 
| list.extend(alist) | adds the element of a list to the end of the current list |
| list.index() | Returns the index number of the fist element with a specified value | 
| list.insert(index, element) | Adds and element at a specified index value |
| list.pop(index) | Removes an element at a specific index position, or if not index position is provided, removes the last item on the list | 
| list.remove() | Removes a list item with a  specified value | 
| list.reverse() | Reverses the list order | 
| list.sort() | sorts the list alphabetically | 

## Sets notes
What is a set?
- It is an unordered grouping of data and is defined by using the curly braces of a dictionary, without the key:value pair.
- Sets by default are mutable.
- To join two sets your would use the | (pipe), just like a math equation.
- You can find the intersections of two sites with the &.
- One advantage is that Sets logic can be performed a lot quicker than list logic can be.



### Function Notes
Basic function rules
- Must not start with a number
- Must not be a reserved Python word, or a name that has already been used as a function or variable.
- Can be any combination of A-Z, a-z, 0-9, underscore or a dash.

IMPORTANT NOTE ABOUT FUNCTIONS
- Keyword augments will help you a lot.
- if you write a basic function without keywords you will have to pass detail in a very specific order.
  - Example - def( username, first_name, last_name). 
  - If you create this as a basic and you change the order of these names when you call the function, your program will not behave how you expect it to.
- Here is why you should use keyword arguments. A keyword argument is a name/value pair that you pass to a function.
- You might not know how many arguments to expect. Python allows you to use * and ** (often referred to as *args and **kwargs) to define any number of arguments or keyword arguments.
- *args is a single argument that you pass in to your function. REMEMBER *args is still a positional argument call for your function. **kwargs is a Key value pair that you would pass into your function.
- You can define a default value argument in case you have an empty value to send to a function.
- 

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



