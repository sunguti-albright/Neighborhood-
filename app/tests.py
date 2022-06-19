from django.test import TestCase
from .models import Neighbourhood, Business
from django.contrib.auth.models import User


class TestNeighborhood(TestCase):
    def setUp(self):
        self.new_user = User(
            username='test', email='test@gmail.com', password='password')
        self.new_user.save()

        self.new_hood = Neighbourhood(
            admin=self.new_user, hood_name='Cairo', location='Egypt')
        self.new_hood.save()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood, Neighbourhood))

    # Testing Save Method
    def test_save_method(self):
        self.new_hood.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.new_hood.delete_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) == 0)

    # Testing Getting Hood by id
    def test_get_hood_method(self):
        self.new_hoodnew_hood = Neighbourhood.get_hood_by_id(self.new_hood.id)
        self.assertTrue(isinstance(self.new_hood.id, self.new_hood.id))

    # Testing getting all neigbourhoods
    def test_get_all_neigbourhoods(self):
        hoods = Neighbourhood.get_all_hoods()
        self.assertTrue(len(hoods) == 1)


class TestBusiness(TestCase):
    def setUp(self):
        self.new_user = User(
            username='test', email='test@gmail.com', password='password')
        self.new_hood = Neighbourhood(
            admin=self.new_user, hood_name='Cairo', location='Egypt')
        self.new_biz = Business(business_name='Fastfood', business_email='fastfood@gmail.com',
                                user=self.new_user, neighborhood=self.new_hood)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_biz, Business))

    # Test Find Biz
    def test_find_business_method(self):
        biz = Business.search_biz_by_title(self.new_biz.id)
        self.assertEqual(biz.id, type([self.new_biz.id]))