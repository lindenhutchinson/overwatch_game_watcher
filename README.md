# Screen Watcher

Python script that can detect when your game has started and email you a notification.

Allows you to go and make a cup of tea while queueing for a game of Overwatch without wondering if you're about to be kicked for afk


### how to use

Create a virtual environment and install dependencies

```
virtualenv venv

source venv/scripts/activate 

pip install -r requirements.txt
```

Create a .env file with the same format as .env.example

To generate the E_PASS and E_KEY value, run password_manager.py

Use the password for your SENDER_EMAIL

Copy the generated values into your .env file

The SENDER_EMAIL and RECEIVER_EMAIL can be the same or different

Using a gmail account will require you to disable safe login protection

If possible, create a new account to be used as the sender email


*storing the encryption key and encrypted password next to each other isn't very secure. It's only a small step up from storing it in plaintext*

### what it does

The script takes a screenshot of your screen every SLEEP_TIME_S seconds

It then takes the average colour of the screenshot and compares it to the previous screenshot

If the difference between their average colours is greater than COLOUR_DIFF_THRESHOLD, an email is sent to RECEIVER_EMAIL and the script ends

There is a time out on the script to stop the loop after MAX_ATTEMPTS




