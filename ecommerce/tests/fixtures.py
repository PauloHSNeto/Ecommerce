import pytest
from django.contrib.auth.models import User
from django.core.management import call_command



@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return  django_user_model.objects.create_superuser("paulo","a@a.com","senha")




@pytest.fixture(scope ="session")
def django_db_setup(django_db_blocker):
        """
        Load DB data Fixtures
        
       """
   with django_db_blocker.unblock():
        call_command("loaddata","db_admin_fixture.json")  