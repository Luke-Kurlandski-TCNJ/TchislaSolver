"""
Luke Kurlandski
Tchisla Solver Back-End
Spring 2020
"""

import math
import time
from itertools import product, combinations_with_replacement

from errors import NumberError, TargetFound

class Operation:
    """
    Contains functions for computing results of mathematical operations Tchisla uses.
    
    Should have been in separte file, but R was making importation of files tricky.
    """
    
    def __init__(self, use, targets, max_fact, max_pow, max_rec, too_big):
        
        # Numbers to search for and number to use.
        self.USE = use
        self.TARGETS = targets
        
        	# Prevent program breaking due to large numbers.
        self.MAX_FACT = int(max_fact) #20000
        self.MAX_POW = int(max_pow) #140*140
        self.MAX_REC = int(max_rec) #10000
        self.TOO_BIG = pow(10, too_big) #10^24
        
        # Store the permitted operations in a list.
        self.uniary_ops = [self.factorial, self.negation, self.root]
        self.binary_ops = [self.addition, self.subtraction, self.multiplication, 
                      self.division, self.exponentiation]

    def factorial(self, n):
        """
        Compute and return the factorial of n, raise NumberError as needed.
        """
        
        if n > self.MAX_FACT or n < 3:
            raise NumberError
        r = math.factorial(n)
        if r > self.TOO_BIG:
            raise NumberError
        return int(r)
    
    def negation(self, n):
        """
        Compute and return the negation of n, raise NumberError as needed.
        """
        
        r = -1 * n
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG):
            raise NumberError
        return int(r)
    
    def root(self, n):
        """
        Compute and return the negation of n, raise NumberError as needed.
        """
        
        if  n < 2:
            raise NumberError
        r = math.sqrt(n)
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG) or not r.is_integer():
            raise NumberError
        return int(r)
    
    def addition(self, n, m):
        """
        Compute and return the sum of n and m, raise NumberError as needed.
        """
        
        r = m + n
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG):
            raise NumberError
        return int(r)
    
    def subtraction(self, n, m):
        """
        Compute and return the difference of n and m, raise NumberError as needed.
        """
        
        r = n - m
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG):
            raise NumberError
        return int(r)
    
    def multiplication(self, n, m):
        """
        Compute and return the product of n and m, raise NumberError as needed.
        """
        
        r = m * n
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG):
            raise NumberError
        return int(r)
    
    def division(self, n, m):
        """
        Compute and return the quotient of n and m, raise NumberError as needed.
        """
    
        if m == 0:
            raise NumberError
        r = n / m
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG) or not r.is_integer():
            raise NumberError
        return int(r)
    
    def exponentiation(self, n, m):
        """
        Compute and return n to the power of m, raise NumberError as needed.
        """
        
        if n * m > self.MAX_POW:
            raise NumberError
        r = math.pow(n, m)
        if r > self.TOO_BIG or r < (-1*self.TOO_BIG) or not r.is_integer():
            raise NumberError
        return int(r)
    
    def symbol(self, name):
        """
        Return the appropriate mathematical symbol for a function name.
        """
    
        if name == "factorial":
            return "!"
        if name == "root":
            return "sq"
        if name == "negation":
            return "-"
        if name == "addition":
            return "+"
        if name == "subtraction":
            return "-"
        if name == "multiplication":
            return "*"
        if name == "division":
            return "/"
        if name == "exponentiation":
            return "^"

def nice_print(nums, m:Operation):
    """
    Neatly print a dictionary of result:path pairs for testing purposes. 
    """
    
    for i in range(1, len(nums)):
        print("\nUsed " + str(m.USE) + ", " + str(i) + " times:\n")
        for res in sorted(nums[i].keys()):
            print(int(res), "=", nums[i][res])
            
def total_report(nums, m:Operation):
    """
    Print a report of all numbers generated for testing purposes.
    """
    
    print("\nTotal Report:")
    for i in nums:
        print("Numbers Produced With " + str(i) + ", " + str(m.USE) + "s:", len(nums[i].keys()))
    print()
    
def sort_tuple(tup_list):
    """
    Sort the list of tuples produced in calculate method.
    """
    
    tup_list.sort(key = lambda x: x[0])  
    return tup_list 
        
def check_target(n, path, m:Operation):
    """
    Check if the target is found and print result.
    
    Arguments:
        n : int : number to check if equal to target
        path : str : operations taken to arrive at n
    """
    
    for i in m.TARGETS:
        if n == i:
            m.TARGETS.remove(n)
            raise TargetFound(i, path, path.count(str(m.USE)))
        
def subset_sum(numbers, target):
    """
    Calculate the pairs of numbers that sum to a given target.
    """
    
    pairs = []
    for i in list(combinations_with_replacement(numbers, 2)):
        s = sum(i)
        if s == target:
            pairs.append(i)
    return pairs

