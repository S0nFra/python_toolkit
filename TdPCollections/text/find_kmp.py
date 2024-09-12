# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def find_kmp(T, P):
  """
    Implements the Knuth-Morris-Pratt (KMP) string matching algorithm.

    This function efficiently searches for the first occurrence of pattern P within text T
    using the KMP algorithm. It utilizes a failure function to skip unnecessary comparisons.

    Args:
    T (str): The text string to search within.
    P (str): The pattern string to search for.

    Returns:
    int: The starting index of the first occurrence of P in T,
         or -1 if P is not found in T.

    Time Complexity: O(n + m), where n is the length of T and m is the length of P.
    Space Complexity: O(m) for the failure function.
  """
  n, m = len(T), len(P)            # introduce convenient notations
  if m == 0: return 0              # trivial search for empty string
  fail = compute_kmp_fail(P)       # rely on utility to precompute
  j = 0                            # index into text
  k = 0                            # index into pattern
  while j < n:
    if T[j] == P[k]:               # P[0:1+k] matched thus far
      if k == m - 1:               # match is complete
        return j - m + 1           
      j += 1                       # try to extend match
      k += 1
    elif k > 0:                    
      k = fail[k-1]                # reuse suffix of P[0:k]
    else:
      j += 1
  return -1                        # reached end without match

def compute_kmp_fail(P):
  """
    Computes the failure function for the KMP algorithm.

    This function pre-processes the pattern P to create a failure function,
    which is used to determine how much to shift the pattern when a mismatch occurs.

    Args:
    P (str): The pattern string to compute the failure function for.

    Returns:
    list: A list representing the failure function for P.

    Time Complexity: O(m), where m is the length of P.
    Space Complexity: O(m) for the failure function.

    Note: This is an internal utility function used by find_kmp.
  """
  m = len(P)
  fail = [0] * m                   # by default, presume overlap of 0 everywhere
  j = 1
  k = 0
  while j < m:                     # compute f(j) during this pass, if nonzero
    if P[j] == P[k]:               # k + 1 characters match thus far
      fail[j] = k + 1
      j += 1
      k += 1
    elif k > 0:                    # k follows a matching prefix
      k = fail[k-1]
    else:                          # no match found starting at j
      j += 1
  return fail
