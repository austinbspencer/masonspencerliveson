# Python program to convert text
# file to JSON


import os
import json


class mydict(dict):
    def __str__(self):
        return json.dumps(self)


def linkFound(dict1, line):
    words = line.split()
    for word in words:
        if 'http' in word:
            dict1['links'].append({
                "title": "some title",
                "url": word
            })
    return dict1


jsonList = []


def makeJson(f):
    # the file to be converted
    filename = f

    dict1 = {
        "date": "",
        "year": "",
        "pfp": "pfp.jpeg",
        "author": "Mason Spencer Lives On",
        "url": "",
        "attachments": None,
        "links": [
        ],
        "message": [
        ]
    }

    with open(filename) as fh:

        for line in fh:

            # Add the date
            if line[:4] == 'date':
                dict1['date'] = line[5:].rstrip()

            # Add the year
            elif line[:4] == 'year':
                dict1['year'] = line[5:].rstrip()

            # Add attachments if there are any
            elif line[:4] == 'attch':
                dict1['attachments'] = line[5:].rstrip()

            # Add paragraph content
            elif line[0].isalpha():
                dict1['message'].append(
                    {'content': line.rstrip(), "type": "Paragraph"})
                if 'http' in line:
                    dict1 = linkFound(dict1, line)

            # Add bullet point content
            else:
                dict1['message'].append(
                    {'content': line[2:].rstrip(), "type": "Bullet"})
                if 'http' in line:
                    dict1 = linkFound(dict1, line)

        jsonList.append(dict1)


def main():
    directory = 'posts'
    posts = 0
    for _filename in os.listdir(directory):
        # checking if it is a file
        # if os.path.isfile(f):
        #     makeJson(f)
        posts += 1
    i = 1
    while i <= posts:
        file_name = 'posts/post' + str(i) + '.txt'
        makeJson(file_name)
        i += 1


if __name__ == '__main__':
    main()
    out_file = open("out.json", "w")
    json.dump(jsonList, out_file, indent=4, sort_keys=False)
    out_file.close()
