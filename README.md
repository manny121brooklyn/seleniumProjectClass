# seleniumProject

Selenium Python 

How to build XPATH web element locator using text() or contains(text()='') methods

HTML: <span class="mr-3">Click Button to see alert </span>

Using text of the element to build the xpath:
Option 1: //span[text()='Click Button to see alert']
Option 2: //*[text()='Click Button to see alert'] - - Use * instead of span
Option 3: //span[contains(text(), 'Click Button to')]
Option 4: //*[contains(text(), 'Click Button to')]



