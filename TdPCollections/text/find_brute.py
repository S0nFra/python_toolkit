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

def find_brute(T, P):
  """
    Implements the brute-force string matching algorithm.

    This function searches for the first occurrence of pattern P within text T
    using a simple brute-force approach. It checks every possible starting position
    in T for a match with P.

    Args:
    T (str): The text string to search within.
    P (str): The pattern string to search for.

    Returns:
    int: The starting index of the first occurrence of P in T,
         or -1 if P is not found in T.

    Time Complexity: O(nm), where n is the length of T and m is the length of P.
    Space Complexity: O(1), as it uses only a constant amount of extra space.
  """
  n, m = len(T), len(P)                      # introduce convenient notations
  for i in range(n-m+1):                     # try every potential starting index within T
    k = 0                                    # an index into pattern P
    while k < m and T[i + k] == P[k]:        # kth character of P matches
      k += 1
    if k == m:                               # if we reached the end of pattern,
      return i                               # substring T[i:i+m] matches P
  return -1                                  # failed to find a match starting with any i
