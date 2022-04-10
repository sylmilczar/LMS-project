def test_create_user(user, django_user_model):
    print('test')
    users = django_user_model.objects.all()
    assert len(users) == 1


def test_change_password(user):
    print('test')
    user.set_password('secret')
    assert user.check_password('secret') is True
