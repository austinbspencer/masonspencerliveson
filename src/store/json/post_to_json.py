# Python program to convert text
# file to JSON


import os
import json


class mydict(dict):
    def __str__(self):
        return json.dumps(self)


def linkFound(line):
    words = line.split()
    for word in words:
        if 'http' in word:
            dict1['links'].append({
                "title": "some title",
                "url": word
            })


# directory = 'posts'
# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         print(f)

# the file to be converted
filename = 'post.txt'

# resultant dictionary
dict1 = {
    "date": "",
    "year": "",
    "pfp": "pfp.jpeg",
    "author": "Mason Spencer Lives On",
    "url": "",
    "links": [
    ],
    "message": [
    ]
}

# fields in the sample file
fields = ['name', 'designation', 'age', 'salary']

with open(filename) as fh:

    # count variable for employee id creation
    l = 1

    for line in fh:

        if line[:4] == 'date':
            dict1['date'] = line[5:].rstrip()

        elif line[:4] == 'year':
            dict1['year'] = line[5:].rstrip()

        elif line[0].isalpha():
            dict1['message'].append(
                {'content': line.rstrip(), "type": "Paragraph"})
            if 'http' in line:
                linkFound(line)

        else:
            dict1['message'].append(
                {'content': line[2:].rstrip(), "type": "Bullet"})
            if 'http' in line:
                linkFound(line)


print(mydict(dict1))
