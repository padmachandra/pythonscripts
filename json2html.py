import json

with open('people.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    # Creating an HTML file
    Func = open("GFG-1.html","w")
    htmlStr = "<html>\n<head>\n<title> \nJSON to HTML \n\
           </title>\n</head> <body><h1></u></h1>\
           \n<table border='1'>\n"
    #print(fcc_data[0]['id'])
    htmlStr += "\n<tr>"
    for key in fcc_data[0]:
        htmlStr += "<th>"+key+"</th>"
    htmlStr += "\n</tr>"
    
        #break
    for value in fcc_data:
        htmlStr += "\n<tr>"
        for rows in value:
            htmlStr += "\n<td>"+value[rows]+"</td>"
            print(value[rows])   
        htmlStr += "\n</tr>"
   
# Adding input data to the HTML file
Func.write(htmlStr)
              
# Saving the data into the HTML file
Func.close()
