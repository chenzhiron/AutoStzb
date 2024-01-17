from modules.team.Class.teamProp import TeamProp
from config.config import userConfig

teamLists = []

for v in userConfig['TeamManager']:
    teamLists.append(TeamProp(config=v))

