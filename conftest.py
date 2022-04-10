import pytest
from django.contrib.auth.models import Group


@pytest.fixture(scope='function')
def user(db, django_user_model):
    """
    User instance from default django user model
    """
    Group.objects.create(name='students')
    print('\nbefore test (setup)')
    yield django_user_model.objects.create_user(email='a@a.pl', fullname='Ala', password='testPAss123')
    print('\nafter test (teardown)')
