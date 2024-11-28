from modules.web.modules import Private, Team, overview, StLog

private = Private()
team = Team()
stlog = StLog()
overview.update_log_instance(stlog)
