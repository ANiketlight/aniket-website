
import numbers
from tkinter import Y
import phonenumbers 
from phonenumbers import carrier, geocoder , timezone


x=0
for x in range (2):


    mobilenp= input("enter mobile number and country code :")
    mobilenp=  phonenumbers.parse(mobilenp)

    print(timezone.time_zones_for_number(mobilenp))


    print(carrier.name_for_number(mobilenp,"en"))

    print(geocoder.description_for_number(mobilenp,"en"))

 

    print("checking possiblity of number :",phonenumbers.is_possible_number(mobilenp))

    if x == 2:
        input("for exit type :", Y,"or not press N")
        if input== Y :
            break
        else :
            continue

    

    
