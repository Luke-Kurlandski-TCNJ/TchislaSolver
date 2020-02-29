from itertools import product, combinations_with_replacement

from exceptions import NumberError, TargetFound
import configs
import functions

def nice_print(nums):
    """
    Neatly print a dictionary of result:path pairs for testing purposes. 
    """
    
    for i in range(1, len(nums)):
        print("\nUsed " + str(configs.USE) + ", " + str(i) + " times:\n")
        for res in sorted(nums[i].keys()):
            print(int(res), "=", nums[i][res])
            
def total_report(nums):
    """
    Print a report of all numbers generated for testing purposes.
    """
    
    print("\nTotal Report:")
    for i in nums:
        print("Numbers Produced With " + str(i) + ", " + str(configs.USE) + "s:", len(nums[i].keys()))
    print()
        
def check_target(n, path):
    """
    Check if the target is found and print result.
    
    Arguments:
        n : int : number to check if equal to target
        path : str : operations taken to arrive at n
    """
    
    if n == configs.TARGET:
        raise TargetFound(path)
        
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

def calculate_uniary(n, x_uses, path, rdepth=1):
    """
    Fill x_uses with the results of using uniary operators on the number n.
    
    Arguments:
        n : int : integer to use
        x_uses : dict : results that requires x uses of USE
        path : str : path taken to calculate a result
        rdepth : int :  recursive depth of the function
    """
    
    # Perform each single operator on n.
    for op in configs.uniary_ops:
        # Avoid a recursion error
        if rdepth > configs.MAX_REC:
            return 
        # Avoid repetative switching sign.
        if op.__name__ == "neg" and len(path) > 1 and path[1] == "-":
            continue 
        # Calculate the result and perform recursion on result.
        sym = functions.symbol(op.__name__)
        try:
            res = op(n)
            if res not in x_uses:
                # Place minus sign/sqr in front, factorial behind
                if sym == "!":
                    x_uses[res] = "(" + path + sym + ")"
                    calculate_uniary(res, x_uses, x_uses[res], rdepth+1)
                else:
                    x_uses[res] = "(" + sym + path + ")"
                    calculate_uniary(res, x_uses, x_uses[res], rdepth+1)
                check_target(res, x_uses[res])
        except NumberError:
            continue

def perform_uniary_operations(x_uses):
    """
    Perform all uniary operations on every number in x_uses.
    
    Arguments:
        x_uses : dict : results that requires x uses of USE
    """

    for n in list(x_uses):
        calculate_uniary(n, x_uses, x_uses[n])

def calculate_nthles(nums_pairs, x_uses):
    """
    Fill x_uses with results taking x operations by performing operations with
        the values from nums_pairs.

    Arguments:
        nums_pairs : list[tuples[dict]]] : pairs of y_uses and z_uses dicts to 
            combine with binary operators
        x_uses : dict : results that requires x uses of USE to fill
    """

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
            for op in configs.binary_ops:
                # Get the operation symbol and paths for each num.
                sym = functions.symbol(op.__name__)
                path1 = nums1[num1]
                path2 = nums2[num2]
                # Calculate and add num1 op num2 to the dict.
                try:
                    res = op(num1, num2)
                    if res not in x_uses: 
                        x_uses[res] = "(" + path1 + sym + path2 + ")"
                        check_target(res, x_uses[res])
                except (OverflowError, ValueError, NumberError):
                    pass
                # Calculate and add num2 op num1 to the dict.
                try:
                    res = op(num2, num1)
                    if res not in x_uses: 
                        x_uses[res] = "(" + path2 + sym + path1 + ")"
                        check_target(res, x_uses[res])
                except (OverflowError, ValueError, NumberError):
                    pass

def calculate(TARGET, USE):
    """
    Calculate the TAGRET number with as few uses of the USE number as possible.
    """
    
    # Establish the global USE and TARGET variables.
    configs.TARGET = TARGET
    configs.USE = USE
    # Store all dictionaries containing num:path relationships.
    nums = ["NULL"]
    # An exception will be raised if the number is found.
    try:
        i = 1
        while True:
            # Dictionary stores numbers of path length i as num:path pairs.
            nums.append({int(str(configs.USE) * i): str(configs.USE) * i})
            # Combine the dictionaries with shorter paths to find more numbers.
            if i > 1:
                nums_pairs = []
                # Find which dictionaries to combine to add to i.
                for pair in subset_sum(range(1,i), i):
                    nums_pairs.append((nums[pair[0]], nums[pair[1]]))
                # Calculate numbers formed by path length i.
                calculate_nthles(nums_pairs, nums[i])
            # Perform uniary operations on numbers of path length i.
            perform_uniary_operations(nums[i])
            # Increment to find numbers of next path length.
            i += 1
    # Stop process if number was found.
    except TargetFound as e:
        uses = e.path.count(str(configs.USE))
        print(str(configs.TARGET) + " Found With " + str(uses) + " " + str(configs.USE) + "'s")
        print(str(configs.TARGET) + " = " + e.path + "\n")



