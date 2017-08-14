from models.model_group import Group

def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(group_name='a', group_header='b', group_footer='c'))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.pop(0)
    assert old_groups == new_groups



