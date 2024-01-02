import os
import subprocess

import yaml


class EnvironmentSetup:
    def __init__(self):
        self.config = {}
        self.script_path = os.path.abspath(os.path.dirname(__file__))
        self.python_executable = None
        self.pip_executable = None
        self.git_bash_path = None
        self.requirements_file = None
        self.whl_file = None
        self.main_script = None

    def load_config(self, file_path):
        with open(file_path, 'r') as stream:
            self.config = yaml.safe_load(stream)
        self.setup_environment_variables()

    def setup_environment_variables(self):
        self.python_executable = self.config['Python']['executable']
        self.pip_executable = os.path.join(self.script_path, self.config['Python']['pip'])
        self.git_bash_path = os.path.join(self.script_path, self.config['Git']['executable'])
        self.requirements_file = os.path.join(self.script_path, self.config['Python']['package'])
        self.whl_file = os.path.join(self.script_path, 'toolkit', 'future-0.18.3-py3-none-any.whl')
        self.main_script = os.path.join(self.script_path, 'main.py')

    def run(self):
        self.set_environment_variables()
        self.reset_and_update_git()
        self.install_pip()
        self.install_whl_package()
        self.install_requirements()
        self.run_main_script()

    def set_environment_variables(self):
        os.environ['PATH'] += os.pathsep + os.path.join(self.script_path, 'toolkit', 'Scripts')
        os.environ['PATH'] += os.pathsep + self.git_bash_path

    def reset_and_update_git(self):
        subprocess.call([self.git_bash_path, '-c', "git reset --hard && git pull"])

    def install_pip(self):
        subprocess.call([self.python_executable, os.path.join(self.script_path, 'toolkit', 'get_pip.py')])

    def install_whl_package(self):
        subprocess.call([self.pip_executable, 'install', self.whl_file])

    def install_requirements(self):
        subprocess.call([self.python_executable, self.pip_executable, 'install', '--no-warn-script-location', '-r',
                         self.requirements_file])

    def run_main_script(self):
        subprocess.call([self.python_executable, self.main_script])

# # 创建环境设置对象
# env_setup = EnvironmentSetup()
#
# # 加载配置
# env_setup.load_config(config_file_path)
#
# # 运行所有设置步骤
# env_setup.run()
