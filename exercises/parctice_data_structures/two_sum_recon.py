from typing import List

class Solution:
    def reconcile_ledger(self, transactions: List[int], target: int) -> List[int]:
        txn_dict = dict(transactions)
        print(txn_dict)
        return []

if __name__=="__main__":
    list = [2, 4, 3, 6, 8, 5]
    target = 8
    sol = Solution()
    sol.reconcile_ledger(list, target)