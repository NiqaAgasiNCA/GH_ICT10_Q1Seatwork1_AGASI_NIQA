from pyscript import display, document


first_name = "Niqa"
last_name = "Agasi"
age = 14
height = 149

display(type(first_name), target='result')
display (f'Hello! my name is <i>{first_name} {last_name}.</i> I am {age} years old and my height is {height} cm.', target='result')

document.getElementById('result').innerHTML = f'Hello! my name is <i>{first_name} {last_name}.</i> I am {age} years old and my height is {height} cm'

string_sample = ["Japan", "Indonesia", "France"]

document.getElementById('result').innerHTML += f'<br>Some countries I would like to visit are:{string_sample}'

student_type = False 

things_about_self = {
    "favorite_color": "Purple",
    "car_brand": "Ford",
    "shoe_size": 8,
    "best_friend": "Chloe Delos Reyes"
}

display(f'My favorite color is {things_about_self["favorite_color"]}, my car brand is {things_about_self["car_brand"]}, my shoe size is {things_about_self["shoe_size"]}, and my best friend is {things_about_self["best_friend"]}.', target='result')

favorite_fruits = "Mango, Grapes, Pomelo, Watermelon and Honeydew"
display(f'My favorite fruits are: {favorite_fruits}.', target='result')    

#line 30 is a string variable

days_in_a_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
display(f'The days of the week are: {days_in_a_week}.', target='result')

# line 34 is a tuple variable
