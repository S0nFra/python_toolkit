import numpy as np
import argparse

def BoyerMoore(T, P):
    """
    Implementation of the Boyer-Moore string search algorithm.
    
    Args:
    T (str): Text in which to search.
    P (str): Pattern to search for.
    
    Returns:
    int: The starting index of the first occurrence of P in T, or -1 if P is not found.
    """
    n, m = len(T), len(P)
    if m == 0: return 0  # If pattern is empty, it's found at the start.

    # Create the last occurrence table for the pattern.
    last_occurance = dict()
    for k in range(m):
        last_occurance[P[k]] = k

    i = m - 1  # Pointer in the text.
    k = m - 1  # Pointer in the pattern.
    while i < n:
        if T[i] == P[k]:  # Characters match.
            if k == 0:
                return i  # Found the pattern.
            else:
                i -= 1
                k -= 1
        else:
            j = last_occurance.get(T[i], -1)  # Last occurrence of T[i] in the pattern.
            i = i + m - min(k, j + 1)  # Shift the pattern.
            k = m - 1  # Reset pattern pointer.
    return -1  # Pattern not found.

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

def _test(conf={"del_cost": 1, "ins_cost": 1, "sub_cost": 1}):
    """
    Runs a series of tests to verify the implementation of the Levenshtein distance function.
    
    Args:
    conf (dict): Configuration for deletion, insertion, and substitution costs.
    """
    print("conf:", conf)
    
    print(">>> FIRST TEST SET <<<")
    A = ["helo", "algorithm", "kitten", "gate", "winter", "INTENTION", "pero", "paolo", "casa", "Channel1", "Stanby"]
    B = ["hello", "rhythm", "sitting", "goat", "writers", "EXECUTION", "melo", "parlo", "cassa", "CH1", "STBY"]
    res = []
    
    for i in range(len(A)):
        edit_dist, _ = levenshtein_dist(A[i], B[i], **conf)
        print("Levenshtein Distance between \"{}\" and \"{}\" = {}".format(A[i], B[i], edit_dist))
        res.append(edit_dist)
    print(res, "\n")
    
    print(">>> SECOND TEST SET <<<")
    tests = [
        ("winter", "writers", 3),
        ("INTENTION", "EXECUTION", 5),
        ("paolo", "parlo", 1),
        ("casa", "cassa", 1),
        ("pero", "melo", 2)
    ]
    
    for test in tests:
        src, trg, res = test
        pred, _ = levenshtein_dist(src, trg, **conf)
        assert pred == res, f"src:\"{src}\" trg:\"{trg}\" expected {res} obtained {pred}"
    
    print(">>> TEST END <<<")

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
