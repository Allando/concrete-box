#!/bin/python

yn = " [y/n] "


# Chapter 0: Incarnation

firstQuestion = input("If I told you the world is under siege, would you believe me?" + yn)

if firstQuestion == "y":
    secondQuestion = input("If I told you the world is under siege, would you care?" + yn )
    if secondQuestion == "y":
        print("Well... in that case let's get started.")
    else:
        print("In that case, I have no time for this.")
else:
    print("Forget I said anything.")


