from main import run_node_matching
from src.cli.cli import import_mmd_file
from src.BPMN.bpmn import BPMN
import sys

"""
This script evaluates node matching in BPMN models using three different low-level approaches:
syntactic similarity, BERT-based similarity, and GloVe-based similarity.

The script sets specific weight configurations and thresholds for each approach and
runs a matching process to compare BPMN models.

Global Variables:
    weights_syntactic (dict): Weights configuration for syntactic similarity evaluation.
    weights_bert (dict): Weights configuration for BERT-based similarity evaluation.
    weights_glove (dict): Weights configuration for GloVe-based similarity evaluation.
    threshold_syntactic (float): Pre-determined optimal threshold for syntactic similarity.
    threshold_bert (float): Pre-determined optimal threshold for BERT-based similarity.
    threshold_glove (float): Pre-determined optimal threshold for GloVe-based similarity.

Functions:
    run_matching(weights, threshold):
        Runs the node matching for the PET dataset list of BPMN models using the specified weights
        and threshold.

    run_nm_evaluation():
        Evaluates node matching using all three similarity approaches (syntactic, BERT, GloVe).
"""


#set weights variables for evaluating all three low-level approaches
weights_syntactic = {'syntactic': 1, 'bert': 0, 'glove': 0}
weights_bert = {'syntactic': 0, 'bert': 1, 'glove': 0}
weights_glove = {'syntactic': 0, 'bert': 0, 'glove': 1}

#set determined optimal thresholds (see threshold_determination.py)
threshold_syntactic = 0.47
threshold_bert = 0.74
threshold_glove = 0.71


def run_matching(weights, threshold):
    """
    Runs the node matching for the PET dataset list of BPMN models using the specified weights
    and threshold.

    Args:
        weights (dict): A dictionary specifying the weights for the similarity approach.
        threshold (float): The threshold value to be used in the matching process.
    """
    
    models = ["10_13.mmd", "10_6.mmd", "10_1.mmd", "5_2.mmd", "3_3.mmd", "1_3.mmd", "1_2.mmd"]
    
    for model in models:
        path_sm = "testing/pet/SM/" + model
        path_gm = "testing/pet/GM/" + model
        sm_model_str = import_mmd_file(path_sm)
        gm_model_str = import_mmd_file(path_gm)
        sm = BPMN(sm_model_str)
        gm = BPMN(gm_model_str)
        print(f'Model: {model}')
        run_node_matching(sm, gm, weights, threshold)
        print('++++++++++++++++++++++++++\n')

    
def run_nm_evaluation():
    input_user = input("Choose the low-level similarity algorithm for the evaluation of the PET data set: \n S for Syntactic \n B for BERT \n G for GloVe\n")
    if input_user == 'S':
        print('\n\033[1mEvaluation of node matching with syntactic similarity\033[0m\n')
        run_matching(weights_syntactic, threshold_syntactic)
    elif input_user == 'B':
        print('\n\033[1mEvaluation of node matching with BERT similarity\033[0m\n')
        run_matching(weights_bert, threshold_bert)
    elif input_user == 'G':
        print('\n\033[1mEvaluation of node matching with GloVe similarity\n\033[0m')
        run_matching(weights_glove, threshold_glove) 
    else:
        print(f'Wrong input \"{input_user}\" but expected to be \"S\" or \"B\" or \"G\"')
        sys.exit(1) 
    
if __name__ == "__main__":
    run_nm_evaluation()    