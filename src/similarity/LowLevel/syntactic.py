import Levenshtein

    

def compute_syntactic_similarity(sm_element, gm_elements):
    """
    Compute the syntactic similarity between a SM text element and all the elements of GM.

    This function uses the Levenshtein distance to compute the similarity between the `sm_element` and 
    each element in `gm_elements`. The similarity is calculated as 1 - (Levenshtein distance / maximum length of the two strings).

    Args:
        sm_element (str): The text element for which the similarity is to be computed.
        gm_elements (list of str): A list of text elements to compare against `sm_element`.

    Returns:
        list of float: A list of similarity scores, one for each element in `gm_elements`.
    """
    
    def syn(l1, l2):
        ed = Levenshtein.distance(l1, l2)
        return 1 - ed / max(len(l1), len(l2))
    
    similarities = []
    for gm_element in gm_elements:
        similarity = syn(sm_element, gm_element)
        similarities.append(similarity)

    return similarities
