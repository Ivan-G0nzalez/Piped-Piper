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
    

    def test_get_device(self):
        response = self.client.get('/devices/devices')
        status_code = response.status_code

        self.assertEqual(status_code, 200)

    def test_get_one_device(self):
        response = self.client.get('/devices/device/1')
        
        status_code = response.status_code

        self.assertEqual(status_code, 404)

    def test_post_one_device(self):
        
        data = {
            "client_count":1, 
            "cpu_utiization":40,
            "firmware_version": "",
            "labels":"",
            "macaddr":"",
            "mem_free": 10,
            "mem_total":1024,
            "model": "",
            "name": "switch24",
            "serial":123456847,
            "stack_id": 0,
            "status": "up",
            "temperature":4,
            "uptime": 0,
            "uplink_ports": "prueba",
            "components_id": 1
            }
        
        response = self.client.post('/devices/devices', json=data)
        status_code = response.status_code

        self.assertEqual(201, status_code)

    def test_update_device(self):
        data_post = {
            "client_count": 4,
            "cpu_utiization": 80,
            "firmware_version": "4.0v",
            "labels": "asdasd",
            "macaddr": "123546",
            "mem_free": 20,
            "mem_total": 1206,
            "model": "router",
            "name": "router_3",
            "stack_id": 12345,
            "status": "up",
            "temperature": "20",
            "uptime": 0,
            "uplink_ports": "",
            "components_id": 3
            }
        
        
        data_update = {
            "client_count": 8,
            "cpu_utiization": 70,
            "firmware_version": "4.0v",
            "labels": "asdasd",
            "macaddr": "123546",
            "mem_free": 20,
            "mem_total": 1206,
            "model": "router",
            "name": "router_4",
            "stack_id": 12345,
            "status": "up",
            "temperature": "20",
            "uptime": 0,
            "uplink_ports": "",
            "components_id": 3
            }

        response_post = self.client.post('/devices/devices', json=data_post)
        response_update = self.client.put('/devices/device/1', json=data_update)

        status_code = response_update.status_code

        self.assertEqual(200, status_code)


    def test_delete_device(self):
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
        
        self.assertEqual(response_post.status_code, 201)
        
        response_delete = self.client.delete('/devices/device/1')

        status_code = response_delete.status_code
        self.assertEqual(status_code, 200)


    def test_tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()        