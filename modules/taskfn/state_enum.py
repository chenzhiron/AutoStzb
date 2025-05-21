from enum import Enum


class State(Enum):
    """所有可能的游戏状态"""
    INIT = 'INIT'
    DRAFT = "DRAFT"
    SEARCH_MAP = "SEARCH_MAP"
    GO_MAP = "GO_MAP"
    LIST_ACTION = 'LIST_ACTION'
    RESULT = "RESULT"
    DRAW = 'DRAW'
    END = "END"
    ACTION_END = 'ACTION_END'
    ACTION_AWAIT = 'ACTION_AWAIT'
    ACTION_WITHDRAW = 'ACTION_DRAW'