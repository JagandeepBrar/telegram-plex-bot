# Plex Assistant Bot

A bot to notify, control, manage (and more) Plex integration applications like Sonarr, Radarr, Ombi, etc.

*Implemention of more applications and features will occur overtime*

## To-Do List

- Comment code
- Add message building code for daily and weekly notifications, currently sends "movie" and "television" but no other information

## Implemented Commands

- General
    - `/help`: Shows all commands available for the current user (based on their status)
- Account-Related
    - `/register`: Registers a user to the bot's sqlite database
        - `/start` is also an alias, so it is automatically executed when any user starts a conversation with the bot
    - `/account`: Account settings & information
        - Add/change Ombi ID
        - Change notification complexity
- Notification-Related
    - `/watch`: Monitor a show or movie to be notified for new content
    - `/unwatch`: Unmonitor a show or movie to stop notifications for new content
- System-Related **[ADMIN ONLY]**
    - `/access`: View or update the access level of a user (table below for different options)
    - `/forceupdate`: Forcibly update the databases before the regular job interval time

## Features

### Planned

- ~~Sonarr/Radarr notifications~~
- Sonarr/Radarr calendars
- Connect to Ombi for automatic notifications
- Add new shows/movies to Sonarr/Radarr

### Potential

- SABnzbd/NZBget implementations
