# main.py
from src.cli.cli import main as frontend_main
from src.BPMN.bpmn import BPMN
from src.evaluation.metrics import calculate_jaccard_index, calculate_recall, calculate_precision
from src.similarity.HighLevel.EdgeMatching import compare_models_em
from src.similarity.HighLevel.NodeMatching import compare_models_nm
import sys

"""
Main entry point for the automation tool. 

Functions:
    run_node_matching(sm, gm, weights, threshold):
        Compares nodes of Standard Model (SM) and Generated Model (GM) using given weights and threshold.
        Computes and prints the optimal equivalence mapping, recall, precision, and Jaccard index.

    run_edge_matching(sm, gm, weights, threshold):
        Compares edges of Standard Model (SM) and Generated Model (GM) using given weights and threshold.
        Computes and prints the optimal equivalence mapping, recall, precision, and Jaccard index.

    run():
        Main function to execute the appropriate matching algorithm (node or edge) based on the version specified.
        Parses input, initializes BPMN models, and calls the corresponding matching function.

Usage:
    Execute the script to run the matching algorithm with provided inputs (run 'python main.py --help' for further information).

"""


def run_node_matching(sm, gm, weights, threshold):
    opt_eq_map = compare_models_nm(sm, gm, weights, threshold)
    tp = len(opt_eq_map)
    fp = len(sm.tasks) - tp
    fn = len(gm.tasks) - tp
    
    jaccard_index = calculate_jaccard_index(tp, fp, fn)
    recall = calculate_recall(tp, fn)
    precision = calculate_precision(tp, fp)
    print('**************Node matching results:**********\n')
    print(f'tasks in SM: {len(sm.tasks)}')
    print(f'Found: {tp}')
    print(f'Additional: {fn}')
    print(f'tasks in GM: {len(gm.tasks)}\n')
    
    
    print(f"Recall: {recall}")
    print(f"Precision: {precision}")
    print(f"Jaccard Index: {jaccard_index}\n")
    print(f'Optimal equivalence mapping is {opt_eq_map}')

def run_edge_matching(sm, gm, weights, threshold):  
    opt_eq_map = compare_models_em(sm, gm, weights, threshold)
    # Calculate metrics
    tp = len(opt_eq_map)
    fp = len(sm.edges) - tp
    fn = len(gm.edges) - tp
    jaccard_index = calculate_jaccard_index(tp, fp, fn)
    recall = calculate_recall(tp, fn)
    precision = calculate_precision(tp, fp)
    print('**************Edge matching results:**********\n')
    print(f'edges in SM: {len(sm.edges)}')
    print(f'Found: {tp}')
    print(f'Additional: {fn}')
    print(f'edges in GM: {len(gm.edges)}\n')
    
    
    print(f"Recall: {recall}")
    print(f"Precision: {precision}")
    print(f"Jaccard Index: {jaccard_index}\n")  
    print(f'Optimal Eq. Mapping is {opt_eq_map}')



def run():
    sm_model_str, gm_model_str, version, weights, threshold = frontend_main()
    version = int(version)
    sm = BPMN(sm_model_str)
    #print(f'SM tasks are {sm.tasks}')
    gm = BPMN(gm_model_str)
    #print(f'GM tasks are {gm.tasks}')


    '''
    determine_threshold(sm, gm, weights, threshold, version)
    '''
    if version == 1:
        run_node_matching(sm, gm, weights, threshold)
    elif version == 2: 
        run_edge_matching(sm, gm, weights, threshold)
    else:
        print(f'Error: version is not valid. Should be 1 or 2 but is {version}')      
        sys.exit(1)  
    
    
    
    
if __name__ == "__main__":
    run()
