<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
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
<div align="center">
  <a href="https://github.com/sourabhdeshmukh/twitter_sentiment_analysis">
    <img src="images/twitter.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Twitter Sentiment Analysis</h3>

  <p align="center">
    The "Twitter Sentiment Analysis using NLP and Machine Learning" aims to harness the power of Natural Language Processing (NLP) and advanced machine learning techniques to accurately predict the sentiments of individuals expressed through Twitter handles or hashtags, while categorizing these sentiments as positive or negative.
    <br />
    <a href="https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/blob/main/docs/Twitter_Sentiment_Analysis_report.pdf"><strong>Project Report »</strong></a>
    <br />
    <br />
    <a href="https://twittersentimentpredictor.streamlit.app/">View Demo</a>
    ·
    <a href="https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/issues">Report Bug</a>
    ·
    <a href="https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The core objective of this project is to build a sophisticated sentiment analysis model that can effectively classify tweets as either positive or negative. By training the model on a diverse and comprehensive dataset of labeled tweets, the system will learn to identify linguistic patterns, contextual cues, and emotional expressions that signify positive or negative sentiments.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python3-url]
* [![Streamlit][Streamlit.io]][Streamlit-url]
* [![Twitter][Twitter.com]][Twitter-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can run this project local machine. This project is built on Ubuntu.

### Prerequisites

Before running this project on locl machine, you need to create project on the developer.twitter.com and generate the consumer keys, and access token required for the project to get the data from the twitter using API's.
* [Twitter Developer URL](https://developer.twitter.com/en)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sourabhdeshmukh/twitter_sentiment_analysis.git

2. Setup your python virtual environment
   ```sh
   python3 -m venv <env_name>
   ``` 

3. Activate your virtual environment
   ```sh
   source <env_name>/bin/activate
   ```
4. Copy the consumer and access keys in streamlit file and store it inside ~/.streamlit directory

5. Install the python dependecies inside your virtual environment 
   ```sh
   pip install -r requirements.txt
   ```

6. Run the project using below command.
   ```sh
   streamlit run app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. **Business Insights:** This project's outcomes can be employed by businesses for brand monitoring, understanding customer feedback, and adjusting marketing strategies based on the sentiment trends.

2. **Social Listening:** Governments and organizations can utilize the sentiment analysis to gauge public opinion on social and political issues.

3. **Event Tracking:** Tracking sentiments related to specific events or campaigns can help organizations understand the overall impact and success of their initiatives.

4. **User Experience Enhancement:** Online platforms can utilize sentiment analysis to identify and address user concerns promptly, enhancing user satisfaction.

5. **Market Research:** Sentiment analysis can serve as a cost-effective method for conducting market research and gathering insights into consumer preferences.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@100rabhdeshmukh](https://twitter.com/100rabhdeshmukh) - sourabh[dot]deshmukh[dot]988[at]gmail[dot]com

Project Link: [https://github.com/sourabhdeshmukh/twitter_sentiment_analysis](https://github.com/sourabhdeshmukh/twitter_sentiment_analysis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/sourabhdeshmukh/twitter_sentiment_analysis.svg?style=for-the-badge

[contributors-url]: https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/sourabhdeshmukh/twitter_sentiment_analysis.svg?style=for-the-badge

[forks-url]: https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/network/members

[stars-shield]: https://img.shields.io/github/stars/sourabhdeshmukh/twitter_sentiment_analysis.svg?style=for-the-badge

[stars-url]: https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/stargazers

[issues-shield]: https://img.shields.io/github/issues/sourabhdeshmukh/twitter_sentiment_analysis.svg?style=for-the-badge

[issues-url]: https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/issues

[license-shield]: https://img.shields.io/github/license/sourabhdeshmukh/twitter_sentiment_analysis.svg?style=for-the-badge

[license-url]: https://github.com/sourabhdeshmukh/twitter_sentiment_analysis/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/sourabh-deshmukh
[product-screenshot]: images/screenshot.png

[Python.org]: https://img.shields.io/badge/Python-3-blue.svg?logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIHdpZHRoPSI4MDBweCIgaGVpZ2h0PSI4MDBweCIgdmlld0JveD0iMCAwIDY0IDY0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zMS44ODUgMTZjLTguMTI0IDAtNy42MTcgMy41MjMtNy42MTcgMy41MjNsLjAxIDMuNjVoNy43NTJ2MS4wOTVIMjEuMTk3UzE2IDIzLjY3OCAxNiAzMS44NzZjMCA4LjE5NiA0LjUzNyA3LjkwNiA0LjUzNyA3LjkwNmgyLjcwOHYtMy44MDRzLS4xNDYtNC41MzcgNC40NjUtNC41MzdoNy42ODhzNC4zMi4wNyA0LjMyLTQuMTc1di03LjAxOVM0MC4zNzQgMTYgMzEuODg1IDE2em0tNC4yNzUgMi40NTRjLjc3MSAwIDEuMzk1LjYyNCAxLjM5NSAxLjM5NXMtLjYyNCAxLjM5NS0xLjM5NSAxLjM5NWExLjM5MyAxLjM5MyAwIDAgMS0xLjM5NS0xLjM5NWMwLS43NzEuNjI0LTEuMzk1IDEuMzk1LTEuMzk1eiIgZmlsbD0idXJsKCNhKSIvPjxwYXRoIGQ9Ik0zMi4xMTUgNDcuODMzYzguMTI0IDAgNy42MTctMy41MjMgNy42MTctMy41MjNsLS4wMS0zLjY1SDMxLjk3di0xLjA5NWgxMC44MzJTNDggNDAuMTU1IDQ4IDMxLjk1OGMwLTguMTk3LTQuNTM3LTcuOTA2LTQuNTM3LTcuOTA2aC0yLjcwOHYzLjgwM3MuMTQ2IDQuNTM3LTQuNDY1IDQuNTM3aC03LjY4OHMtNC4zMi0uMDctNC4zMiA0LjE3NXY3LjAxOXMtLjY1NiA0LjI0NyA3LjgzMyA0LjI0N3ptNC4yNzUtMi40NTRhMS4zOTMgMS4zOTMgMCAwIDEtMS4zOTUtMS4zOTVjMC0uNzcuNjI0LTEuMzk0IDEuMzk1LTEuMzk0czEuMzk1LjYyMyAxLjM5NSAxLjM5NGMwIC43NzItLjYyNCAxLjM5NS0xLjM5NSAxLjM5NXoiIGZpbGw9InVybCgjYikiLz48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImEiIHgxPSIxOS4wNzUiIHkxPSIxOC43ODIiIHgyPSIzNC44OTgiIHkyPSIzNC42NTgiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjMzg3RUI4Ii8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMzY2OTk0Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9ImIiIHgxPSIyOC44MDkiIHkxPSIyOC44ODIiIHgyPSI0NS44MDMiIHkyPSI0NS4xNjMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjRkZFMDUyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRkZDMzMxIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PC9zdmc+
[Python3-url]: https://www.python.org/

[Streamlit.io]: https://img.shields.io/badge/Streamlit--blue.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMzAxIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDMwMSAxNjUiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xNTAuNzMxIDEwMS41NDdMOTguMTM4NyA3My43NDcxTDYuODQ2NzQgMjUuNDk2OUM2Ljc2MzQgMjUuNDEzNiA2LjU5Njc0IDI1LjQxMzYgNi41MTM0MSAyNS40MTM2QzMuMTgwMDcgMjMuODMwMyAtMC4yMzY2MDggMjcuMTYzNiAxLjAxMzQgMzAuNDk3TDQ3LjUzMDIgMTQ5LjEzOUw0Ny41Mzg1IDE0OS4xNjRDNDcuNTg4NSAxNDkuMjgxIDQ3LjYzMDIgMTQ5LjM5NyA0Ny42ODAyIDE0OS41MTRDNDkuNTg4NSAxNTMuOTM5IDUzLjc1NTIgMTU2LjY3MiA1OC4yODg2IDE1Ny43NDdDNTguNjcxOSAxNTcuODMxIDU4Ljk0NjEgMTU3LjkwNiA1OS40MDY0IDE1Ny45OThDNTkuODY0NSAxNTguMSA2MC41MDUyIDE1OC4yMzkgNjEuMDU1MiAxNTguMjgxQzYxLjE0NjkgMTU4LjI4OSA2MS4yMzAyIDE1OC4yODkgNjEuMzIxOSAxNTguMjk3SDYxLjM4ODZDNjEuNDU1MiAxNTguMzA2IDYxLjUyMTkgMTU4LjMwNiA2MS41ODg2IDE1OC4zMTRINjEuNjgwMkM2MS43Mzg2IDE1OC4zMjIgNjEuODA1MiAxNTguMzIyIDYxLjg2MzYgMTU4LjMyMkg2MS45NzE5QzYyLjAzODYgMTU4LjMzMSA2Mi4xMDUyIDE1OC4zMzEgNjIuMTcxOSAxNTguMzMxVjE1OC4zMzFDMTIxLjA4NCAxNjQuNzU0IDE4MC41MTkgMTY0Ljc1NCAyMzkuNDMxIDE1OC4zMzFWMTU4LjMzMUMyNDAuMTM5IDE1OC4zMzEgMjQwLjgzMSAxNTguMjk3IDI0MS40OTcgMTU4LjIzMUMyNDEuNzE0IDE1OC4yMDYgMjQxLjkyMiAxNTguMTgxIDI0Mi4xMzEgMTU4LjE1NkMyNDIuMTU2IDE1OC4xNDcgMjQyLjE4OSAxNTguMTQ3IDI0Mi4yMTQgMTU4LjEzOUMyNDIuMzU2IDE1OC4xMjIgMjQyLjQ5NyAxNTguMDk3IDI0Mi42MzkgMTU4LjA3MkMyNDIuODQ3IDE1OC4wNDcgMjQzLjA1NiAxNTguMDA2IDI0My4yNjQgMTU3Ljk2NEMyNDMuNjgxIDE1Ny44NzIgMjQzLjg3IDE1Ny44MDYgMjQ0LjQzNiAxNTcuNjExQzI0NS4wMDEgMTU3LjQxNyAyNDUuOTQgMTU3LjA3NyAyNDYuNTI3IDE1Ni43OTRDMjQ3LjExNSAxNTYuNTExIDI0Ny41MjIgMTU2LjIzOSAyNDguMDE0IDE1NS45MzFDMjQ4LjYyMiAxNTUuNTQ3IDI0OS4yMDEgMTU1LjE1NSAyNDkuNzg4IDE1NC43MTVDMjUwLjA0MSAxNTQuNTIxIDI1MC4yMTQgMTU0LjM5NyAyNTAuMzk3IDE1NC4yMjJMMjUwLjI5NyAxNTQuMTY0TDE1MC43MzEgMTAxLjU0N1oiIGZpbGw9IiNGRjRCNEIiLz4KPHBhdGggZD0iTTI5NC43NjYgMjUuNDk4MUgyOTQuNjgzTDIwMy4zNTcgNzMuNzQ4M0wyNTQuMTI0IDE0OS4zNTdMMzAwLjUyNCAzMC40OTgxVjMwLjMzMTVDMzAxLjY5MSAyNi44MzE0IDI5OC4xMDggMjMuNjY0OCAyOTQuNzY2IDI1LjQ5ODEiIGZpbGw9IiM3RDM1M0IiLz4KPHBhdGggZD0iTTE1NS41OTggMi41NTU3MkMxNTMuMjY0IC0wLjg1MjYyNCAxNDguMTgxIC0wLjg1MjYyNCAxNDUuOTMxIDIuNTU1NzJMOTguMTM4OSA3My43NDc3TDE1MC43MzEgMTAxLjU0OEwyNTAuMzk4IDE1NC4yMjJDMjUxLjAyNCAxNTMuNjA5IDI1MS41MjYgMTUzLjAxMiAyNTIuMDU2IDE1Mi4zODFDMjUyLjgwNiAxNTEuNDU2IDI1My41MDYgMTUwLjQ2NSAyNTQuMTIzIDE0OS4zNTZMMjAzLjM1NiA3My43NDc3TDE1NS41OTggMi41NTU3MloiIGZpbGw9IiNCRDQwNDMiLz4KPC9zdmc+Cg==
[Streamlit-url]: https://streamlit.io/

[Twitter.com]: https://img.shields.io/badge/TwitterAPI-v1.1-blue.svg?logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbDpzcGFjZT0icHJlc2VydmUiIHZpZXdCb3g9IjAgMCAyNDggMjA0Ij4KICA8cGF0aCBmaWxsPSIjMWQ5YmYwIiBkPSJNMjIxLjk1IDUxLjI5Yy4xNSAyLjE3LjE1IDQuMzQuMTUgNi41MyAwIDY2LjczLTUwLjggMTQzLjY5LTE0My42OSAxNDMuNjl2LS4wNGMtMjcuNDQuMDQtNTQuMzEtNy44Mi03Ny40MS0yMi42NCAzLjk5LjQ4IDggLjcyIDEyLjAyLjczIDIyLjc0LjAyIDQ0LjgzLTcuNjEgNjIuNzItMjEuNjYtMjEuNjEtLjQxLTQwLjU2LTE0LjUtNDcuMTgtMzUuMDcgNy41NyAxLjQ2IDE1LjM3IDEuMTYgMjIuOC0uODctMjMuNTYtNC43Ni00MC41MS0yNS40Ni00MC41MS00OS41di0uNjRjNy4wMiAzLjkxIDE0Ljg4IDYuMDggMjIuOTIgNi4zMkMxMS41OCA2My4zMSA0Ljc0IDMzLjc5IDE4LjE0IDEwLjcxYzI1LjY0IDMxLjU1IDYzLjQ3IDUwLjczIDEwNC4wOCA1Mi43Ni00LjA3LTE3LjU0IDEuNDktMzUuOTIgMTQuNjEtNDguMjUgMjAuMzQtMTkuMTIgNTIuMzMtMTguMTQgNzEuNDUgMi4xOSAxMS4zMS0yLjIzIDIyLjE1LTYuMzggMzIuMDctMTIuMjYtMy43NyAxMS42OS0xMS42NiAyMS42Mi0yMi4yIDI3LjkzIDEwLjAxLTEuMTggMTkuNzktMy44NiAyOS03Ljk1LTYuNzggMTAuMTYtMTUuMzIgMTkuMDEtMjUuMiAyNi4xNnoiLz4KPC9zdmc+
[Twitter-url]: https://twitter.com/
