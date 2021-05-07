'''
Python program to convert files to JSON
Specifically for use in masonspencerliveson webpage
Built to take Facebook posts and create JSON for displaying in the webpage


Austin Spencer - 05 / 06 / 2021
'''

import os
import json
import time


class mydict(dict):
    def __str__(self):
        return json.dumps(self)


def linkFound(dict1, line, links):
    '''
    Helper function that will be called when 'http' is found in the file line
    This will assume the word with 'http' in it is a link and will replace the link with phrase below
    Will also add to the dict1 with the link url and the title of the link based on how many links found
    in the current file
    '''
    words = line.split()
    for word in words:
        if 'http' in word:
            links += 1  # increment links which keeps track of the number of links found in THIS file
            line = line.replace(
                word, f'**The link is "Link {links}" at the bottom of this post!**')
            dict1['links'].append({
                "title": f"Link {links}",
                "url": word
            })
    return dict1, line


def makeJson(filename):
    '''
    makeJson will take a file and iterate through it and append to / edit dict1 with the content of the file
    Once completed iterating the entire file returns the updated dict1 dictionary

    Param(filename) : name of file to be converted to dictionary
    Return : dictionary of the files content
    '''

    # Reset number of links
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

            # Check for empty line and ignore the line if it's empty
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
                        dict1, line = linkFound(dict1, line, links)
                    dict1['message'].append(
                        {'content': line.rstrip(), "type": "Paragraph"})

                # Add bullet point content
                else:
                    if 'http' in line:
                        dict1, line = linkFound(dict1, line, links)
                    dict1['message'].append(
                        {'content': line[2:].rstrip(), "type": "Bullet"})

        # Close file after finished for best practice
        fh.close()

        # Return the updated dictionary
        return dict1


def main():
    # Initializing variables
    json_list = []
    directory = 'posts'
    posts = 0

    # Get total number of posts
    for _filename in os.listdir(directory):
        # checking if it is a file
        # if os.path.isfile(f):
        #     makeJson(f)
        posts += 1
    i = 1

    # Iterate through all posts
    while i <= posts:
        file_name = 'posts/post' + str(i) + '.txt'

        # Call helper function with bulk of the algorithm
        json_list.append(makeJson(file_name))

        # Output how far along the program is
        # Completely unecessary and the sleep is needed because it builds so fast
        if i % 5 == 0:
            pct = float(i / posts) * 100
            print(f'--> {pct}%')
            time.sleep(1)
        i += 1

    # Output 100% complete if the total posts isn't % 5
    if pct != 100.0:
        print('--> 100.0%')

    return json_list


if __name__ == '__main__':
    json_list = main()

    out_file = open("out.json", "w")

    # Dump the json into the new file without sort
    json.dump(json_list, out_file, indent=4, sort_keys=False)

    # Close the file for best practice
    out_file.close()
