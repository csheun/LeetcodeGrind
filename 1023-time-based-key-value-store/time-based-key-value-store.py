class TimeMap:

    def __init__(self):
        self.key_val_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_val_map:
            self.key_val_map[key] = []
        self.key_val_map[key].append(tuple([timestamp, value]))


    def get(self, key: str, timestamp: int) -> str:
        arr = self.key_val_map.get(key)
        if not arr:
            return ""
        # search through arr for the best timestamp
        # brute force
        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0] <= timestamp):
                return arr[i][1]
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)