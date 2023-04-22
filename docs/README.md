> This project is no longer being developed, and as such is being archived.

# Telegram Plex Bot

A bot to notify, control, manage (and more) Plex integration applications like Sonarr, Radarr, Ombi, etc.

*Implementation of more applications and features will occur overtime*

## Implemented Commands

- General
    - `/help`: Shows all commands available for the current user (based on their status)
- Account-Related
    - `/register`: Registers a user to the bot's sqlite database
        - `/start` is also an alias, so it is automatically executed when any user starts a conversation with the bot
    - `/account`: Account settings & information
        - Add/change Ombi ID
        - Change notification complexity
        - Change upgrade notification preference
    - `/deleteaccount`: Allows a user to delete their account
- Notification-Related
    - `/watch`: Watch a show or movie to be notified for new content
    - `/unwatch`: Unwatch a show or movie to stop notifications for new content
    - `/watching`: Get a list of the content you are currently watching
- System-Related **[ADMIN ONLY]**
    - `/access`: View or update the access level of a user (table in the wiki for different options)
    - `/forceupdate`: Forcibly update the databases before the regular job interval time
