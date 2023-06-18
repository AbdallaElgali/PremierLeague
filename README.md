# Premier League Scraper
This program is designed to scrape information about the current standings of the Premier League and allow users to retrieve match details for a specific date. The program retrieves data from two websites: https://www.skysports.com/premier-league-table for the current standings and https://sports.ndtv.com/english-premier-league/schedules-fixtures for match information.

## Installation
To run the Premier League Scraper program, follow these steps:

1. Clone the repository or download the source code files.
2. Install the required dependencies:
   -requests library: Use the command pip install requests to install.
   -beautifulsoup4 library: Use the command pip install beautifulsoup4 to install.
   -bs4 module: This is included in the beautifulsoup4 library.
3. Open a terminal or command prompt and navigate to the directory where the program files are located.
4. Run the program by executing the command python filename.py, where filename.py is the name of the Python script containing the program code.

## Usage
Upon running the program, you will be presented with a menu of options:

1. Show Current Standing of Premier League Teams
2. Check Premier League matches on a given date
3. Check the matches today
4. Exit
To select an option, enter the corresponding number and press Enter.

## 1. Show Current Standing of Premier League Teams
This option displays the current standings of the Premier League teams. The program scrapes the data from https://www.skysports.com/premier-league-table and retrieves the team names and their corresponding points. The standings are then displayed in the terminal.

## 2. Check Premier League matches on a given date
This option allows you to retrieve the match details for a specific date. You will be prompted to enter a date in the format dd-mm-yyyy. The program will scrape the match information from https://sports.ndtv.com/english-premier-league/schedules-fixtures and display the matches, teams, and scores for the specified date.

## 3. Check the matches today
Selecting this option will automatically retrieve the current date and fetch the match details for today. The program will display the matches, teams, and scores for the current date.

## 4. Exit
Choosing this option will terminate the program.

## Requirements
The Premier League Scraper program requires the following dependencies:

Python 3.x
requests library
beautifulsoup4 library
These dependencies can be installed using the pip package manager. Refer to the "Installation" section above for more details.

## License
This program is released under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license. Refer to the LICENSE file for more information.

## Disclaimer
This program is intended for educational purposes only. The scraping of websites may be subject to legal restrictions or terms of service. Ensure that you comply with the terms of service of the websites you scrape and respect the intellectual property rights of the website owners.

Please use this program responsibly and avoid overloading the websites with excessive requests. Be considerate of the bandwidth and resources of the websites you scrape.
