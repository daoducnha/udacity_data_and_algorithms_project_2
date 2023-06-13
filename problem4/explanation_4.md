function is_user_in_group takes two arguments: user and group. It checks if the user is in the group or any of its child groups
    The function will check if the user is in the group returns True.
    If the user is not found in the group, the function recursively checks each child group of the group by iterating over the groups attribute of the group.
    If the user is not found in the group or any of its child groups, returns False.
Big0 of this function is O(n) because the function may need to traverse the entire hierarchy to find the user