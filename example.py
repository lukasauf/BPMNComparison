from main import run_node_matching
from main import run_edge_matching
from src.cli.cli import import_mmd_file
from src.BPMN.bpmn import BPMN

"""
An example procedure of both matching techniques for the automation tool with the support ticket models. 
These models are located in testing/example.
Here, only the syntactic similarity is applied as low-level measure, but the weights can be changed 
according to personal preferences.

Usage:
    Execute the script to run the support ticket example
"""

def main():
    #first load the support ticket example models (SM/GM) and store them in a string variable
    sm_model_str = import_mmd_file("testing/example/SM_Support_Ticket.mmd")
    gm_model_str = import_mmd_file("testing/example/GM_Support_Ticket.mmd")
    
    #parse the attributes of the BPMN models (events/tasks/gateways/edges)
    sm = BPMN(sm_model_str)
    gm = BPMN(gm_model_str)
    
    #determine threshold for text simialarity algorithm (in this case the opt. threshold for syntactic similarity)
    threshold = 0.47
    
    #weigh the 3 different low-level similarity metrics in a prefered way (here only syntactic is applied)
    weights = {
        'glove': 0, 
        'bert': 0, 
        'syntactic': 1 
        }
    
    #first run node matching algorithm 
    run_node_matching(sm, gm, weights, threshold)
    
    #then run edge matching
    run_edge_matching(sm, gm, weights, threshold)
    
if __name__ == "__main__":
    main()    