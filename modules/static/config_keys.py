class SimulatorKeys:
    DEVICE_ADDRESS = "device_address"


class BesiegeKeys:
    STATE = "state"
    NEXTTIME = "nexttime"


class EnemyKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    ENDTIME = "endtime"
    LOOPTIME = "looptime"


class MyFightKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    ENDTIME = "endtime"
    LOOPTIME = "looptime"


class RankingKeys:
    STATE = "state"
    NEXTTIME = "nexttime"


class BattleDestoryKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    ENDTIME = "endtime"
    LOOPTIME = "looptime"


class TakeLandKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    X = "x"
    Y = "y"
    DRAFT = "draft"
    SELECT_LIST = "select_list"


class PracticeLandKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    X = "x"
    Y = "y"
    DRAFT = "draft"
    ADDRESS = 'address'
    SELECT_LIST = "select_list"
    MAX_DISTANCE = 'max_distance'
    TIME_CONSUMING = 'time_consuming'
    MY_REMAINING = 'my_remaining'
    ENEMY_REMAINING = 'enemy_remaining'

class FightCityKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    X = "x"
    Y = "y"


# 顶层配置键名
class ConfigSections:
    SIMULATOR = "simulator"
    BESIEGE = "besiege"
    EXPLOIT = "exploit"
    ENEMY = "enemy"
    MYFIGHT = "myfight"
    RANKING = "ranking"
    BATTLEDESTORY = "battledestory"
    TAKE_LAND = "take_land"
    PRACTICE_LAND = "practice_land"
    FIGHT_CITY = "fight_city"
