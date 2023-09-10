import logging

from tasks.zhengbing import zhengbing
from tasks.saodang import saodang
from tasks.battle import battle

task_config_obj = {}


def add_task_config_obj(task_config):
    if task_config['type'] == 1:
        task_config_obj[task_config['id']] = [{
            'id': task_config['id'],
            'handle': zhengbing
        }]
    if task_config['type'] == 2:
        current_task_group = [{
            'id': task_config['id'],
            'handle': saodang
        }, {
            'id': task_config['id'],
            'handle': battle
        }, {
            'id': task_config['id'],
            'handle': battle
        },
            {
            'id': task_config['id'],
            'handle': zhengbing
        }]
        task_config_obj[task_config['id']] = current_task_group * task_config['number']


def remove_task_config(ids):
    task_config_obj[ids].pop(0)


def insertion_task_config(ids, task_config):
    task_config_obj[ids].insert(0, task_config)


def return_task_config_obj():
    return task_config_obj
