# How to add posts to the Recent Posts page
Here are some instructions for adding posts to the recent posts page.


## Adding the post
Add a post to the posts folder with the sequential number. src/store/json/posts

- Here is the template for the post{num}.txt file
```bash
date January 18
year 2021
dat3 2021-01-18
url https://www.facebook.com/permalink.php?story_fbid=1563570430519724&id=418764678333644
attc https://scontent.fphx1-2.fna.fbcdn.net/v/t1.6435-9/140154441_1563570083853092_7172133497388044043_n.jpg?_nc_cat=100&_nc_map=control&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=Ky7znRBdEKsAX_9_8JF&_nc_ht=scontent.fphx1-2.fna&oh=8b8b1c340188c51b387eb5f5fb62b756&oe=60BB8489

copy and paste post here
```

## How to get the Facebook url and attc
- To get the url click the date below Mason Spencer Lives On in the post
    - This will take you to a new page with a facebook.com/permalink that you copy and paste the url
- If there are image attachments to the post
    - Click on **ONE** image that you want to display on the website
        - Right click the image and choose to copy the image address
    - If there are several photos attached in the post you can add at the end of the post a statement mentioning to click the facebook link for more photos


### Running Python Script
Follow these commands in terminal to run the script

```bash
# Get into correct directory
cd src/store/json

# Execute the script
python post_to_json.py
```