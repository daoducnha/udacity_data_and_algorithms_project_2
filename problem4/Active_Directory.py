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


    child_groups = group.groups

    for child_group in child_groups:
        if is_user_in_group(user, child_group):
            return True
    return False


## Test Case 1
print("=============Test case 1=============")

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
parent.add_group(child)
child.add_group(sub_child)
sub_child.add_user(sub_child_user)

assert is_user_in_group(sub_child_user, parent) == True

## Test Case 2
print("=============Test case 2=============")

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)
new_user = "new_user"

assert is_user_in_group(new_user, parent) == False

## Test Case 3
print("=============Test case 3=============")
parent = Group("parent")
child = Group("child")
child2 = Group("child2")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")
sub_child_user2 = "sub_child_user2"

parent.add_group(child)
parent.add_group(child2)
child.add_group(sub_child)
child2.add_group(sub_child2)
sub_child2.add_user(sub_child_user2)

assert is_user_in_group(sub_child_user2, parent) == True