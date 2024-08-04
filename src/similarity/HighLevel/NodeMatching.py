# Importing libraries for similarity score

from src.util.helpers import check_index_access
from src.util.helpers import get_value
from src.similarity.LowLevel.computation import compute_similarity
"""_summary_
"""



def max_with_index(lst):
    """
    Get the max value of the list with its corresponding index

    Args:
        lst (list): List to be processed

    Returns:
        tuple: Tuple of the max. value with its index in the list
    """  
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_value, max_index

def compare_models_nm(sm, gm, weights, threshold):
    """
    Compare the two models Standard Model (SM) and Generated Model (GM) with the EdgeMatching1 algorithm.
    The node matching and corresponding optimal equivalence mapping between SM and GM is computed.
    

    Args:
        sm (BPMN): The standard BPMN model (created by a human process modeler)
        gm (BPMN): The generated BPMN model (generated by the AI)
        weights (dict): Weights for the low level similarity to be applied (glove/BERT/syntactic)
        threshold (float): Threshold for accepting the similarity value: Let elem1 and elem2 be text labels,  if sim(elem1, elem2) > threshold --> elem1 and elem2 are considered equal 

    Returns: 
        list: The optimal equivalence mapping between the two sets of tasks/nodes of SM and GM as a list of tuples, i.e.:
        [(sm_task_key1, gm_task_key2), (sm_task_key3, gm_task_key3),...]      
    """
    opt_eq_map = []
    gm_keys = list(gm.tasks.keys())
    gm_values = list(gm.tasks.values())
    
    for sm_key in sm.tasks:
        similarity_scores = compute_similarity(sm.tasks[sm_key], gm_values, weights)
        max_value, max_index = max_with_index(similarity_scores)
        print(f'Max value is {max_value} and max index is {max_index}')
        
        if max_value > threshold:
            gm_key = gm_keys[max_index]
            #ensure that nodes should only be mapped 1:1 and not i.e. n:1
            if all(sm_key != pair[0] for pair in opt_eq_map) and all(gm_key != pair[1] for pair in opt_eq_map):
                print('****************************')
                print(f'sm_key is {sm_key} and gm_key is {gm_key}')
                print('****************************')
                opt_eq_map.append((sm_key, gm_key))
    return opt_eq_map




            