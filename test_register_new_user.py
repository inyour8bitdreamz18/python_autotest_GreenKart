# -*- coding: utf-8 -*-
import pytest
from application import Application
from user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_register_user(app):
    app.fill_user_info(User(firstname="Anna", lastname="User", email="user_20@gmail.com",
                            telephone="+123545789", fax="+148234578", company="Learning Automation",
                            address1="str.Learn, 211", address2="str. Quality Assurance, 12",
                            city="London", zone_id="Cheshire", postcode="1234567", country_id="United Kingdom",
                            loginname="anna_user20", password="anna_user20"))

    app.confirm_registration_info()
    app.open_success_registration_page()

    
