# import nflgame as n
import time

# https://pypi.org/project/nflgame/

http://cdn.espn.com/core/nfl/playbyplay/401772988

http://cdn.espn.com/nfl/game/_/gameId/401772988/seahawks-patriots

g = n.one(2016, 4, 'CIN', 'IND', kind='PRE')
scores0 = len(g.scores)
hometo0 = g.stats_home[6]
awayto0 = g.stats_away[6]
awaypenalty0 = g.stats_away[4]
homepenalty0 = g.stats_home[4]
awaypenyds0 = g.stats_away[5]
homepenyds0 = g.stats_home[5]

while(not(g.game_over())):
    g = n.one(2016, 4, 'CIN', 'IND', kind='PRE')
    games = n.games(year=2016, week=4, kind='PRE', away='IND')
    
    
    scores = g.scores
    
    hometo = g.stats_home[6]
    awayto = g.stats_away[6]
    awaypenalty = g.stats_away[4]
    homepenalty = g.stats_home[4]
    awaypenyds = g.stats_away[5]
    homepenyds = g.stats_home[5]
    
    if len(scores) > scores0: # someone scored

        text = str(scores[len(scores)-1]) + ' ' + str(g.nice_score())
        
        send('Scoring Play', text)

        print text
        
        scores0 += 1
    
    if hometo > hometo0:
        send('Home Turnover', str(hometo))
        
        print "Home turnover number: " + str(hometo)
        
        hometo0 = hometo
        
    if awayto > awayto0:
        send('Away Turnover', str(awayto))
        
        print "Away turnover number: " + str(awayto)
        
        awayto0 = awayto
    
    if awaypenalty > awaypenalty0:
        send('Away Penalty', str(awaypenyds - awaypenyds0))
        
        print "Away penalty for " + str(awaypenyds - awaypenyds0) + " yards."
        
        awaypenalty0 = awaypenalty
        awaypenyds0 = awaypenyds
        
    if homepenalty > homepenalty0:
        send("Home Penalty", str(homepenyds - homepenyds0))
        
        print 'Home penalty for ' + str(homepenyds - homepenyds0) + ' yards.'
        print
        
        homepenalty0 = homepenalty
        
        homepenyds0 = homepenyds
    
    time.sleep(120)

