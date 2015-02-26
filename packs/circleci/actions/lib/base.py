
import os
import requests
from circleclient import circleclient

from st2actions.runners.pythonrunner import Action

__all__ = [
    'BaseCircleciAction'
]

BASE_URL = 'https://github.com'

class BaseCircleciAction(Action):
    def __init__(self, config):
        super(BaseCircleciAction, self).__init__(config=config)
        self.cci_token = config.get("cci_token")
        self._client = circleclient.CircleClient(self.cci_token)
