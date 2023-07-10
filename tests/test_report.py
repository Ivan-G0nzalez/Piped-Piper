import unittest

from app.utils.config import TestConfig 
from main import create_app
from app.models.exts import db

class TestDevices(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)

            db.create_all()

    def test_report(self):
        data_post = {
            "client_count": 8,
            "cpu_utiization": 80,
            "firmware_version": "4.0v",
            "labels": "asdasd",
            "macaddr": "123546",
            "mem_free": 20,
            "mem_total": 1206,
            "model": "router",
            "name": "router1",
            "stack_id": 12345,
            "status": "up",
            "temperature": "20",
            "uptime": 0,
            "uplink_ports": "",
            "components_id": 3
            }
        
        response_post = self.client.post('/devices/devices', json=data_post)
        data = response_post.get_json()
        serial = data['serial']

        response_get = self.client.get(f'/report/configuration?serial=%s' % serial)

        expected_response = {"response": "Report was successfully created"}
        self.assertEqual(response_get.get_json(), expected_response)        

    def test_performace(self):
        data_post = {
            "client_count": 8,
            "cpu_utiization": 80,
            "firmware_version": "4.0v",
            "labels": "asdasd",
            "macaddr": "123546",
            "mem_free": 20,
            "mem_total": 1206,
            "model": "router",
            "name": "router2",
            "stack_id": 12345,
            "status": "up",
            "temperature": "20",
            "uptime": 0,
            "uplink_ports": "",
            "components_id": 3
            }
        
        response_post = self.client.post('/devices/devices', json=data_post)
        data = response_post.get_json()
        serial = data['serial']

        response_get = self.client.get(f'/report/performace?serial=%s' % serial)

        expected_response = {"response":"Performance report created"}

        self.assertEqual(response_get.get_json(), expected_response)

    def test_tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()       