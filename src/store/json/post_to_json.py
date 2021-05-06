# Python program to convert text
# file to JSON


import os
import json


class mydict(dict):
    def __str__(self):
        return json.dumps(self)


jsonList = []
links = 0


def linkFound(dict1, line):
    words = line.split()
    global links
    for word in words:
        if 'http' in word:
            links += 1
            line = line.replace(
                word, f'**The link is "Link {links}" at the bottom of this post!**')
            dict1['links'].append({
                "title": f"Link {links}",
                "url": word
            })
    return dict1, line


def makeJson(f):
    # the file to be converted
    filename = f

    # Reset number of links
    global links
    links = 0

    # After running no values should be left as default
    dict1 = {
        "date": "default",
        "year": "default",
        "pfp": "pfp.jpeg",
        "author": "Mason Spencer Lives On",
        "url": "default",
        "attachments": None,
        "links": [
        ],
        "message": [
        ]
    }

    with open(filename) as fh:

        for line in fh:

            # Check for empty line
            if line != "\n":

                # Add the date
                if line[:4] == 'date':
                    dict1['date'] = line[5:].rstrip()

                # Add the year
                elif line[:4] == 'year':
                    dict1['year'] = line[5:].rstrip()

                # Add attachments if there are any
                elif line[:4] == 'attc':
                    dict1['attachments'] = line[5:].rstrip()

                # Add the post url
                elif line[:3] == 'url':
                    dict1['url'] = line[4:].rstrip()

                # Add paragraph content
                elif line[0].isalpha():
                    if 'http' in line:
                        dict1, line = linkFound(dict1, line)
                    dict1['message'].append(
                        {'content': line.rstrip(), "type": "Paragraph"})

                # Add bullet point content
                else:
                    if 'http' in line:
                        dict1, line = linkFound(dict1, line)
                    dict1['message'].append(
                        {'content': line[2:].rstrip(), "type": "Bullet"})
            else:
                print('empty line ignored')

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
