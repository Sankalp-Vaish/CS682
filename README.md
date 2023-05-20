# RTInvest

<img src="https://img.shields.io/badge/Version-v1.0-blue.svg?logo=LOGO">

## Objective/Description
Web application that uses information fetched from APIs to calculate and generate Cash Flow Analysis of properties available in the country.
<br>

## Structure
The application is based on a Django framework. The application follows the MVC architecture. The backend of the application fetches the details of properties in a specified pincode from real estate apis and sends it to a python based calculator. The front end displays the properties on a google map along with their ROI results. Each property is displayed along with a report on the cashflow analysis given by the investment calculator of the application.


## Usage
Steps for new user to run project 
<ol>

<li> Clone the project from the github repository to a new folder on your system terminal.
git clone https://github.com/Sankalp-Vaish/CS682.git</li>

<li> Navigate into the project folder
cd CS682</li>

<li> Start the application using the below command.

> py manage.py runserver<br>
> OR<br>
> python manage.py runserver
</ol>

 
## Pre-requisites
<ul>
<li> Google API key is required - Replace the current Google API key with your new key in places it is currently being used (settings.py, mortgage.html).</li>
<li> Python </li>
<li> Django -v 4.1.7 </li>
<li> IDE of your choice </li>
</ul>


## Installations required

> pip install django<br>
> pip install django-bootstrap-v5<br>
> pip install numpy<br>
> pip install googlemaps<br>
> pip install geopy<br>
> pip install --upgrade "kaleido==0.1.*"<br>
> pip3 install pandas<br>
> pip3 install plotly


## Tools and Technologies used

<img src="https://img.shields.io/badge/HTML-v5-blue.svg?logo=LOGO">
<img src="https://img.shields.io/badge/CSS-v3-blue.svg?logo=LOGO">
<img src="https://img.shields.io/badge/Django-v4.2-blue.svg?logo=LOGO">
<img src="https://img.shields.io/badge/Bootstrap-v4.2-blue.svg?logo=LOGO">
<img src="https://img.shields.io/badge/VSCode-v1.77-blue.svg?logo=LOGO">


## Future scope
Some of the many ideas that can be implemented onto the application:
* Integrate drawing feature into the map that helps focus on custom area.
* Various filters to help make the user experience better.
* Interaction feature that helps set a platform for the seller and investor to interact with each.


## Collaborators
Prarthana Prathap

Prateeksha Bhojaraj

Sankalp Vaish

## Acknowledgement
We express our gratitude to Professor Kenneth Fletcher for giving us this opportunity to work on this project.
