<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Concreet Kennisdeler</h3>

  <p align="center">
    By teachers, for teachers
    <br />
    <a href="https://repo.go2people.nl/django/kennisdeler-luca-stage"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

Conreet kennisdeler stage project voor Go2People.

### Built With

* [Django](https://www.python.org/)



<!-- GETTING STARTED -->
## Getting Started

Have a working pc and probably like a virtual enviroment or something. 

### Prerequisites

Setup postgres:
https://www.2ndquadrant.com/en/blog/pginstaller-install-postgresql/
Database connection type is assumed to be "Trust"

Install dependencies:
$ apt install python3.6
$ apt install python3-pip

### Installation

Clone the repo
```sh
git clone https://git@repo.go2people.nl:django/kennisdeler-luca-stage.git
```

Change directory to root folder "kennisdeler"
``` sh
cd kennisdeler
```

Install all pip requirements
``` sh
pip3 install -r requirements/defaults.txt
```

Generate a Secret_key
``` sh
python3 manage.py generate_secret_key
```

Rename ".env.example" to ".env" and add your own settings
``` sh
mv .env.example .env
nano .env
```

Run the database migrations
``` sh
python3 manage.py migrate --settings=kennisdeler.settings.base
```



<!-- USAGE EXAMPLES -->
## Usage

Run the server
``` sh
python3 manage.py runserver <address:port>--settings=kennisdeler.settings.base
```



<!-- ROADMAP -->
## Roadmap

Sorry, the roadmap is in my google todo. Private eyes only.


<!-- CONTRIBUTING -->
## Contributing

don't 


<!-- LICENSE -->
## License

Distributed under the Go2People licence. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Luca Barendse - luca@go2people.nl

Project Link: [https://repo.go2people.nl/django/kennisdeler-luca-stage](https://repo.go2people.nl/django/kennisdeler-luca-stage)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Tycho](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png