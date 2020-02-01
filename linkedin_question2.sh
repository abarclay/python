#!/bin/sh

# Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information. The employee information endpoint is "/employee/<id>". Each employee record you retrieve will be a JSON object with the following keys:
#
#   - 'name'  refers to a String that contains the employee's first and last name
#
#   - 'title' refers to a String that contains the employee's job title
#
#   - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports
#
#
# Sample JSON API Response.
# Sample JSON
# # GET /employee/A123456789
# {
#  "name": "Flynn Mackie",
#  "title": "Senior VP of Engineering",
#  "reports": ["A123456793", "A1234567898"]
# }
#
# Write a function that will take an employee ID and print out the entire hierarchy of employees under that employee.
#
# For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.
#
#
#
# -----------Begin Sample Output--------------
# Flynn Mackie - Senior VP of Engineering
#   Wesley Thomas - VP of Design
#     Randall Cosmo - Director of Design
#       Brenda Plager - Senior Designer
#   Nina Chiswick - VP of Engineering
#     Tommy Quinn - Director of Engineering
#       Jake Farmer - Frontend Manager
#         Liam Freeman - Junior Software Engineer
#       Sheila Dunbar - Backend Manager
#         Peter Young - Senior Code Cowboy
#
# -----------End Sample Output--------------

# AWB NOTE: I switched to bash here
# mostly because I'm more comfortable using curl and I didn't know off-hand
# whether I could use google to determine which library to include
# in order to make http requests - turns out it is "requests"
# FYI: I struggled a little bit with vim mode in the coderpad... it isn't
# completely vi-like. For example, you can't hold down the "k" key to 
# move upwards

# During the test, the run button is disabled, so you can't actually
# test anything. This doesn't really jive with how I code
# Let’s say I had to build a binary tree to store integers.
# Literally, my first step would be to write a loop that prints out
# each of the integers in the list. I would run that to make sure it
# works, THEN I would add a function to print the tree (the tree
# that doesn’t exist yet), then I would write the insert statement
# with lots of debugging statements so I can see what it is doing to
# test my logic

# mock function because the rest api doesn't actually exist
callCurl()
{
	url=$1
	if echo $url |grep -w A123456789 >/dev/null
	then
		cat <<EOT
{
  "name": "Flynn Mackie",
  "title": "Senior VP of Engineering",
  "reports": ["A123456793", "A1234567898"]
}
EOT
	return
	fi

	if echo $url |grep -w A123456793 >/dev/null
	then
		cat <<EOT
{
  "name": "Wesley Thomas",
  "title": "VP of Design",
  "reports": ["A123456693", "A1234566898"]
}
EOT
	return
	fi

	if echo $url |grep -w A1234567898 >/dev/null
	then
		cat <<EOT
{
  "name": "Machinegun Kelly",
  "title": "VP of Banking",
  "reports": ["A123456693", "A1234566898"]
}
EOT
	return
	fi

	if echo $url |grep -w A123456693 >/dev/null
	then
		cat <<EOT
{
  "name": "Randall Cosmo",
  "title": "Director of Design",
  "reports": ["B123456693"]
}
EOT
	return
	fi

	# catch all
	cat <<EOT
{
  "name": "Jamie Ross",
  "title": "GIMP"
}
EOT
}

getEmployeeInfo()
{
    local id=$1
    local depth=$2
    if [ -z "$depth" ]
    then
       depth=0
    fi
    # I'm going to mock this out since the rest call doesn't
    # actually exist
    #curl http://www.linkedin.corp/api/employee/$id >/tmp/emp
    callCurl http://www.linkedin.corp/api/employee/$id >/tmp/emp

    empName=$(cat /tmp/emp| jq .name)
    empTitle=$(cat /tmp/emp| jq .title)
    # originally, didn't have this test and was getting an error from
    # jq about not being able to itterate over null
    # Actually surprised I got all the jq commands correct
    if grep reports /tmp/emp >/dev/null
    then
    	empReports=$(cat /tmp/emp| jq .reports[])
    else
    	empReports=""
    fi 
    x=0
    while [ $x -lt $depth ]
    do
	# originally used echo here and built-in doesn't support -n
      /bin/echo -n "  "
      x=`expr $x + 1`
    done
    echo "${empName} - ${empTitle}"
    for emp in $empReports
    do
      getEmployeeInfo $emp `expr $depth + 1`
    done
}

getEmployeeInfo A123456789

