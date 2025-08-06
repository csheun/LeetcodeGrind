class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # make the sentence a list of words then process each word accordingly
        # for each word: find the shortest root in dictionary?
        # make dictionary into a dict, meanwhile get the length of the shortest 
        # when processing i will use the min length of word as key and slowly increase to find
        root_set = set()
        min_root_len = len(dictionary[0])
        max_root_len = len(dictionary[0])
        for root in dictionary:
            min_root_len = min(min_root_len, len(root))
            max_root_len = max(max_root_len, len(root))
            root_set.add(root)
        sentence_lst = sentence.split()
        # print(f"min_root_len: {min_root_len}")
        # print(f"max_root_len: {max_root_len}")
        for i in range(len(sentence_lst)):
            word = sentence_lst[i]

            if (len(word) >= min_root_len):
                # try find root
                for j in range(min_root_len, max_root_len + 1):
                    target = word[:j]
                    if (target in root_set):
                        sentence_lst[i] = target
                        break
        return ' '.join(sentence_lst)
                
        