class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True

    for g in group.groups:
        if is_user_in_group(user, g):
            return True

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

br1 = Group('branch1')
br1.add_user('branch1_user')

parent.add_group(br1)

br2 = Group('branch2')
br2.add_user('branch2_user')

sub_child.add_group(br2)

assert(is_user_in_group('sub_child_user', parent) == True)
assert(is_user_in_group('branch1_user', parent) == True)
assert(is_user_in_group('branch2_user', parent) == True)
assert(is_user_in_group('Slavko', parent) == False)
assert(is_user_in_group('', parent) == False)
