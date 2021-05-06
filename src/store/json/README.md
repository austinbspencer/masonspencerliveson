# How to add posts to the Recent Posts page
Here are some instructions for adding posts to the recent posts page. You could also just check the posts.json file that already has several examples.

## Template to copy and paste
Below is a skeleton you can copy and paste into the posts.json file and it will be added to the page, note that the posts will display from top to bottom as they 
appear in the posts.json file

```bash
{
    "date": "January 22, 2021",
    "pfp": "pfp.jpeg",
    "author": "Mason Spencer Lives On",
    "url": "",
    "attachments": null,
    "links": [
        {
            "title": "",
            "url": ""
        }
    ],
    "message": [
        {
            "content": "",
            "type": "Paragraph"
        },
        {
            "content": "",
            "type": "Bullet"
        }
    ]
}
```

## Template with comments
Below is the template with comments on what to put in the fields and where to find them

```bash
{
    "date": "January 22, 2021",
    # this is a link straight from the public folder, notice pfp.jpeg is in there
    "pfp": "pfp.jpeg", 
    "author": "Mason Spencer Lives On",
    # link to the post which you can get by clicking on the timestamp below post author and copying URL that takes you to follow this url to see an example
    "url": "https://www.facebook.com/permalink.php?story_fbid=1565912810285486&id=418764678333644",
    # If there is a photo attached at the end of the post then you need to add the photo to public and put the name in there
    "attachments": "henry.jpeg",
    "links": [ # This is any link that is put into the post content, there can be multiple or none, if none just do links: []
        {
            "title": "Donate",
            "url": "https://ilprairiecf.org/mason-spencer-lives-on-fund"
        }
    ],
    "message": [ # Organize in order of the post so for example this post looks like this:

        # Please help us celebrate Mason’s 15 years on earth at what should be his 21st birthday with a donation to the foundation.
        
        # - To donate online click on the donate button AT THE BOTTOM of the Fund description: https://ilprairiecf.org/mason-spencer-lives-on-fund 
        # **it should say Mason Spencer Lives On in your PayPal donation window or you have clicked the incorrect donate button

        # Details about the foundation. Each year the foundation gives a $500 scholarship to a graduating TV student, $75 award to an 8th grade 
        # basketball player, and to date has contributed $20,000 to Cincinnati Children’s for research. We choose the projects the funds are directed to. 
        # We target ones which would benefit those in Mason’s situation (with XIAP or GVHD related). The projects chosen to date are:

        # - Graft Versus Host Disease Research  (Helped fund the Mice portion which was unfunded) There was a funded project to validate a human peripheral 
        # blood screening test for acute GVHD (to detect it before symptoms develop), but an unfunded related project to develop the same test in mice and 
        # test different treatments in transplanted mice using the same blood test to detect acute GVHD before it develops.  They were doing this so that 
        # hopefully they were successful and hopefully had human trial of pre-emptive treatment in patients with positive screening results in a few years, 
        # would know what agents to use/what should work best



        # Separate in the order the conent appears
        {
            "content": "Please help us celebrate Mason’s 15 years on earth at what should be his 21st birthday with a donation to the foundation.",
            "type": "Paragraph"
        },
        {
            "content": "To donate online click on the donate button AT THE BOTTOM of the Fund description: https://ilprairiecf.org/mason-spencer-lives-on-fund **it should say Mason Spencer Lives On in your PayPal donation window or you have clicked the incorrect donate button",
            "type": "Bullet"
        },
        {
            "content": "Details about the foundation. Each year the foundation gives a $ 500 scholarship to a graduating TV student, $ 75 award to an 8th grade basketball player, and to date has contributed $ 20,000 to Cincinnati Children’s for research. We choose the projects the funds are directed to. We target ones which would benefit those in Mason’s situation (with XIAP or GVHD related). The projects chosen to date are:",
            "type": "Paragraph"
        },
        {
            "content": "Graft Versus Host Disease Research  (Helped fund the Mice portion which was unfunded) There was a funded project to validate a human peripheral blood screening test for acute GVHD (to detect it before symptoms develop), but an unfunded related project to develop the same test in mice and test different treatments in transplanted mice using the same blood test to detect acute GVHD before it develops.  They were doing this so that hopefully they were successful and hopefully had human trial of pre-emptive treatment in patients with positive screening results in a few years, would know what agents to use/what should work best",
            "type": "Bullet"
        }
    ]
}

```