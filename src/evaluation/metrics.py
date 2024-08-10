from src.util.helpers import check_index_access
import sys 

"""
This module provides functions to calculate key evaluation metrics for comparing models, 
specifically focusing on the Jaccard Index, recall, and precision.

Functions:
    - calculate_jaccard_index(tp, fp, fn): 
        Calculates the Jaccard Index, which measures the similarity between two models by 
        comparing the true positives, false positives, and false negatives.
    
    - calculate_recall(tp, fn): 
        Calculates the recall, which measures the ability of a model to identify all relevant instances (true positives)
        compared to the total relevant instances in the standard model.
    
    - calculate_precision(tp, fp): 
        Calculates the precision, which measures the accuracy of the positive predictions made by the model in comparison to the standard model.
"""
                       
            

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


