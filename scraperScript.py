import requests
from bs4 import BeautifulSoup
# Script for pulling the data i needed from the uefa website
# Issues - leaves out the first returned result (usualy 2018/19)

# Make the request to a url - Barcelona eg: https://www.uefa.com/teamsandplayers/teams/club=50080/profile/history/index.html
# change fo reach team
r = requests.get('https://www.uefa.com/teamsandplayers/teams/club=50080/profile/history/index.html')

c = r.content
soup = BeautifulSoup(c)

main_content = soup.find('tbody')

winnerArray = []
runnerUpArray = []
semiFinalArray = []
quarterFinalArray = []
last16Array = []
groupArray = []

# Returns years of exit for each champions leauge competition stage
for tag in main_content.tr.next_siblings:
    rowDate = tag.find('td', attrs = {'class': 'b l w18'}).text
    rowTournament = tag.find('td', attrs = {'class': 'l w230'}).text    
    rowStage = tag.find('td', attrs = {'class': 'l w200'}).text

    if(rowTournament == "UEFA Champions League" and rowStage == "Winner" ):
      winnerArray.append(rowDate)

    if(rowTournament == "UEFA Champions League" and rowStage == "Final" ):
      runnerUpArray.append(rowDate)

    if(rowTournament == "UEFA Champions League" and rowStage == "Semi-finals" ):
      semiFinalArray.append(rowDate)

    if(rowTournament == "UEFA Champions League" and rowStage == "Quarter-finals" ):
      quarterFinalArray.append(rowDate)

    if(rowTournament == "UEFA Champions League" and rowStage == "Round of 16"):
      last16Array.append(rowDate)

    if(rowTournament == "UEFA Champions League" and rowStage == "Group stage" ):
      groupArray.append(rowDate)

print("winner:", winnerArray),
print("runnerUp:", runnerUpArray)
print("semiFinal:", semiFinalArray)
print("quarterFinal:", quarterFinalArray)
print("last16:", last16Array)
print("group:", groupArray)

# Example output for Barcelona
# winner: ['2014/15', '2010/11', '2008/09', '2005/06']
# runnerUp: ['1993/94']
# semiFinal: ['2012/13', '2011/12', '2009/10', '2007/08', '2001/02', '1999/00']
# quarterFinal: ['2017/18', '2016/17', '2015/16', '2013/14', '2002/03', '1994/95']
# last16: ['2006/07', '2004/05']
# group: ['1998/99', '1997/98']