import sys 

def check_index_access(list, i):
    """
    Check if accessing the element at index i of the list is valid.
    If the index is out of bounds, print an error message and terminate the program.

    Args:
        list (list): The list to check.
        i (int): The index to check.

    """
    if 0 <= i < len(list):
        # Access is valid, do nothing
        pass
    else:
        # Access is invalid, print error message and terminate the program
        print(f"Error: Index {i} is out of bounds for the list of length {len(list)}.")
        sys.exit(1)
        

def get_value(key, model):
    """
    Get the value of the key (stored in the list_edges list) for comparison

    Args:
        key (str): Unique key linked to a single element of the BPMN model  
        model (BPMN): BPMN model to be considered for searching key

    Returns:
        str: Value linked to the key of the BPMN model (could be a task/event/gateway)
    """
    if 'event' in key:
        return model.events[key]
    elif 'task' in key:
        return model.tasks[key]
    elif 'gateway' in key:
        return model.gateways[key]
    else:
        print("Error: Invalid key!")
        sys.exit(1) 
    

def get_type(key):
    """
    Get the type of the key (stored in the list_edges list)

    Args:
        key (str): Unique key linked to a single element of the BPMN model  

    Returns:
        str: Value linked to the key of the BPMN model
    """
    if 'event' in key:
        return 'event'
    elif 'task' in key:
        return 'task'
    elif 'exclusivegateway' in key:
        return 'exclusivegateway'
    elif 'parallelgateway' in key:
        return 'parallelgateway'
    else:
        print("Error: Invalid key!")
        sys.exit(1)                          