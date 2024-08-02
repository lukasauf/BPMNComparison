from helper.helpers import check_index_access
import sys 

def calculate_tp_fp_fn(sm_list_edges, gm_list_edges):
    """
    Calculcate the following metrics for the similarity calculation:
      - True Positives (TP): edges, that are generated and exist in the standard model
      - False Positives (FP): edges, that are not generated and exist in the standard model 
      - False Negatives (FN): edges, that are generated and don't exist in the standard model 

    Args:
        sm_list_edges (list): A list of lists where each list represents an edge in the BPMN model (SM)
        gm_list_edges (list): A list of lists where each list represents an edge in the BPMN model (GM)

    Returns:
        tuple: A 3- tuple (tp, fp, fn) indicating the TP, FP and FNs of the models.
    """
    tp = 0
    fp = 0
    for sm_edge in sm_list_edges:
        check_index_access(sm_edge, 2)
        if sm_edge[2] == 1:
            tp += 1
        elif sm_edge[2] == 0:
            fp += 1
        else:
            print(f"Error: Index 2 is out of bounds for the sm_list_edges with length {len(sm_edge)}.")
            sys.exit(1)
    
    fn = len(gm_list_edges) - tp
    return tp, fp, fn
                       
            

def calculate_jaccard_index(tp, fp, fn):
    """
    Calculate the Jaccard Index of the two models. It is computed as follows:
       Jaccard Index = TP / (TP + FN + FP)

    Args:
        tp (int): True Positives (TP) - edges, that are generated and exist in the standard model
        fp (int): False Positives (FP) - edges, that are not generated and exist in the standard model 
        fn (int): False Negatives (FN) - edges, that are generated and don't exist in the standard model

    Returns:
        float: the calulated Jaccard Index as a float
    """
    
    return tp /(tp + fp + fn)

def calculate_recall(tp,fn):
    """
    Calculate the recall of the two models. It is computed as follows:
       Recall = TP / (TP + FN)

    Args:
        tp (int): True Positives (TP) - edges, that are generated and exist in the standard model
        fn (int): False Negatives (FN) - edges, that are generated and don't exist in the standard model
    
    Returns: 
        float: the calculated recall represented as a float     
    """
    
    return tp / (tp + fn)

def calculate_precision(tp, fp):
    """
    Calculate the precision of the two models. It is computed as follows:
       Precision = TP / (TP + FP)

    Args:
        tp (int): True Positives (TP) - edges, that are generated and exist in the standard model
        fp (int): False Positives (FP) - edges, that are not generated and exist in the standard model 
    
    Returns: 
        float: the calculated recall represented as a float     
    """
    return tp / (tp + fp)

def calculate_node_matching_sim():
    return
