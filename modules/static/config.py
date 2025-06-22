from modules.static.config_keys import *

tasks_config = {
    ConfigSections.SIMULATOR: {SimulatorKeys.DEVICE_ADDRESS: "127.0.0.1:7885"},
    ConfigSections.BESIEGE: {BesiegeKeys.STATE: False, BesiegeKeys.NEXTTIME: "2019/06/01 00:00:00"},
    ConfigSections.EXPLOIT: {"state": False, "nexttime": "2019/06/01 00:00:00"},
    ConfigSections.ENEMY: {
        EnemyKeys.STATE: False,
        EnemyKeys.NEXTTIME: "2019/06/01 00:00:00",
        EnemyKeys.ENDTIME: "2019/06/01 00:00:00",
        EnemyKeys.LOOPTIME: 60,
    },
    ConfigSections.MYFIGHT: {
        MyFightKeys.STATE: True,
        MyFightKeys.NEXTTIME: "2019/06/01 00:00:00",
        MyFightKeys.ENDTIME: "2019/06/01 00:00:00",
        MyFightKeys.LOOPTIME: 0,
    },
    ConfigSections.RANKING: {RankingKeys.STATE: False, RankingKeys.NEXTTIME: "2019/06/01 00:00:00"},
    ConfigSections.BATTLEDESTORY: {
        BattleDestoryKeys.STATE: False,
        BattleDestoryKeys.NEXTTIME: "2019/06/01 00:00:00",
        BattleDestoryKeys.ENDTIME: "2019/06/01 00:00:00",
        BattleDestoryKeys.LOOPTIME: 60,
    },
    ConfigSections.TAKE_LAND: {
        TakeLandKeys.STATE: False,
        TakeLandKeys.NEXTTIME: "2019/06/01 00:00:00",
        TakeLandKeys.X: 123,
        TakeLandKeys.Y: 123,
        TakeLandKeys.DRAFT: False,
        TakeLandKeys.SELECT_LIST: 1
    },
    ConfigSections.PRACTICE_LAND: {
        PracticeLandKeys.STATE: False,
        PracticeLandKeys.NEXTTIME: "2019/06/01 00:00:00",
        PracticeLandKeys.X: 123,
        PracticeLandKeys.Y: 123,
        PracticeLandKeys.STAGE: 0,
        PracticeLandKeys.ADDRESS: '',
        PracticeLandKeys.DRAFT: True,
        PracticeLandKeys.NUM: 1,
        PracticeLandKeys.ACTION_LIST: 1,
        PracticeLandKeys.MAX_DISTANCE: 300,
        PracticeLandKeys.TIME_CONSUMING: 0,
        PracticeLandKeys.MY_REMAINING: 30000,
        PracticeLandKeys.ENEMY_REMAINING: 30000
    },
    ConfigSections.FIGHT_CITY: {
        FightCityKeys.STATE: False,
        FightCityKeys.NEXTTIME: "2019/06/01 00:00:00",
        FightCityKeys.X: 123,
        FightCityKeys.Y: 123,

    }
}
