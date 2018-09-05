"""HTTP Handlers for the hub server"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from .base import BaseHandler

class AutoLoginHandler(BaseHandler):
    """Log a user out by clearing their login cookie."""

    def get(self):
        self.log.warning("auto login begin")
        username = self.get_argument('username', default='')
        password = self.get_argument('password', default='')
        self.log.warning("username=" + username + ", password=" + password)
        html = self.render_template('auto_login.html',
                                    username=username,
                                    password=password)
        self.finish(html)
        self.log.warning("auto login end")

# /login renders the login page or the "Login with..." link,
# so it should always be registered.
# /logout clears cookies.
default_handlers = [
    (r"/auto_login", AutoLoginHandler)
]
