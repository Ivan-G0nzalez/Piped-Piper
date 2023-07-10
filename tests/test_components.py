import unittest

from app.utils.config import TestConfig 
from main import create_app
from app.models.exts import db

class TestComponents(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)

            db.create_all()

    def test_get_components(self):
        response = self.client.get('/api/components')
        status_code = response.status_code

        self.assertEqual(status_code, 200)

    def test_get_one_component(self):
        print("+++++++++++++++++++++++++++++++++++++++++")
        response = self.client.get('/api/component/1')
        print(f"########{response}")
        status_code = response.status_code

        self.assertEqual(status_code, 404)

    def test_post_one_component(self):
        response = self.client.post('/api/components', json={"name":"test"})
        status_code = response.status_code

        self.assertEqual(status_code, 201)

    def test_update_component(self):
        response_post = self.client.post('/api/components', json={"name":"test"})  

        response_put = self.client.put('/api/component/1', json={"name":"test2"})

        status_code = response_put.status_code

        self.assertEqual(status_code, 200)

    def test_delete_component(self):
        response_post = self.client.post('/api/components', json={"name":"test"})

        delete_component = self.client.delete('/api/component/1')

        status_code = delete_component.status_code

        self.assertEqual(status_code, 200)


    def test_tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    