# Objective: Create a program which scraps a website for information about current standings of premier league and allows me to ask about the matches on a specific date

from datetime import date
from datetime import datetime
import requests
import bs4
import urllib3
import dateparser

class Premierleague():
    page = None
    page2games = None

    try:
        page = requests.get('https://www.skysports.com/premier-league-table')  # Getting page HTML through request
        page2games = requests.get('https://sports.ndtv.com/english-premier-league/schedules-fixtures')
        Condition = True

    except requests.exceptions.ConnectionError:
        print('Please Check your Connection and try again!!')
        Condition = False
    except urllib3.exceptions.NewConnectionError:
        print('Please Check your Connection and try again!!')
        Condition = False

    if page is not None:
        soup = bs4.BeautifulSoup(page.content, 'html.parser')  # Parsing content using beautifulsoup
    if page2games is not None:
        soup2games = bs4.BeautifulSoup(page2games.content, 'html.parser')

    # Function to return a list with information about the matches of the date given and remove unwanted characters from the list (clean the list)
    def MatchInfo(self, mdate):

        global cleanlist

        self.MatchDay = str(self.soup2games.find_all("div", attrs={"id": mdate})).split(
            ',')  # Returning information about matches that day

        cleanlist = list()

        if len(self.MatchDay) <= 1:
            print("No matches on the date specified!")

        for x in self.MatchDay:
            if '>' in x:
                smallxl = x.split('>')
                smallxl.pop(0)
                smallxl.pop(1)
            else:
                continue
            for minor in smallxl:
                if '<' in minor:
                    minorxl = minor.split('<')
                    minorxl.pop(1)
                else:
                    continue
                for mini in minorxl:  # Appending the individual Team Names as a string to the TeamNames list, as minorxl is of type list
                    if len(mini) == 0:
                        continue
                    elif mini == ' ':
                        continue
                    else:
                        cleanlist.append(mini)

    # Function which prints out the matches found, the teams and their score
    def matches(self):

        c = 0
        x = int(len(cleanlist) / 10)
        smatchlist_big = []

        # Considering there can only be a maximum of 10 matches per day, 10 lists will be created, a list for each match that day
        match1 = list()
        match2 = list()
        match3 = list()
        match4 = list()
        match5 = list()
        match6 = list()
        match7 = list()
        match8 = list()
        match9 = list()
        match10 = list()

        counter = 0
        for e10 in cleanlist:
            if counter < 10:
                match1.append(e10)
            elif 20 > counter >= 10:
                match2.append(e10)
            elif 30 > counter >= 20:
                match3.append(e10)
            elif 40 > counter >= 30:
                match4.append(e10)
            elif 50 > counter >= 40:
                match5.append(e10)
            elif 60 > counter >= 50:
                match6.append(e10)
            elif 70 >= counter >= 60:
                match7.append(e10)
            elif 80 > counter >= 70:
                match8.append(e10)
            elif 90 > counter >= 80:
                match9.append(e10)
            elif 100 >= counter >= 90:
                match10.append(e10)
            elif len(cleanlist) == 0:
                print("No matches on specified date!!")
                break
            else:
                continue
            counter = counter + 1

        for i in range(x):
            if i == 0:
                smatchlist_big.append(match1)
            elif i == 1:
                smatchlist_big.append(match2)
            elif i == 2:
                smatchlist_big.append(match3)
            elif i == 3:
                smatchlist_big.append(match4)
            elif i == 4:
                smatchlist_big.append(match5)
            elif i == 5:
                smatchlist_big.append(match6)
            elif i == 6:
                smatchlist_big.append(match7)
            elif i == 7:
                smatchlist_big.append(match8)
            elif i == 8:
                smatchlist_big.append(match9)
            elif i == 9:
                smatchlist_big.append(match10)

            else:
                continue

        # printing out the match and the match score to the Terminal
        counter0 = 1
        for match in smatchlist_big:
            print(f'\nMatch {counter0}:\n{match[3]} vs {match[5]}\n SCORE: {match[4]}:{match[6]}\n\n')
            counter0 = counter0 + 1

    # Create a function which prints out the matches and the scores of each team.

    def matches_per_date(self):

        #We can make use of Natural Language Processing here in order to make it more lenient in accepting input
        while True:
            date_string = input("Enter a date to check Premier League matches (e.g., 'next Sunday', 'tomorrow'): ")
            parsed_date = dateparser.parse(date_string)

            if parsed_date is None:
                print("Invalid date. Please try again.")
            else:
                mdate = parsed_date.date()
                self.MatchInfo(mdate.strftime("%d-%m-%Y"))
                self.matches()
                break

    def matchestoday(self):
        # considering todays the date we want to pass
        today = date.today()
        todaysdate = today.strftime('%d-%m-%Y')
        self.MatchInfo(todaysdate)
        self.matches()

    # Create a function for current standings
    def Current_standings(self):

        self.TeamName = self.soup.select(
            "table tbody tr td.standing-table__cell.standing-table__cell--name a")  # Selecting all of the anchors with titles
        self.AllTeams = self.TeamName[:20]

        # Extract the points value of each team from the raw code
        text = self.page.text
        line = text.split("\n")

        num = 0
        s = int()
        proteinlist = list()

        for x in line:

            if '<td class="standing-table__cell" data-sort-value=' in x:
                stripped = x.split('>')
                steroid = stripped[1]
                natural = steroid.split('<')
                protein = natural[0]  # The points
                proteinlist.append(protein)


            else:
                continue
        # print the team with points
        n = 1
        for Team in self.AllTeams:
            print(f'{n}. {Team.text}: {proteinlist[n - 1]}')  # Display the innerText of each anchor
            n = n + 1

        return 0

    def Run(self):

        wc = 0
        denial = ['no', 'No', 'Nah', 'nein']
        acceptance = ['yes', 'yeah', 'Yes', 'Ja']

        while self.Condition:
            try:
                if wc >= 1:
                    q2 = input('\nDo you wish to continue? ')
                    if q2 in denial:
                        break
                    elif q2 in acceptance:
                        wc = 0
                        continue
                    else:
                        break

                elif wc == 0:
                    q1 = int(input(
                        '\nChoose one of the following: (hint: only enter an integer from the given, ex: 1,2..4)\n 1. Show Current Standing of Premier League Teams\n 2. Check Premier League matches on a given date\n 3. Check the matches Today\n 4. Exit\n ---> '))
                    if q1 == 1:
                        self.Current_standings()
                    elif q1 == 2:
                        self.matches_per_date()
                    elif q1 == 3:
                        self.matchestoday()
                    elif q1 == 4:
                        print('\nGoodbye!!!')
                        break
                    elif type(q1) != int:
                        print('\nPlease try again and enter a number from 1-4!!')
                    else:
                        break
            except(ValueError):
                print('\nPlease try again and enter a number from 1-4!!')
            wc = wc + 1


premierleague = Premierleague()
premierleague.Run()