
from app import create_app, sqlalchemy as db
from app.config import TestingConfig
from model.Events import Events
import unittest





class EventAppTestCase(unittest.TestCase):
    """This class represents the Event App test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client
        self.user = {"firstname":"chetat", "lastname":"Wilfred","email":"yekuwilfre@gmail.com", "phone": "671357962"}
        
        with self.app.app_context():
            db.create_all()

    def test_given_behavior(self):
        """Test create user endpoint """
        res = self.client().post('api/v1/events',  json = self.user)
        self.assertEqual(res.status_code, 201)
        
    def test_invalid_userid(self):
        err = self.client().post(f'api/v1/events/{id}', json = {'id': id})
        self.assertEqual()
        print("\nCreating new Users ==============")

    def test_get_all_events(self):
        """Test create user endpoint """
        res = self.client().get('api/v1/events')
        print("Getting Users ==============")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json['success'], True)

    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
            #Drop all tables
            db.session.remove()
            db.drop_all()
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()