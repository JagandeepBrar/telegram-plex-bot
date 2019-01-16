# Plex Assistant Bot

A bot to notify, control, manage (and more) Plex integration applications like Sonarr, Radarr, Ombi, etc.

*Implemention of more applications will occur overtime*

## To-Do List

- Comment code

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

| Code |  Type  | Verification |
|:----:|:------:|:------------:|
| 0    | Admin  | -            |
| 1    | Normal | Unverified   |
| 2    | Normal | Verified     |
| 3    | Normal | Restricted   |
| 4    | Normal | Banned       |

#### Frequency

| Code | Timeframe    |
|:----:|:------------:|
| 0    | Immediately  |
| 1    | Daily        |
| 2    | Weekly       |

#### Detail

| Code | Details |
|:----:|:-------:|
| 0    | Simple  |
| 1    | Complex |
