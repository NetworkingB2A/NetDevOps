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
