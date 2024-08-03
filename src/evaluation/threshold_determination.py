#from backend.similarity.HighLevel.Matching import compare_models
from src.evaluation.metrics import calculate_tp_fp_fn, calculate_jaccard_index, calculate_recall, calculate_precision, calculate_node_matching_sim
import copy

def determine_threshold(sm, gm, weights, threshol, version):
    thresholds = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    sm_unchanged = copy.deepcopy(sm)
    gm_unchanged = copy.deepcopy(gm)
    for threshold in thresholds:
        sm = copy.deepcopy(sm_unchanged)
        gm = copy.deepcopy(gm_unchanged)
        #compare_models(sm, gm, weights, threshold, version)
        print('++++++++++++++++++++++++++++++++++++')
        print(f'For threshold {threshold} results are:')
        tp, fp , fn = calculate_tp_fp_fn(sm.edges, gm.edges)
        jaccard_index = calculate_jaccard_index(tp, fp, fn)
        recall = calculate_recall(tp, fn)
        precision = calculate_precision(tp, fp)
        print('**************FINAL DATA**********\n')
        print(f'tuples in SM: {len(sm.edges)}')
        print(f'TP: {tp}')
        print(f'FN: {fn}')
        print(f'tuples in GM: {len(gm.edges)}\n')
        
        
        print(f"Recall: {recall}")
        print(f"Precision: {precision}")
        print(f"Jaccard Index: {jaccard_index}\n")