import sys
import logging

sys.path.insert(0, '/usr/local/lib/python3.12/dist-packages')

# Add your Flask app directory
sys.path.insert(0, '/var/www/flaskapp')
logging.basicConfig(stream=sys.stderr)

from website import create_app
application = create_app()
