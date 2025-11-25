

import auth


def test_auth_functionality():
    """Test the authentication functionality"""
    assert auth.authenticate("admin", "password123") is True
    assert auth.authenticate("user", "wrongpassword") is False
def test_auth_invalid_user():   



#TODO   """Test authentication with invalid user"""

#TODO Run with a framework  end to end 