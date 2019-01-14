# Plex Assistant Bot

A bot to notify, control, manage (and more) Plex integration applications like Sonarr, Radarr, Ombi, etc.

*Implemention of more applications will occur overtime*

## Features

### Planned

- Sonarr/Radarr notifications
- Sonarr/Radarr calendars
- Connect to Ombi for automatic notifications
- Add new shows/movies to Sonarr/Radarr

## Potential

- SABnzbd/NZBget implementations

## Implementation

### Users

#### Status

| Status Code |  Type  |               Verification                |
|:-----------:|:------:|:-----------------------------------------:|
| 0           | Admin  | -                                         |
| 1           | Normal | <b style="color: yellow;">Unverified</b>  |
| 2           | Normal | <b style="color: lime;">Verified</b>      |
| 3           | Normal | <b style="color: fuchsia;">Restricted</b> |
| 4           | Normal | <b style="color: red;">Banned</b>         |
