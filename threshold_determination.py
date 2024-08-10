from main import run_edge_matching
from src.cli.cli import import_mmd_file
from src.BPMN.bpmn import BPMN
import sys

"""
This script evaluates and determines the optimal threshold for edge matching in BPMN models (this threshold will also be used for node matching)
using three different low-level similarity approaches: syntactic, BERT-based, and GloVe-based similarity.

Global Variables:
    weights_syntactic (dict): Weights configuration for evaluating syntactic similarity.
    weights_bert (dict): Weights configuration for evaluating BERT-based similarity.
    weights_glove (dict): Weights configuration for evaluating GloVe-based similarity.

Functions:
    determine_threshold(weights):
        Evaluates a range of thresholds for edge matching in BPMN models using the specified 
        similarity approach

    
    run_tresholds():
        Prompts the user to select one of the three low-level similarity algorithms (syntactic, 
        BERT, GloVe) to evaluate and determine the optimal threshold.
"""

#set weights variables for evaluating all three low-level approaches
weights_syntactic = {'syntactic': 1, 'bert': 0, 'glove': 0}
weights_bert = {'syntactic': 0, 'bert': 1, 'glove': 0}
weights_glove = {'syntactic': 0, 'bert': 0, 'glove': 1}

def determine_threshold(weights):
    """
    Evaluates a range of thresholds for edge matching in BPMN models using the specified 
    similarity approach

    Args:
        weights (dict): A dictionary specifying the weights for the similarity approach 
                        (syntactic, BERT, or GloVe).
    """
    thresholds = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    models = ["10_13.mmd", "10_6.mmd", "10_1.mmd", "5_2.mmd", "3_3.mmd", "1_3.mmd", "1_2.mmd"]
    
    for model in models:
        path_sm = "testing/pet/SM/" + model
        path_gm = "testing/pet/GM/" + model
        sm_model_str = import_mmd_file(path_sm)
        gm_model_str = import_mmd_file(path_gm)
        sm = BPMN(sm_model_str)
        gm = BPMN(gm_model_str)
        print(f'\033[1mModel: {model}\033[0m')
        for threshold in thresholds:
            print(f'For threshold = {threshold} results are:')
            run_edge_matching(sm, gm, weights, threshold)
            print('\n')
            
            
        

def run_tresholds():
    """
    Run threshold determination:
    Prompts the user to select one of the three low-level similarity algorithms (syntactic, 
    BERT, GloVe) to evaluate and determine the optimal threshold.
    """
    input_user = input("Choose the low-level similarity algorithm for the optimal threshold: \n S for Syntactic \n B for BERT \n G for GloVe\n")
    if input_user == 'S':
        determine_threshold(weights_syntactic)
    elif input_user == 'B':
        determine_threshold(weights_bert)
    elif input_user == 'G':
        determine_threshold(weights_glove)
    else:
        print(f'Wrong input \"{input_user}\" but expected to be \"S\" or \"B\" or \"G\"')
        sys.exit(1)
                    
if __name__ == "__main__":
    run_tresholds()
            