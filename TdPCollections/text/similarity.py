import numpy as np
import argparse

def levenshtein_dist(src: str, trg: str, del_cost=1, ins_cost=1, sub_cost=2, pre_process=str.lower):
    """
    Computes the Levenshtein distance between two strings.
    
    Args:
    src (str): Source string.
    trg (str): Target string.
    del_cost (int): Cost of deletions.
    ins_cost (int): Cost of insertions.
    sub_cost (int): Cost of substitutions.
    pre_process (function): Function to preprocess the strings (default is to lower case the strings).
    
    Returns:
    tuple: A tuple containing the edit distance and the distance matrix.
    """
    src = pre_process(src)
    trg = pre_process(trg)

    src_len, trg_len = len(src), len(trg)
    dist_matrix = np.zeros((src_len + 1, trg_len + 1), dtype=np.int16)
    
    # Fill in the cost for deletions
    for i in range(1, src_len + 1):
        dist_matrix[i][0] = i * del_cost
    
    # Fill in the cost for insertions
    for j in range(1, trg_len + 1):
        dist_matrix[0][j] = j * ins_cost
    
    # Compute the distance matrix
    for i in range(1, src_len + 1):
        for j in range(1, trg_len + 1):
            effective_sub_cost = 0 if src[i - 1] == trg[j - 1] else sub_cost

            dist_matrix[i][j] = min(
                dist_matrix[i - 1][j] + ins_cost,             # insertion
                dist_matrix[i][j - 1] + del_cost,             # deletion
                dist_matrix[i - 1][j - 1] + effective_sub_cost  # replacement
            )
            
    edit_dist = dist_matrix[src_len][trg_len]
    
    return edit_dist, dist_matrix

def similarity(str1, str2, *args, **kargs):
    """
    Computes the similarity score between two strings based on Levenshtein distance.
    
    Args:
    str1 (str): First string.
    str2 (str): Second string.
    
    Returns:
    tuple: A tuple containing the similarity score between 0 and 1, and the edit distance.
    """
    dist, _ = levenshtein_dist(str1, str2, *args, **kargs)
    max_length = max(len(str1), len(str2))
    return 1.0 - (dist / max_length), dist

def smart_search(s, target, th=0.3):
    """
    Searches for strings in a list that are similar to a target string.
    
    Args:
    s (list): List of strings to search within.
    target (str): Target string to compare against.
    th (float): Similarity threshold.
    
    Prints:
    Similarity score and string if the score is above the threshold.
    """
    for e in s:
        res = similarity(e, target)
        if res[0] >= th:
            print(f"{res[0]:.3f}", ":", e)
            
if __name__ == '__main__':
    def get_param() -> argparse.Namespace:
        """
        Parses command-line arguments.
        
        Returns:
        argparse.Namespace: Namespace with the parsed arguments.
        """
        parser = argparse.ArgumentParser(
            prog="String similarity",
            description="Calculate the percentage of similarity between two strings using the Levenshtein edit-distance."
        )
        
        parser.add_argument('string1')
        parser.add_argument('string2')
        parser.add_argument('del_cost', type=int, default=1)
        parser.add_argument('ins_cost', type=int, default=1)
        parser.add_argument('sub_cost', type=int, default=1)
        parser
