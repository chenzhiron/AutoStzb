class SimulatorKeys:
    DEVICE_ADDRESS = "device_address"


class BesiegeKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    X = "x"
    Y = "y"
    MODE = 'mode'
    STAGE = 'stage'
    ADDRESS = 'address'
    MAX_DISTANCE = 'max_distance'
    TIME_CONSUMING = 'time_consuming'


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


class PracticeLandKeys:
    STATE = "state"
    NEXTTIME = "nexttime"
    X = "x"
    Y = "y"
    NUM = 'num'
    STAGE = 'stage'
    DRAFT = "draft"
    ADDRESS = 'address'
    ACTION_LIST = "action_list"
    MAX_DISTANCE = 'max_distance'
    TIME_CONSUMING = 'time_consuming'
    MY_REMAINING = 'my_remaining'
    ENEMY_REMAINING = 'enemy_remaining'


class ATTACK_LAND:
    STATE = "state"
    NEXTTIME = "nexttime"
    NUM = 'num'
    X = "x"
    Y = "y"
    STAGE = 'stage'
    DRAFT = "draft"
    ADDRESS = 'address'
    ACTION_LIST = "action_list"
    MAX_DISTANCE = 'max_distance'
    TIME_CONSUMING = 'time_consuming'
    MY_REMAINING = 'my_remaining'
    ENEMY_REMAINING = 'enemy_remaining'


class SPARTA_ATTACK_LAND:
    STATE = "state"
    NEXTTIME = "nexttime"
    X = "x"
    Y = "y"
    STAGE = 'stage'
    ADDRESS = 'address'
    MAX_DISTANCE = 'max_distance'
    TIME_CONSUMING = 'time_consuming'


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
    PRACTICE_LAND = "practice_land"
    PRACTICE_LAND_1 = "practice_land_1"
    PRACTICE_LAND_2 = "practice_land_2"
    PRACTICE_LAND_3 = "practice_land_3"
    PRACTICE_LAND_4 = "practice_land_4"
    ATTACK_LAND = 'attack_land'
    ATTACK_LAND_1 = 'attack_land_1'
    ATTACK_LAND_2 = 'attack_land_2'
    ATTACK_LAND_3 = 'attack_land_3'
    ATTACK_LAND_4 = 'attack_land_4'
    SPARTA_ATTACK_LAND = 'sparta_attack_land'
    FIGHT_CITY = "fight_city"
