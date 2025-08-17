class TimeMap:

    def __init__(self):
        self.key_val_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_val_map:
            self.key_val_map[key] = []
        self.key_val_map[key].append(tuple([timestamp, value]))


    def get(self, key: str, timestamp: int) -> str:
        print(f"searching for key: {key} timestamp: {timestamp}")
        arr = self.key_val_map.get(key)
        if not arr:
            print("Array not found")
            return ""
        # search through arr for the best timestamp
        # # brute force (works but nvr use binary search)
        # for i in range(len(arr) - 1, -1, -1):
        #     if (arr[i][0] <= timestamp):
        #         return arr[i][1]
        # return ""

        # binary search
        lo = 0
        hi = len(arr) -1
        ans = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (arr[mid][0] == timestamp):
                return arr[mid][1]
            elif (arr[mid][0] > timestamp):
                hi = mid - 1
            else:
                ans = arr[mid][1]
                lo = mid + 1
        
        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)