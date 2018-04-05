from datetime import date
import nba_py
from prettytable import PrettyTable


scoreboard=nba_py.Scoreboard(day=date.today().day-1)
line_score=scoreboard.line_score()

games=[]
current_game={}

current_game_sequence=0
game_sequence_count=0
for team in line_score:
    if (team['GAME_SEQUENCE'] != current_game_sequence):
        current_game['TEAM_1']=team['TEAM_ABBREVIATION']
        current_game['TEAM_1_WINS_LOSSES']=team['TEAM_WINS_LOSSES']
        current_game['PTS_TEAM_1']=team['PTS']
        current_game['PTS_QTR1_TEAM_1']=team['PTS_QTR1']
        current_game['PTS_QTR2_TEAM_1'] = team['PTS_QTR2']
        current_game['PTS_QTR3_TEAM_1'] = team['PTS_QTR3']
        current_game['PTS_QTR4_TEAM_1'] = team['PTS_QTR4']
        current_game_sequence=team['GAME_SEQUENCE']

        if team['PTS_OT1']!= 0:
            current_game['PTS_OT1_TEAM_1'] = team['PTS_OT1']
            current_game['PTS_OT2_TEAM_1'] = team['PTS_OT2']
        else:
            current_game['PTS_OT1_TEAM_1']=0
            current_game['PTS_OT2_TEAM_1']=0

        game_sequence_count += 1

    elif(game_sequence_count==1):
        current_game['TEAM_2'] = team['TEAM_ABBREVIATION']
        current_game['TEAM_2_WINS_LOSSES'] = team['TEAM_WINS_LOSSES']
        current_game['PTS_TEAM_2'] = team['PTS']
        current_game['PTS_QTR1_TEAM_2'] = team['PTS_QTR1']
        current_game['PTS_QTR2_TEAM_2'] = team['PTS_QTR2']
        current_game['PTS_QTR3_TEAM_2'] = team['PTS_QTR3']
        current_game['PTS_QTR4_TEAM_2'] = team['PTS_QTR4']
        current_game_sequence = team['GAME_SEQUENCE']

        if team['PTS_OT1']!=0:
            current_game['PTS_OT1_TEAM_2'] = team['PTS_OT1']
            current_game['PTS_OT2_TEAM_2'] = team['PTS_OT2']
        else:
            current_game['PTS_OT1_TEAM_2'] = 0
            current_game['PTS_OT2_TEAM_2'] = 0
        games.append(current_game)

        current_game = {}
        game_sequence_count = 0

for game in games:
    table=PrettyTable()
    table.field_names=["TEAM", "PTS_QTR1", "PTS_QTR2", "PTS_QTR3", "PTS_QTR4", "PTS_OT1", "PTS_OT2", "PTS"]
    table.add_row([game["TEAM_1"], game["PTS_QTR1_TEAM_1"], game["PTS_QTR2_TEAM_1"], game["PTS_QTR3_TEAM_1"], game["PTS_QTR4_TEAM_1"],
                    game["PTS_OT1_TEAM_1"], game["PTS_OT2_TEAM_1"], game["PTS_TEAM_1"]])
    table.add_row([game["TEAM_2"], game["PTS_QTR1_TEAM_2"], game["PTS_QTR2_TEAM_2"], game["PTS_QTR3_TEAM_2"],
                   game["PTS_QTR4_TEAM_2"], game["PTS_OT1_TEAM_2"], game["PTS_OT2_TEAM_1"], game["PTS_TEAM_2"]])
    print(table)