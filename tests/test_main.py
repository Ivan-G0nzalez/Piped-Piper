# from flask_testing import TestCase
# from flask import current_app, jsonify


# from main import app
# from app.models.network_component import NetworkComponent

# from mock import ANY
# import json
# import unittest
# import uuid

# class MainTest(TestCase):
#     def create_app(self):
#         app.config['TESTING'] = True
#         app.config['WTF_CSRF_ENABLE'] = False
#         return app
    
#     def test_app_exist(self):
#         self.assertIsNotNone(current_app)
    
#     def test_app_in_test_mode(self):
#         self.assertTrue(current_app.config['TESTING'])

#     def test_get_component(self):
#         expected_response = [
#             {
#                 "id": ANY,
#                 "name":ANY
#             }
#         ]

#         response = self.client.get('/api/components')
#         self.assert200(response)
#         for expected_item, actual_item in zip(expected_response, response.json):
#             self.assertEqual(expected_item.keys(), actual_item.keys())
    
#     def test_post_component(self):
#         request_data = {
#             "name": "Test Component"
#         }

#         response = self.client.post('/api/components', json=request_data)
#         self.assertEqual(response.status_code, 201)
#         expected_response = {"response": "successfully added"}
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertEqual(response_data, expected_response)

#     def test_update_component(self):
#         response = self.client.put('/api/components/2', json={'name': 'Updated Component Name'})
        
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.json, {"response": "successfully update"})   

#     def test_delete_component(self):
#         response = self.client.delete('/api/components/1')
        
#         self.assert200(response)
#         self.assertEqual(response.json, {"response": "Successfully deactivated"}) 

#     def test_get_devices(self):
#         expected_response = [
#             {
#             "id": ANY,
#             "client_count": ANY,
#             "cpu_utilization": ANY,
#             "firmware_version": ANY,
#             "labels": ANY,
#             "macaddr": ANY,
#             "men_free": ANY,
#             "men_total": ANY,
#             "model": ANY,
#             "name": ANY,
#             "serial": ANY,
#             "stack_id": ANY,
#             "status": ANY,
#             "temperature": ANY,
#             "uptime": ANY,
#             "uplink_port": ANY
#             }
#         ]

#         response = self.client.get('/api/devices')
#         self.assert200(response)
#         for expected_item, actual_item in zip(expected_response, response.json):
#             self.assertEqual(expected_item.keys(), actual_item.keys())

#     def test_post_devices(self):
#         expected_response = {
#                 'client_count':5,
#                 'cpu_utilization':80,
#                 'firmware_version':'1.0',
#                 'labels':'label1',
#                 'macaddr':'00:11:22:33:44:55',
#                 'mem_free':1024,
#                 'mem_total':2048,
#                 'model':'Device Model',
#                 'name':'Device Name',
#                 'serial': str(uuid.uuid4()),
#                 'stack_id':"123456",
#                 'status':'up',
#                 'temperature': '30.5',
#                 'uptime': 3600,
#                 'uplink_ports':'port1',
#                 'components_id': 1
#                 }
        

#         response = self.client.post('/api/devices', json=expected_response)
#         self.assertEqual(response.status_code, 200)
#         expected_response = {"response":"successfully added"}
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertEqual(response_data, expected_response)

#     def test_update_component(self):
        
#         data = {
#                 'client_count':5,
#                 'cpu_utilization':80,
#                 'firmware_version':'1.0',
#                 'labels':'label1',
#                 'macaddr':'00:11:22:33:44:55',
#                 'mem_free':1024,
#                 'mem_total':2048,
#                 'model':'Device Model',
#                 'name':'Device Name',
#                 'stack_id':'12345',
#                 'serial': 'example_serial',
#                 'status':'up',
#                 'temperature': '30.5',
#                 'uptime': 3600,
#                 }    

#         response = self.client.put('/api/devices/2', json=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json, {"response": "successfully update"})

#     def test_delete_component(self):
#         response = self.client.delete('/api/devices/1')
        
#         self.assert200(response)
#         self.assertEqual(response.json, {"response": "Successfully deactivated"}) 
        

# if __name__ == '__main__':
#     unittest.main()