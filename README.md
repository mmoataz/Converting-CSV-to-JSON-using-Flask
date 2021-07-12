# Converting-CSV-to-JSON-using-Flask
This code is reponsible for converting CSV file to JSON file using Flask

The used libraries are JSON, CSV, Flask, and Flask_restful libraries in python

The function is a get function that contains all the logic of our code as follows:
1- The file is opened and read using open function and all its data is converted into dictreader
2- We initialize an empty dictionary that will hold the output
3- A loop is conducted on every line in the file and every line is added to the dictionary declared before with the line ID
4- The last step is saving the output to the file "out1.json" that will contain the dictionary formed after converting it to an object (string)

- To run the code just open main.py and run it
- Use http://127.0.0.1:5000/questions to see the output response and see the file out1.json in the same directory you run from

Thank you :)
