"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from website.models import Users


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    user = Users('TestEmail@test.com', 'TestPassword')
    assert user.email == 'TestEmail@test.com'
    assert user.hashed_password != 'TestPassword'
    assert user.__repr__() == '<User: TestEmail@test.com>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert new_user.email == 'TestEmail@test.com'
    assert new_user.hashed_password != 'TestPassword'
