# Utilization of Speech Recognition to Have Indonesian Subtitles and Translations
> Outline a brief description of your project.
> Live demo [_here_](https://auto-subtitle-ofa.herokuapp.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
We developed an application called Wibu x Nolep as a solution to automatically create subtitles by utilizing Natural Language Processing and also a speech recognition API. The main purpose of this application is to present an automatic way to generate subtitles for audio and video. Replacing the tedious methods of the current system will save time, reduce the amount of administrative work to be done and will generate subtitles automatically with electronic equipment. The system will extract the audio first, then recognize the extracted audio with the available speech recognition APIs. Then the recognized audio is converted into a .wav audio file and then converted back into text and stored in a text file with a “.srt” extension. Later, this “.srt” file can be opened in the media player to view subtitles and videos.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- python version 3.10.4
- audiosegment version 0.23.0
- googletrans version 3.1.0a0
- gunicorn version 20.1.0
- Jinja2 version 3.0.3
- itsdangerous version 2.0.1
- Flask version 1.1.1
- pandas version 1.3.4
- pydub version 0.25.13
- SpeechRecognition version 3.8.1
- srt version 3.5.2
- Werkzeug version 2.0.2


## Features
List the ready features here:
- Awesome feature 1
- Awesome feature 2
- Awesome feature 3


## Screenshots
![Example screenshot](./img/screenshots/home.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->