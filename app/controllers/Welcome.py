"""
    Sample Controller File
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        # self.load_model('WelcomeModel')

    def index(self):
        # self.models['WelcomeModel'].get_all_users()
        return self.load_view('index.html')
