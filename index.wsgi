import os

from start import robot

application = sae.create_wsgi_app(robot.wsgi)