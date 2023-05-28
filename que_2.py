""" Q2. Dictionary, what?
Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]
The program should return a dict of filename: type pairs
E.g.
f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]) should return
{
"abc.jpg": "image",
"xyz.xls": "spreadsheet",
"Text.csv": "unknown",
"123": "unknown"
} """

# Code
def get_file_type(extension_type_list, file_list):
    extension_types = {}
    result = {}

    # Parse the extension and type values
    for pair in extension_type_list.split(';'):
        extension, file_type = pair.split(',')
        extension_types[extension] = file_type

    # Determine file types for each file
    for file_name in file_list:
        extension = file_name.split('.')[-1]
        file_type = extension_types.get(extension, 'unknown')
        result[file_name] = file_type

    return result

# Test the function
extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
file_list = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_types = get_file_type(extension_type_list, file_list)
print(file_types)
