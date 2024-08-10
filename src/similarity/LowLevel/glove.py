
import os
import gensim.downloader as api
from nltk.tokenize import word_tokenize
from scipy.spatial.distance import cosine
from gensim.models import KeyedVectors
from src.similarity.LowLevel.syntactic import compute_syntactic_similarity
from src.util.helpers import check_index_access
# Define the model path
model_path = 'glove-wiki-gigaword-300'

if os.path.exists(model_path):
    # Load the model from disk
    print("Loading model from disk...")
    model = KeyedVectors.load(model_path)
else:
    # Download and save the model
    print("Downloading model...")
    model = api.load('glove-wiki-gigaword-300')
    print("Saving model to disk...")
    model.save(model_path)


def compute_glove_similarity(sm_element, gm_elements):
    """
    Compute the glove similarity between a SM text element and all the elements of GM.


    Args:
        sm_element (str): The text element for which the similarity is to be computed.
        gm_elements (list of str): A list of text elements to compare against `sm_element`.

    Returns:
        list of float: A list of similarity scores, one for each element in `gm_elements`.
    """
    similarities = []
    #print('****************************\n')
    #print(f'SM_element is {sm_element} and GM_elements are {gm_elements}')
    for gm_element in gm_elements:
        similarity = glove_similarity(sm_element, gm_element)
        # threshold must be added
        similarities.append(similarity)
    #print(f'Similarities are {similarities}')
    #print('****************************\n')
    return similarities
    
# Function to compute similarity between two BPMN elements
def glove_similarity(sm_element, gm_element):
    sm_element = word_tokenize(sm_element.lower())
    #print(f'TYPE OF GM_ELEMENT IS {type(gm_element)}')
    gm_element = word_tokenize(gm_element.lower())
    sm_vectors = [model[word] for word in sm_element if word in model]
    gm_vectors = [model[word] for word in gm_element if word in model]

    #if there are no synonyms for the words calculate the syntactic similarity (happens for e.g. "startevent")
    if not sm_vectors or not gm_vectors:
        similarities = compute_syntactic_similarity(sm_element, [gm_element])
        check_index_access(similarities, 0)
        return similarities[0]

    avg_sm_vector = sum(sm_vectors) / len(sm_vectors)
    avg_gm_vector = sum(gm_vectors) / len(gm_vectors)
    similarity = 1 - cosine(avg_sm_vector, avg_gm_vector)
    return similarity
