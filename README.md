# seleniumProject

How to build XPATH web element locator using text() or contains(text()='') methods
xpath = //Tag[@attribute='value']

HTML: <span class="mr-3">Click Button to see alert </span>

Using text of the element to build the xpath:
Option 1: //span[text()='Click Button to see alert']
Option 2: //*[text()='Click Button to see alert'] - - Use * instead of span
Option 3: //span[contains(text(), 'Click Button to')]
Option 4: //*[contains(text(), 'Click Button to')]


# CSS selector
# Method                    Target Syntax                   Example
Tag and ID                  css=tag#id                      css=input#email
Tag and Class               css=tag.class                   css=input.inputtext
Tag and Attribute           css=tag[attribute=value]        css=input[name=lastName]
Tag, Class, and Attribute   css=tag.class[attribute=value]  css=input.inputtext[tabindex=1]  

# tag and id – CSS Selector
css=tag#id 
tag = the HTML tag of the element being accessed 
'#' = the hash sign. This should always be present when using a Selenium CSS Selector with ID
id = the ID of the element being accessed

Eg. Facebook.com, let's examine the “Email or Phone” text box.
# <input id='email' ... name = 'email'>
Take note that the HTML tag is 'input' and its ID is 'email', so ourt syntax will be 'css=input#email'.

# tag and class – CSS Selector
CSS Selector in Selenium using an HTML tag and a class name is similar to using a tag and ID, 
but in this case, a dot (.) is used instead of a hash sign.

# Syntax 
css=tag.class 

tag = the HTML tag of the element being accessed
.= the dot sign. This should always be present when using a CSS Selector with class
class = the class of the element being accessed

Let's inspect the “Email or Phone” text box. Notice that its HTML tag is “input” and its class is 
“inputtext _55r1 _6luy.”
Let's build CSS selector using Tag and Class:
'css=input.inputtext _55r1 _6luy'

# tag and attribute – CSS Selector
Syntax
css=tag[attribute=value] 

Navigate to http://demo.guru99.com/test/newtours/register.php and 
and inspect the “Last Name” text box. Take note of its HTML tag 
(“input” in this case) and its name (“lastName”).

So the CSS selector will be:
css=input[name=lastName]

## tag, class, and attribute – CSS Selector
Syntax:
css=tag.class[attribute=value]
Eg.css=input.inputtext _55r1 _6luy[autofocus=1]
tag = input
class = inputtext _55r1 _6luy
[attribute=value] = [autofocus=1]

# Find out more about CSS selector at:
https://www.guru99.com/locators-in-selenium-ide.html

# Demo automation site Mercury Tours:
https://demo.guru99.com/test/newtours/register.php


### WebElement class: Alerts

''' python
'''
# switct to alert
alert = driver.switch_to.alert()

# get the text from alert 
alert_text = alert.text  #text is a property
#methods 
alert.accept() #clicking OK button 
alert.dismiss() #click Cancel button 
alert.send_keys() #enter a text on the alert box