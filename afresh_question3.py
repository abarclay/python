#!/usr/local/bin/python3

# You receive a phone bill and it seems abnormally high so you decide
# to check the bill for accuracy
# You download all the calls in CSV format
# Each line in the csv file is of the form
# duration,phoneNumber
# where duration is measured in hours:minutes:seconds
# and each number is of the form xxx-xxx-xxxx
#
# Report the total cost of the calls in cents according to the following
# rules
# For any call less than 5 minutes, the charge is 3 cents per second
# For any call of 5 minutes or greater, the charge is 50 cents for each
# whole or partial minute
# All calls to the phone number with the highest total duration are free
# If two numbers have the same duration, then only the numerically smaller
# phone number is the free one.

