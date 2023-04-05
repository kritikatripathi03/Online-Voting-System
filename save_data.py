#save the data received from the html form using html library
from flask import request
import csv
from flask import Flask, current_app

app = Flask(__name__)

with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)

def save_comment():
    # This is to make sure the HTTP method is POST and not any other
    if request.method == 'POST':
        # request.form is a dictionary that contains the form sent through
        # the HTTP request. This work by getting the name="xxx" attribute of
        # the html form field. So, if you want to get the name, your input
        # should be something like this: <input type="text" name="name" />.
        name = request.form['name']
        aadhaar = request.form['aadhaar']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # This array is the fields your csv file has and in the following code
        # you'll see how it will be used. Change it to your actual csv's fields.
        fieldnames = ['name', 'aadhaar', 'password', 'confirm_password']

        # We repeat the same step as the reading, but with "w" to indicate
        # the file is going to be written.
        with open("C:/Users/Admin/Desktop/OTP/OTP/nameList.csv",'w') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'name': name, 'aadhaar': aadhaar,'passwrod': password, 'confirm_password': confirm_password})

        # And you return a text or a template, but if you don't return anything
        # this code will never work.
        return 'Thanks for your input!'
if __name__ == '__main__':
    #call the function to save the data
    save_comment()


# Path: OTP\index.html
<!DOCTYPE html>
<html>
<head>
    <title>OTP</title>
</head>
<body>
    <form action="/save" method="POST">
        <input type="text" name="name" placeholder="Name" />
        <input type="text" name="aadhaar" placeholder="Aadhaar" />
        <input type="text" name="password" placeholder="Password" />
        <input type="text" name="confirm_password" placeholder="Confirm Password" />
        <input type="submit" value="Submit" />
    </form>
</body>
</html>