def calculate_uniary(n, x_uses, path, m:Operation, rdepth=1):
    """
    Fill x_uses with the results of using uniary operators on the number n.
    
    Arguments:
        n : int : integer to use
        x_uses : dict : results that requires x uses of USE
        path : str : path taken to calculate a result
        rdepth : int :  recursive depth of the function
    """
    
    retVal = []

    # Perform each single operator on n.
    for op in m.uniary_ops:
        # Avoid a recursion error
        if rdepth > m.MAX_REC:
            return
        # Avoid repetative switching sign.
        if op.__name__ == "neg" and len(path) > 1 and path[1] == "-":
            continue 
        # Calculate the result and perform recursion on result.
        sym = m.symbol(op.__name__)
        try:
            res = op(n)
            if res not in x_uses:
                # Place minus sign/sqr in front, factorial behind
                x_uses[res] = "(" + path + sym + ")" if sym == "!" else "(" + sym + path + ")"
                discovered = calculate_uniary(res, x_uses, x_uses[res], m, rdepth+1)
                if discovered:
                    retVal.extend(discovered)
                try:
                    check_target(res, x_uses[res], m)
                except TargetFound as e:
                    retVal.append((e.target, e.path, e.uses))

        except NumberError:
            continue

    # If retVal is empty, return None.
    if retVal:
        return retVal
    else:
        return None

def perform_uniary_operations(x_uses, m):
    """
    Perform all uniary operations on every number in x_uses.
    
    Arguments:
        x_uses : dict : results that requires x uses of USE
    """

    retVal = []

    for n in list(x_uses):
        discovered = calculate_uniary(n, x_uses, x_uses[n], m)
        if discovered is not None:
            retVal.extend(discovered)

    # If retVal is empty, return None.
    if retVal:
        return retVal
    else:
        return None

def calculate_nthles(nums_pairs, x_uses, m:Operation):
    """
    Fill x_uses with results taking x operations by performing operations with
        the values from nums_pairs.

    Arguments:
        nums_pairs : list[tuples[dict]]] : pairs of y_uses and z_uses dicts to 
            combine with binary operators
        x_uses : dict : results that requires x uses of USE to fill
    """

    retVal = []

    # Cycle through the list of tuples.
    for p in nums_pairs:
        # Isolate each dictionary.
        nums1 = p[0]
        nums2 = p[1]
        # Cartesian product list of every combination of the two lists.
        cartesian_combos = list(product(nums1.keys(), nums2.keys()))
        # The first element of combo will be from nums1, second from nums2.
        for combo in cartesian_combos:
            # Isolate the two numbers in the combo.
            num1 = combo[0]
            num2 = combo[1]
            # Perform every double op available between the numbers.
            for op in m.binary_ops:
                # Get the operation symbol and paths for each num.
                sym = m.symbol(op.__name__)
                path1 = nums1[num1]
                path2 = nums2[num2]
                # Calculate and add num1 op num2 to the dict.
                try:
                    res = op(num1, num2)
                    if res not in x_uses: 
                        x_uses[res] = "(" + path1 + sym + path2 + ")"
                    try:
                        check_target(res, x_uses[res], m)
                    except TargetFound as e:
                        retVal.append((e.target, e.path, e.uses))
                except (OverflowError, ValueError, NumberError):
                    pass
                # Calculate and add num2 op num1 to the dict.
                try:
                    res = op(num2, num1)
                    if res not in x_uses: 
                        x_uses[res] = "(" + path2 + sym + path1 + ")"
                        try:
                            check_target(res, x_uses[res], m)
                        except TargetFound as e:
                            retVal.append((e.target, e.path, e.uses))

                except (OverflowError, ValueError, NumberError):
                    pass

    # If retVal is empty, return None.
    if retVal:
        return retVal
    else:
        return None

def calculate(use, targets, max_fact, max_pow, max_rec, too_big):
    """
    Calculate the TAGRET number with as few uses of the USE number as possible.
    """
    
    m = Operation(
            use=int(use), targets=list(map(int, targets.split(","))),
            max_fact=max_fact, max_pow=max_pow, max_rec=max_rec, too_big=too_big)
    
    # Store all dictionaries containing num:path relationships.
    nums = ["NULL"]
    #list of tuples with (TARGET, path, numUses)
    retVal = [] 
    i = 1
    while m.TARGETS:
        # Dictionary stores numbers of path length i as num:path pairs.
        nums.append({int(str(m.USE) * i): str(m.USE) * i})
        # Combine the dictionaries with shorter paths to find more numbers.
        if i > 1:
            nums_pairs = []
            # Find which dictionaries to combine to add to i.
            for pair in subset_sum(range(1,i), i):
                nums_pairs.append((nums[pair[0]], nums[pair[1]]))
            # Calculate numbers formed by path length i.
            discovered = calculate_nthles(nums_pairs, nums[i], m)
            if discovered:
                retVal.extend(discovered)
        # Perform uniary operations on numbers of path length i.
        discovered = perform_uniary_operations(nums[i], m)
        if discovered:
            retVal.extend(discovered)
        # Increment to find numbers of next path length.
        i += 1
    
    return sort_tuple(retVal)

