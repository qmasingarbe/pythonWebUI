# pythonWebUI
Simple local webUI for python with Flask

Make a modern and responsive UI in html/css/javascript while processing data in python.

## Web part
html file is in templates/index.html, css and javascript code are in static folder.
Communication to python is handled in pythonCom.js file.

### Call a python function in javascript
To call a python function via javascript, call the sendData() function
with an object as parameter. Object must look like : 
```
{
    'function_name': 'testFunc',
    'kwargs': {'arg1': 'puppy', 'arg2': 'booh'},
    'return_function' : 'populateText'
}
```
`function_name` is the exact name of the python function you want to call

`kwargs` (optionnal) are the key words arguments to be passed to python function

`return_function` (optionnal) is the name of the javascript function to be called when the python function will return. This function will get passed a javascript object with the returned data from python

## Python part
The communication and server is handle by main.py file. This is the file that should be executed to start everything.
This will also popup a new browser tab with the UI in it at startup

### closing the server
Server will be close automatically at refresh or quit of the tab via a onunload event in the javascript code.
If this doesn't suit you, remove those event in pythonCom.js and add a mecanic that do a get request to the page /quit to close the server.

### python functions
Python functions should be written in callable.py. They should accept the sane keyword arguments that will be given in javascript and return js Object like data (dict json serializable) 