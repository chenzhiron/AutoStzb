from pywebio.output import put_button

from modules.team.team import teamLists


def renderTeam():
    teams = []
    for team in teamLists:
        teams.append(put_button(team.name, onclick=team.render))
    return teams


