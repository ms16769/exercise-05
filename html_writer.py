#!/usr/bin/env python3

import csv
print ("Program start")
def read_html():
    """
        Read the HTML template file into a string
    """
    with open("template.html") as htmlfile:
        htmlstring = htmlfile.read()
        return htmlstring


def read_csv(filename):
    """
        Read a csv file and produce a list of lists with each
        inner list representing a row in the csv file:
        [ [first, last, email], [first, last, email], ...]
    """
    result = []
    with open(filename) as csvfile:
        ### EDIT BELOW HERE ###
		#pass
        result = csv.reader(csvfile, delimiter=";")
		
		#pass
        ### EDIT ABOVE HERE ###
	#result = list(reader)
    return result


def csv_to_html(csvdata):
    """
        Expects csvdata to be a list of lists:
        [ [first, last, email], [first, last, email], ...]

        Returns a string with the HTML <tbody> contents for
        each row in the csv file:
        <tr><td>First name</td><td>Last name</td><td>E-Mail</td></tr>"
    """
    htmlstring = ""
    ### EDIT BELOW HERE ###
    htmlstring = "<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n"
   # pass
    ### EDIT ABOVE HERE ###

    return htmlstring


def combine_template_with_data(template_string, htmldata):
    """
        Combine the HTML template string with the generated
        tabular data.
    """
    ### EDIT BELOW HERE ###
    return ""
    ### EDIT ABOVE HERE ###


def write_html(htmlstring):
    """
        Write the resulting HTML file
    """
    with open("result.html", "w") as htmlfile:
        htmlfile.write(htmlstring)


def main():
    """ 
        This is the main function of the program
    """
    template_string = read_html()
    csvdata = read_csv("test.csv")
	htmldata = csv_to_html(csvdata)
    fullstring = combine_template_with_data(template_string, htmldata)
    write_html(fullstring)

if __name__ == "__main__":
    main()
