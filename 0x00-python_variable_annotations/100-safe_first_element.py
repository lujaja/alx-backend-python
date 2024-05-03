# The types of the elements of the input are not know
def safe_first_element(lst):
    """
    Returns the first element of the input list if the list is not empty, otherwise returns None.
    
    :param lst: A list of elements.
    :type lst: list
    :return: The first element of the input list if the list is not empty, otherwise None.
    :rtype: Any or None
    """
    return lst[0] if lst else None
