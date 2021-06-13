class ItemValue:
 
    """Item Value DataClass"""
 
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt
 
    def __lt__(self, other):
        return self.cost < other.cost
 
# Greedy Approach
 
class FractionalKnapSack:
 
    def getMaxValue(wt, val, capacity):
        """function to get maximum value """
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
 
        # sorting items by value
        iVal.sort(reverse=True)
 
        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = float(capacity - (curWt * fraction))
                break
        return totalValue
 
 
# Driver Code
if __name__ == "__main__":
    #weight input
    wt = []
    val = []

    n = int(input("Enter number of elements: "))
    
    print("Enter WEIGHT")
    for i in range(0, n):
        ele1 = int(input())
        wt.append(ele1) 

    print("Enter Value")
    for i in range(0, n):
        ele2 = int(input())
        val.append(ele2)
    
    capacity = int(input("Enter Capacity: "))
 
    # Function call
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)