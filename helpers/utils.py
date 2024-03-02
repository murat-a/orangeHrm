import os
import shutil
import random
import string

class Utils:

    def __init__(self, app):
        self.app = app
        self.step = self.app.step
        self.wd = self.app.wd

    def generate_random_email(domain='example.com', length=15):
        characters = string.ascii_letters + string.digits
        local_part = ''.join(random.choice(characters) for i in range(length))
        return f"{local_part}@{domain}"