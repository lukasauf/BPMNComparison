from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.util.helpers import check_index_access


def compute_bert_similarity(tuple):
    """Compute cosine similarity of one element of the Standard Model (SM) with all the elements of the Generated Model (GM).

    Args:
        tuple (list): tuple[0] is the single element of the SM to be compared with tuple[1:], the elements of GM

    Returns:
        list: List containing similarity scores for all the comparisons
    """
    
    # Initializing the Sentence Transformer model using BERT with mean-tokens pooling
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    #print('COMPARING EVERY EDGE OF SM WITH ALL list_edges IN GM \nContent is:')
    #print(tuple)
        
    sentence_embeddings = model.encode(tuple)
    
    check_index_access(sentence_embeddings, 0)
    # Calculating the cosine similarity between one sm and all gm parts of one side of the tuple
    similarity_scores = cosine_similarity([sentence_embeddings[0]], sentence_embeddings[1:])
    check_index_access(similarity_scores, 0)
    #print(f'BERT Similarity scores are:{similarity_scores[0]}')
    return similarity_scores[0].tolist()
    
    