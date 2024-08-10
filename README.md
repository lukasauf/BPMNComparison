# BPMNComparison
Automate_BPMN_Comparison is a tool for comparing two BPMN models automatically. Usually the models to be compared are the **Standard Model (SM)** created by a human process modeler and the **Generated Model (GM)** generated by an AI tool. The resulting comparison is based on several **similarity metrics (recall, precision, Jaccard index)**.


<h1> Evaluation Data Set [testing/] </h1>

[Pet Data Set](https://huggingface.co/datasets/patriziobellan/PET) </br>
* **testing/pet/process\_descriptions**: textual descriptions for 7 selected examples from PET data set
* **testing/pet/xml**: the models in BPMN2.0 format with process descriptions (TODO)
* **testing/pet/GM**: the 7 generated models stored in .mmd files
* **testing/pet/SM**: the 7 standard models stored in .mmd files
* **testing/pet/example_manual_evaluation.xlsx**: the manual evaluation of the 7 pairs of models

Support Ticket Example <\br>
* **testing/example**: two BPMN models stored in .mmd files about a support ticket procedure 
  

<h1> Virtual Environment </h1>

* **Pipfile, Pipfile.lock**: virtual environment

<h1> Execution </h1>

1. clone the repo
   - `git clone <repo_name>`
2. navigate to the Automate_BPMN_Comparison directory
3. create virtual environment
   - `pipenv install`
4. install all required libraries
   - `pipenv install -r requirements.txt`
5. start the environment
    - `pipenv shell`
6. execute python script
    - `python main.py [args]` or `pipenv run python main.py [args]` (step 5 can be skipped here)
    - to execute `python main.py` in the virtual environment, you need to add some arguments (run `python main.py --help` for further usage information)
    - to simulate the determination of the threshold for all 3 text similarity algorithm, execute `python threshold_determination.py`
    - to simulate the evaluation of the 7 selected examples from the [Pet Data Set](https://huggingface.co/datasets/patriziobellan/PET) invoke `python node_matching_evaluation.py`
      or `python edge_matching_evaluation.py`
   
 



