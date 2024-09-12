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

def LCS(X, Y):
  """
    Computes the Longest Common Subsequence (LCS) table for two strings.

    This function uses dynamic programming to build a table where L[j][k] represents
    the length of the LCS for the prefixes X[0:j] and Y[0:k].

    Args:
    X (str): The first input string.
    Y (str): The second input string.

    Returns:
    list of lists: A 2D table where L[j][k] is the length of the LCS for X[0:j] and Y[0:k].

    Time Complexity: O(nm), where n is the length of X and m is the length of Y.
    Space Complexity: O(nm) for the LCS table.
  """
  n, m = len(X), len(Y)                      # introduce convenient notations
  L = [[0] * (m+1) for k in range(n+1)]      # (n+1) x (m+1) table
  for j in range(n):
    for k in range(m):
      if X[j] == Y[k]:                       # align this match
        L[j+1][k+1] = L[j][k] + 1            
      else:                                  # choose to ignore one character
        L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
  return L

def LCS_solution(X, Y, L):
  """
    Reconstructs the Longest Common Subsequence (LCS) from the LCS table.

    This function backtracks through the LCS table to construct the actual
    longest common subsequence of X and Y.

    Args:
    X (str): The first input string.
    Y (str): The second input string.
    L (list of lists): The LCS table computed by the LCS function.

    Returns:
    str: The longest common subsequence of X and Y.

    Time Complexity: O(n + m), where n is the length of X and m is the length of Y.
    Space Complexity: O(n + m) in the worst case for the reconstructed subsequence.
  """
  solution = []
  j,k = len(X), len(Y)
  while L[j][k] > 0:                   # common characters remain
    if X[j-1] == Y[k-1]:
      solution.append(X[j-1])
      j -= 1
      k -= 1
    elif L[j-1][k] >= L[j][k-1]:
      j -=1
    else:
      k -= 1
  return ''.join(reversed(solution))   # return left-to-right version
