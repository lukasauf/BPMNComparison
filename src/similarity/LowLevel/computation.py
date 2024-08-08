from src.similarity.LowLevel.bert import compute_bert_similarity
from src.similarity.LowLevel.glove import compute_glove_similarity
from src.similarity.LowLevel.syntactic import compute_syntactic_similarity
import sys

def compute_similarity(sm_element, gm_elements, weights):
    """
    Compute the low level similarity between sm_element and the gm_elements with respect to
    the input weights

    Args:
        sm_element (str): The text element for which the similarity is to be computed.
        gm_elements (list of str): A list of text elements to compare against `sm_element`.
        weights (dict): Weights for the low level similarity to be applied (glove/BERT/syntactic)
    
    Returns: 
        list: List of similarity values between sm_element and the gm_elements     
    """
    compare_nodes = [sm_element] + gm_elements
    similarities = None
    #Note: there are 7 different combinations of the 3 weight variables    
    if weights['glove'] == 0:
       if weights['bert'] == 0:
           similarities = compute_syntactic_similarity(sm_element, gm_elements)
           
       elif weights['syntactic'] == 0:
           similarities = compute_bert_similarity(compare_nodes)
       
       #both bert and syntactic are not 0 
       else: 
           bert_similarities = compute_bert_similarity(compare_nodes)  
           syntactic_similarities = compute_syntactic_similarity(sm_element, gm_elements)
           similarities = [(bert * weights['bert'] + syn * weights['syntactic']) for bert, syn in zip(bert_similarities, syntactic_similarities)]   
    
    else:
        if weights['bert'] == 0:
            if weights['syntactic'] == 0:
                similarities = compute_glove_similarity(sm_element, gm_elements)
            
            #both glove and syntactic are not 0 
            else:
                 glove_similarities = compute_glove_similarity(sm_element, gm_elements)
                 syntactic_similarities = compute_syntactic_similarity(sm_element, gm_elements)       
                 similarities = [(glove * weights['glove'] + syn * weights['syntactic']) for glove, syn in zip(glove_similarities, syntactic_similarities)]
        else:
            if weights['syntactic'] == 0:
                glove_similarities = compute_glove_similarity(sm_element, gm_elements)
                bert_similarities = compute_bert_similarity(compare_nodes)  
                similarities = [(glove * weights['glove'] + bert * weights['bert']) for glove, bert in zip(glove_similarities, bert_similarities)] 
            
            #all elements are not 0 
            else:
                glove_similarities = compute_glove_similarity(sm_element, gm_elements)
                bert_similarities = compute_bert_similarity(compare_nodes)  
                syntactic_similarities = compute_syntactic_similarity(sm_element, gm_elements)  
                similarities = [(glove * weights['glove'] + bert * weights['bert'] + syn * weights['syntactic']) for glove, bert, syn in zip(glove_similarities, bert_similarities, syntactic_similarities)] 
    
    if similarities is None:
        print(f'Error: Calculated similarity of the sm_element {sm_element} and the gm_elements {gm_elements} is None!')
        sys.exit(1)
    return similarities        