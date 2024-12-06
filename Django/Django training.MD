Example of a project vs a app
say you wanted to create a online shop, the apps might be products, cart, admin area and the project will tie them all together.



### Models
What is the blank= false and null= false used for?
```
null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django field types such as DateTimeField or ForeignKey will be stored as NULL in the DB.

blank determines whether the field will be required in forms. This includes the admin and your custom forms. If blank=True then the field will not be required, whereas if it's False the field cannot be blank.

The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

A few examples:

models.DateTimeField(blank=True) # raises IntegrityError if blank

models.DateTimeField(null=True) # NULL allowed, but must be filled out in a form
Obviously, Those two options don't make logical sense to use (though there might be a use case for null=True, blank=False if you want a field to always be required in forms, optional when dealing with an object through something like the shell.)

models.CharField(blank=True) # No problem, blank is stored as ''

models.CharField(null=True) # NULL allowed, but will never be set as NULL
CHAR and TEXT types are never saved as NULL by Django, so null=True is unnecessary. However, you can manually set one of these fields to None to force set it as NULL. If you have a scenario where that might be necessary, you should still include null=True.
```

What is the related_name used for?
```
The related_name attribute specifies the name of the reverse relation from the User model back to your model.

If you don't specify a related_name, Django automatically creates one using the name of your model with the suffix _set, for instance User.map_set.all().

If you do specify, e.g. related_name=maps on the User model, User.map_set will still work, but the User.maps. syntax is obviously a bit cleaner and less clunky; so for example, if you had a user object current_user, you could use current_user.maps.all() to get all instances of your Map model that have a relation to current_user.

The Django documentation has more details.

To disable creating the backwards relationship entirely, set related_name to "+".
```

### URLs(routes)
What are URLs?
Uniform resource locator is what you type into the address bar.
Used to send users to different pages on your website.
URL config/routes: URL-action mapping which ensure that certain results are achieved when certain URLs are entered by the user

### Views
What are views?
Views in django are not what you think they are. A view is not responsible for showing an output to an end user. They are used to take a request and produce a response to that end user. Really they seem more like a render handler. Some examples of tasks you might perform in the views module, at least in the real world include pull data from a database, transform data, send email, ect.

A view is really just a function that django will run when a request for a URL is asked for by the end user. can also be a class.

Next step you do is to map a URL to a view function. End user calls url in their browser which will, once we have completed the mapping between function and url, run the function on the server and give the end user the response from the function. The functions might load and prepare data for the database, run business logic like encrypt a password or prepare and return html code for your end users browser to render. 

### Path converters

The following path converters are available by default:

- str - Matches any non-empty string, excluding the path separator, '/'. This is the default if a converter isn’t included in the expression.
- int - Matches zero or any positive integer. Returns an int.
- slug - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.
- uuid - Matches a formatted UUID. To prevent multiple URLs from mapping to the same page, dashes must be included and letters must be lowercase. For example, 075194d3-6885-417e-a8a8-6c931e272f00. Returns a UUID instance.
- path - Matches any non-empty string, including the path separator, '/'. This allows you to match against a complete URL path rather than a segment of a URL path as with str.

## Notes 
- It is a good idea to do visual updates in the templates and not in the python logic. in the View remember that is core business logic not really a place to make the data look pretty.
- "Slugs" always look something like this: my-post-is-here => SEO-friendly unique identifiers

Planning a blog project
- the welcome page
  - `/`
  - load starting page which lists the latest blog posts and some welcome text
- The posts page
  - `/posts`
  - loads page which lists all blog posts
- the blog post
  - `/posts/my-first-post`
  - Load individual blog post page which shows full blog post
  - Should be a dynamic link. 
  - `/posts/<slug>`

### Django create vs save
In django there are a few different different ways to update a database. for this circumstance we are referring to object.objects.create vs object with object.save()
Here are two ways of adding an object to a table.
```python
from app_name.models import Device
#Option 1
network_device = Device(hostname="Router1", ip_address="192.168.1.1", vendor="ubnt")
network_device.save()

#Option 2
network_device_2 Device.Objects.create(hostname="Router2", ip_address="192.168.2.1", vendor="ubnt"))
```

Here is an excerpt from stack overflow explaining the difference.

The differences between Model() and Model.objects.create() are the following:


Model.save() does either INSERT or UPDATE of an object in a DB, while Model.objects.create() does only INSERT.

Model.save() does
- UPDATE If the object’s primary key attribute is set to a value that evaluates to True
- INSERT If the object’s primary key attribute is not set or if the UPDATE didn’t update anything (e.g. if primary key is set to a value that doesn’t exist in the database).