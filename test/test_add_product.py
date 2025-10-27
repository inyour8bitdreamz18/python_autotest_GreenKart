import pytest
from fixture.application import Application
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_product(app):
    app.session.login((User(loginname="admin.anna", password="admin",
                        firstname=None, lastname=None, email=None,
                        telephone=None, fax=None, company=None,
                        address1=None, address2=None,
                        city=None, zone_id=None, postcode=None, country_id=None)))

    app.open_home_page()
    app.add_product()
    app.open_cart()
    app.session.logout()
