#
# @lc app=leetcode id=380 lang=python
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
            self.a = []

    def insert(self, val: int) -> bool:
           if val in self.a:
                return False
            else:
                self.a.append(val)
                return True

    def remove(self, val: int) -> bool:
           if val in self.a:
                self.a.remove(val)
                return True
            else:
                return False

    def getRandom(self) -> int:
           return random.choice(self.a)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

