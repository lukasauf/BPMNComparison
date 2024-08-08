import argparse
import math
import markdown2
"""
This module provides functions to import BPMN models from .mmd files, 
parse command-line arguments, and prepare inputs for the BPMN process model comparator.

Functions:
    import_mmd_file(file_path):
        Read the content of a .mmd file and converts it to a string.
        Returns the parsed content or None if the file is not found.

    check_sum(values):
        Ensures that the sum of the provided weight values is approximately 1.0.
        Raises an argparse.ArgumentTypeError if the sum is not within the tolerance.

    parse_args():
        Parses command-line arguments required for the BPMN process model comparator.
        Validates that the weights for the similarity methods sum up to 1.
        Returns the parsed arguments.

    main():
        Main function to execute the parsing of command-line arguments and import BPMN models.
        Prepares and returns the inputs needed for running the comparator.
"""

def import_mmd_file(file_path):
    """
    Read the content of a .mmd file and convert it to a string.
     
    Args:
        file_path (str): File path of the provided BPMN model in .mmd format

    Returns:
        str: parsed string or None if the file is not found
    """
    try:
        # Open the .mmd file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse Markdown content using markdown2
        parsed_content = markdown2.markdown(content)
        
        return str(parsed_content)
    except FileNotFoundError:
        print("Error: File not found!")
        return None
    
def check_sum(values):
    """
    Ensures that the sum of the provided weight values for the low-level similarities is approximately 1.0

    Args:
        values (list): list of all three weight values (can be extended) to be examined

    Raises:
        argparse.ArgumentTypeError: If sum is not 1.0 raise error

    Returns:
        list: input list
    """
    values_sum = sum(values)
    target_sum = 1.0
    tolerance = 1e-6 

    if not math.isclose(values_sum, target_sum, abs_tol=tolerance):
        raise argparse.ArgumentTypeError(f"The sum of arguments glove_weight, bert_weight, and syntactic_weight must be approximately 1 (current sum: {values_sum})")
    return values

    
def parse_args():
    """
    Parses command-line arguments required for the BPMN process model comparator
    """
    
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
    """
    Main function to execute the parsing of command-line arguments and import BPMN models
    
    """
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