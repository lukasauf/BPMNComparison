from src.util.helpers import check_index_access

class BPMN:
    """
    Stores all relevant information for BPMN (Business Process Model and Notation) models.

    Attributes:
        bpmn_str (str): The BPMN model string. (adheres to the conventional guideline)
        events (dict): A dictionary storing keys and their corresponding values for events.
        tasks (dict): A dictionary storing keys and their corresponding values for tasks.
        gateways (dict): A dictionary storing keys and their corresponding values for gateways.
        edges (list): A list of lists where each list represents an edge in the BPMN model.
                        Each tuple contains the key_parent, key_child.
                        Let a --> b be an edge, then a is the parent and b is the child
    """

    def __init__(self, bpmn_str):
        """
        Initializes the BPMNParser with a BPMN model string.

        Args:
            bpmn_str (str): The BPMN model string.
        """
        self.__bpmn_str = bpmn_str
        self.events = {}
        self.tasks = {}
        self.gateways = {}
        self.edges = []
        self.__parse()
        
    
    

    def __determine_event_task_gateway(self, key, value):
        """
        Determines whether a key is an event, task, or gateway and adds it to the corresponding dictionary if not already present.

        Args:
            key (str): The key to determine.
            value (str): The value associated with the key.
        """
        if 'event' in key and key not in self.events:
            self.events[key] = value
        #edge case --> if the task is initially introduced as "" and after that the actual tag is mentioned (like in 1_2 10:task:)    
        elif 'task' in key and (key not in self.tasks or self.tasks[key] == ''):
            self.tasks[key] = value
        elif 'gateway' in key and key not in self.gateways:
            self.gateways[key] = value
        return

    def __extract_key_value(self, edge):
        """
        Extracts the key and value from a single edge string by means of seperating symbols

        Args:
            edge (str): The string to extract the key and value from.

        Returns:
            tuple: A tuple containing the key and value.
        """
        key = ''
        value = ''
        isKeys = True
        isCondition = False

        for i, c in enumerate(edge):
            if c == '|' and not isCondition:
                isCondition = True
            elif isCondition:
                if c == '|':
                    isCondition = False
            else:
                if c == '<':
                    break
                if isKeys:
                    key += c
                    if i + 1 < len(edge):
                        if edge[i + 1] == '(' or edge[i + 1] == '{':
                            isKeys = False
                else:
                    if c != '{' and c != '}' and c != '(' and c != ')':
                        value += c

        return key, value

    def __parse(self):
        """
        Parses the BPMN model string and populates the class variables.
        """
        edges_input = self.__bpmn_str.split('\n')
        splitter = '-->'

        for i, edge in enumerate(edges_input):
            if i == 0 or i == len(edges_input) - 1:
                continue

            child_parent_edge = edge.split(splitter)

            check_index_access(child_parent_edge, 0)
            check_index_access(child_parent_edge, 1)
            parent = child_parent_edge[0].strip()
            child = child_parent_edge[1].strip()

            key_parent, value_parent = self.__extract_key_value(parent)
            key_child, value_child = self.__extract_key_value(child)
            key_parent = key_parent.strip()
            key_child = key_child.strip()
            self.edges.append([key_parent, key_child])

            self.__determine_event_task_gateway(key_parent, value_parent)
            self.__determine_event_task_gateway(key_child, value_child)

        return 

