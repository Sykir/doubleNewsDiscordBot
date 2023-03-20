# doubleNewsDiscordBot

- install python 3
- install dependencies with

```python
pip install -r requirement.txt 
```

- run setScheduledTask.ps1 to run the bot at startup

## configuration for facebook

- https://developers.facebook.com/async/registration/dialog/
- create an app
- https://developers.facebook.com/tools/explorer
    - add permission
        - pages_manage_posts
        - pages_read_engagement
    - me?fields=accounts
        - get the id of the page
    - get page token