def test_new_user(new_user):
    """
    creates a new User, using the User model, and checks
    that name and password fields are filled properly.
    """

    assert new_user.name == 'Eric Anderson'
    assert new_user.password == 'testpass'
