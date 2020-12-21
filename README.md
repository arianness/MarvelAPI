# MarvelAPI
Script created to consumes the Marvel API
_____________________________________________________________________
Requirements:  

	Python 3.8
	To install module 'requests'
----------------------------------------------------------------------
How to use:

To use the "marvelapi" module, import it into your application:

	from marvelapi import Marvel 

Create a Marvel object and pass your authentication keys:

	example = Marvel(apikey="", privatekey="")

You can consume the API in two ways:
	1. Calling the method of the desired collection, passing the  
	filters through parameter (if any);
	2. Calling the method 'get', passign the desired colletion 
	name and filters.

1. Using the method by collection type: 
To get all elements of a collection, use the method without passing
no one parameter:

	result = example.characters() 
	result = example.events() 
	result = example.comics() 
	result = example.series() 
	result = example.stories() 

To get events, comics, stories or series from a specific character,
use the 'id' parameter in the method call:

	result = example.characters(id=1011333) 
	result = example.events(id=1011334)

To use filters, add the desired parameters in the method call:

	result = example.characters(name='Spider-Man', nameStartsWith='sp') 
 	result = example.events(id=1011334, orderBy='name', limit=5)
 	
2. Using the 'get' method.
To use the get method, you must pass the name of the desired colelction
and a dictionary containing the desird filters (if any):

	args = {'id' : '1011334', 'orderBy' : 'name', 'limit' : '5'}
	result = example.get('events', args)

If there aren't filters, you must pass an empty dictionary:

	result = exemple.get('events', {})

All methods will return an object of type <class 'requests.models.Response'>, 
or will return 'None' if there is an error in execution.  

Look are some options than you can explore in your request:

	print(result.text)
	print(result.content)
	print(result.url)

---------------------------------------------------------------------
