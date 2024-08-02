import argparse
from frontend.bpmn_loader import import_mmd_file
import math

def check_sum(values):
    values_sum = sum(values)
    target_sum = 1.0
    tolerance = 1e-6 

    if not math.isclose(values_sum, target_sum, abs_tol=tolerance):
        raise argparse.ArgumentTypeError(f"The sum of arguments glove_weight, bert_weight, and syntactic_weight must be approximately 1 (current sum: {values_sum})")
    return values

def parse_args():
    parser = argparse.ArgumentParser(description="BPMN Process Model Comparator")
    parser.add_argument('--file_sm', required=True, help="Path to the standard model BPMN .mmd file")
    parser.add_argument('--file_gm', required=True, help="Path to the generated model BPMN .mmd file")
    parser.add_argument('--version', choices=['1', '2'], default='1', help="Choose the matching algorithm (Node matching --> 1, Edge Matching -->2). Defaults to 1.")
    parser.add_argument('--syntactic_weight', type=float, required=True, help="Weight for the low level similarity method \"syntactic\". All weights should add up to 1.")
    parser.add_argument('--bert_weight', type=float, required=True, help="Weight for the low level similarity method \"BERT\". All weights should add up to 1.")
    parser.add_argument('--glove_weight', type=float, required=True, help="Weight for the low level similarity method \"GloVe\". All weights should add up to 1.")
    parser.add_argument('--threshold', type=float, default=0.7, help="Threshold for accepting the similarity value (defaults to 0.7): if similarity(elem1, elem2) > threshold --> elem1 and elem2 are considered equal")
    args = parser.parse_args()

    # Validate the sum constraint
    try:
        args.glove_weight, args.bert_weight, args.syntactic_weight = check_sum([args.glove_weight, args.bert_weight, args.syntactic_weight])
    except argparse.ArgumentTypeError as e:
        parser.error(str(e))  # Print error message and exit
    
    return args

def main():
    args = parse_args()
    sm_model = import_mmd_file(args.file_sm)
    gm_model = import_mmd_file(args.file_gm)
    
    weights = {
        'glove': args.glove_weight, 
        'bert': args.bert_weight, 
        'syntactic': args.syntactic_weight 
        }
    #print(f'SM Model is: {sm_model}')
    return sm_model, gm_model, args.version, weights, args.threshold


if __name__ == "__main__":
    main()