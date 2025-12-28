# Day 1: The "Reconciliation" Problem (Two Sum)

**Theme: Arrays & HashMaps (Dictionaries)**
    
**Fintech Context: Ledger Reconciliation**
    
**The Challenge**
    You have a list of transaction amounts. You need to find the indices of the two transactions that sum up to a specific target invoice amount.
    
        - Input: transactions (List[int]), target (int)
        
        - Output: List[int] (The two indices, e.g., [0, 3])
        
        - Constraints
            Time Complexity: O(n) (One pass).
            Space Complexity: O(n).
    
    You cannot use the same element twice.
    
**Starter Code:**
```python
from typing import List

class Solution:
    def reconcile_ledger(self, transactions: List[int], target: int) -> List[int]:
        # TODO: Implement O(n) solution using a dictionary
        # Hint: dictionary map should be { value: index }
        pass
```
    
**Test Case**
    transactions = [2750, 1500, 4500, 3250]
    target = 6000
    Expected Output: [0, 3]