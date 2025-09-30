# Web渲染配置
from modules.static.config_keys import *

web_render_config = {
    ConfigSections.SIMULATOR: {
        "display_name": "模拟器设置",
        "description": "",
        "fields": {
            SimulatorKeys.DEVICE_ADDRESS: {
                "display_name": "模拟器地址",
                "description": "推荐使用mumu模拟器",
                "input_type": "str",
                "category": "connection",
            },
        }
    },

    ConfigSections.FIGHT_CITY: {
        "display_name": "打城设置",
        "description": "",
        "fields": {
            FightCityKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            FightCityKeys.ADDRESS: {
                "display_name": "要塞名字",
                "description": "城池周围的要塞名字",
                "input_type": "str",
                "category": "basic",
            },
            FightCityKeys.MODE: {
                "display_name": "打城模式",
                "description": "1:守军未消失时，主力一直上，拆迁拆到没体力。2：守军消失后，主力跟拆迁一直上",
                "input_type": "option",
                "option": [1, 2],
                "category": "basic",
            },
            FightCityKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "主力跟拆迁下次行动时间，一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },

            FightCityKeys.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            FightCityKeys.X: {
                "display_name": "X坐标",
                "description": "城池的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            FightCityKeys.Y: {
                "display_name": "Y坐标",
                "description": "城池的X坐标，以逗号分割，右侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },

    # ConfigSections.ENEMY: {
    #     "display_name": "敌人任务",
    #     "description": "",
    #     "fields": {
    #         EnemyKeys.ENDTIME: {
    #             "display_name": "ENDTIME",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         EnemyKeys.LOOPTIME: {
    #             "display_name": "LOOPTIME",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         EnemyKeys.NEXTTIME: {
    #             "display_name": "下次执行时间",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         EnemyKeys.STATE: {
    #             "display_name": "启用状态",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #     }
    # },

    # ConfigSections.MYFIGHT: {
    #     "display_name": "我的战斗",
    #     "description": "",
    #     "fields": {
    #         MyFightKeys.ENDTIME: {
    #             "display_name": "ENDTIME",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         MyFightKeys.LOOPTIME: {
    #             "display_name": "LOOPTIME",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         MyFightKeys.NEXTTIME: {
    #             "display_name": "下次执行时间",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         MyFightKeys.STATE: {
    #             "display_name": "启用状态",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #     }
    # },

    # ConfigSections.RANKING: {
    #     "display_name": "排行榜",
    #     "description": "",
    #     "fields": {
    #         RankingKeys.NEXTTIME: {
    #             "display_name": "下次执行时间",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         RankingKeys.STATE: {
    #             "display_name": "启用状态",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #     }
    # },

    # ConfigSections.BATTLEDESTORY: {
    #     "display_name": "战斗",
    #     "description": "",
    #     "fields": {
    #         BattleDestoryKeys.ENDTIME: {
    #             "display_name": "ENDTIME",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         BattleDestoryKeys.LOOPTIME: {
    #             "display_name": "LOOPTIME",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         BattleDestoryKeys.NEXTTIME: {
    #             "display_name": "下次执行时间",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #         BattleDestoryKeys.STATE: {
    #             "display_name": "启用状态",
    #             "description": "",
    #             "input_type": "str",
    #             "option": "",
    #             "category": "connection",
    #         },
    #     }
    # },

    ConfigSections.PRACTICE_LAND: {
        "display_name": "扫荡",
        "description": "扫荡练级",
        "fields": {
            PracticeLandKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            PracticeLandKeys.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            PracticeLandKeys.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            PracticeLandKeys.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MAX_DISTANCE: {
                "display_name": "最大行动距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            PracticeLandKeys.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },
            PracticeLandKeys.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            PracticeLandKeys.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            PracticeLandKeys.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.PRACTICE_LAND_1: {
        "display_name": "扫荡",
        "description": "扫荡练级",
        "fields": {
            PracticeLandKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            PracticeLandKeys.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            PracticeLandKeys.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            PracticeLandKeys.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MAX_DISTANCE: {
                "display_name": "最大行动距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            PracticeLandKeys.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },
            PracticeLandKeys.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            PracticeLandKeys.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            PracticeLandKeys.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.PRACTICE_LAND_2: {
        "display_name": "扫荡",
        "description": "扫荡练级",
        "fields": {
            PracticeLandKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            PracticeLandKeys.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            PracticeLandKeys.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            PracticeLandKeys.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MAX_DISTANCE: {
                "display_name": "最大行动距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            PracticeLandKeys.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },
            PracticeLandKeys.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            PracticeLandKeys.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            PracticeLandKeys.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.PRACTICE_LAND_3: {
        "display_name": "扫荡",
        "description": "扫荡练级",
        "fields": {
            PracticeLandKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            PracticeLandKeys.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            PracticeLandKeys.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            PracticeLandKeys.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MAX_DISTANCE: {
                "display_name": "最大行动距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            PracticeLandKeys.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },
            PracticeLandKeys.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            PracticeLandKeys.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            PracticeLandKeys.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.PRACTICE_LAND_4: {
        "display_name": "扫荡",
        "description": "扫荡练级",
        "fields": {
            PracticeLandKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            PracticeLandKeys.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            PracticeLandKeys.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            PracticeLandKeys.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.MAX_DISTANCE: {
                "display_name": "最大行动距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },
            PracticeLandKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            PracticeLandKeys.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            PracticeLandKeys.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },
            PracticeLandKeys.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            PracticeLandKeys.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            PracticeLandKeys.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },

    ConfigSections.ATTACK_LAND: {
        "display_name": "出征",
        "description": "",
        "fields": {
            ATTACK_LAND.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            ATTACK_LAND.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            ATTACK_LAND.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            ATTACK_LAND.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MAX_DISTANCE: {
                "display_name": "最大出征距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },

            ATTACK_LAND.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            ATTACK_LAND.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },

            ATTACK_LAND.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            ATTACK_LAND.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            ATTACK_LAND.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.ATTACK_LAND_1: {
        "display_name": "出征",
        "description": "",
        "fields": {
            ATTACK_LAND.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            ATTACK_LAND.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            ATTACK_LAND.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            ATTACK_LAND.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MAX_DISTANCE: {
                "display_name": "最大出征距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },

            ATTACK_LAND.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            ATTACK_LAND.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },

            ATTACK_LAND.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            ATTACK_LAND.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            ATTACK_LAND.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.ATTACK_LAND_2: {
        "display_name": "出征",
        "description": "",
        "fields": {
            ATTACK_LAND.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            ATTACK_LAND.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            ATTACK_LAND.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            ATTACK_LAND.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MAX_DISTANCE: {
                "display_name": "最大出征距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },

            ATTACK_LAND.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            ATTACK_LAND.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },

            ATTACK_LAND.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            ATTACK_LAND.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            ATTACK_LAND.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.ATTACK_LAND_3: {
        "display_name": "出征",
        "description": "",
        "fields": {
            ATTACK_LAND.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            ATTACK_LAND.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            ATTACK_LAND.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            ATTACK_LAND.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MAX_DISTANCE: {
                "display_name": "最大出征距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },

            ATTACK_LAND.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            ATTACK_LAND.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },

            ATTACK_LAND.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            ATTACK_LAND.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            ATTACK_LAND.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },
    ConfigSections.ATTACK_LAND_4: {
        "display_name": "出征",
        "description": "",
        "fields": {
            ATTACK_LAND.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            ATTACK_LAND.ACTION_LIST: {
                "display_name": "部队编号",
                "description": "要塞/主城的部队位置",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.ADDRESS: {
                "display_name": "行动位置",
                "description": "主城位置留空，要塞出发填写要塞名",
                "input_type": "str",
                "category": "basic",
            },
            ATTACK_LAND.DRAFT: {
                "display_name": "战斗后是否征兵",
                "description": "不论是否选中，首次出发会征满兵",
                "input_type": "checkbox",
                "category": "battle",
            },
            ATTACK_LAND.ENEMY_REMAINING: {
                "display_name": "敌军平局",
                "description": "平局时，守军小于该数量，则等待下一次战斗。",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MY_REMAINING: {
                "display_name": "我方平局",
                "description": "平局时，我方兵力大于该数量，则等待下一次战斗",
                "input_type": "number",
                "category": "battle",
            },
            ATTACK_LAND.MAX_DISTANCE: {
                "display_name": "最大出征距离",
                "description": "默认值300~~~",
                "input_type": "number",
                "category": "battle",
            },

            ATTACK_LAND.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            ATTACK_LAND.NUM: {
                "display_name": "主城位置",
                "description": "此处填写的坐标是在主城页面里，部队位置的编号",
                "input_type": "option",
                "option": [1, 2, 3, 4, 5],
                "category": "basic",
            },
            ATTACK_LAND.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },

            ATTACK_LAND.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "出发/撤退耗费时间，一般不需要手动更改",
                "input_type": "number",
                "category": "basic",
            },
            ATTACK_LAND.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            ATTACK_LAND.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },

    ConfigSections.SPARTA_ATTACK_LAND: {
        "display_name": "斯巴达攻击",
        "description": "",
        "fields": {
            SPARTA_ATTACK_LAND.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            SPARTA_ATTACK_LAND.ADDRESS: {
                "display_name": "排除的位置",
                "description": "填写的要塞名将会排除，以','分割，示例：排除要塞1,排除要塞2 ",
                "input_type": "str",
                "category": "basic",
            },
            SPARTA_ATTACK_LAND.MAX_DISTANCE: {
                "display_name": "最大出征距离",
                "description": "超过战场太远的斯巴达可能是主城原先待命的部队",
                "input_type": "number",
                "category": "basic",
            },
            SPARTA_ATTACK_LAND.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            SPARTA_ATTACK_LAND.STAGE: {
                "display_name": "执行步骤",
                "description": "当前队伍步骤阶段。不需要手动更改",
                "input_type": "number",
                "category": "schedule",
            },
            SPARTA_ATTACK_LAND.TIME_CONSUMING: {
                "display_name": "耗时",
                "description": "此处耗时为斯巴达进攻时间最长的那个，一般不需要手动修改",
                "input_type": "number",
                "category": "basic",
            },
            SPARTA_ATTACK_LAND.X: {
                "display_name": "土地坐标X",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
            SPARTA_ATTACK_LAND.Y: {
                "display_name": "土地坐标Y",
                "description": "土地的X坐标，以逗号分割，左侧坐标",
                "input_type": "number",
                "category": "position",
            },
        }
    },

    ConfigSections.MartialArts: {
        "display_name": "演武",
        "description": "",
        "fields": {
            MartialArtsKeys.STATE: {
                "display_name": "状态",
                "description": "",
                "input_type": "checkbox",
                "category": "schedule",
            },
            MartialArtsKeys.DIFFICULTY: {
                "display_name": "演武难度",
                "description": "",
                "input_type": "option",
                "option": ['简单', '普通', '困难', '极难1', '极难2'],
                "category": "basic",
            },
            MartialArtsKeys.NEXTTIME: {
                "display_name": "下次执行时间",
                "description": "一般不需要手动修改",
                "input_type": "datetime",
                "category": "schedule",
            },
            MartialArtsKeys.RETRY: {
                "display_name": "重试最大次数",
                "description": "挑战失败后重试最大次数，默认20",
                "input_type": "number",
                "category": "basic",
            },
        }
    }
}

field_categories = {
    "schedule": {"display_name": "时间设置", "order": 1},
    "basic": {"display_name": "基本设置", "order": 2},
    "position": {"display_name": "坐标设置", "order": 3},
    "battle": {"display_name": "战斗设置", "order": 4},
    "connection": {"display_name": "连接设置", "order": 5}
}
