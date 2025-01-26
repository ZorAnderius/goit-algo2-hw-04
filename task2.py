from trie import Trie

class LongestCommonWord(Trie):
    def _put_list(self, strings: list):
        if not isinstance(strings, list) or not strings:
            raise TypeError(
                f'Illegal argument for find_longest_common_word: strings = {strings} must be a non-empty list')
        for idx, string in enumerate(strings):
            if not isinstance(string, str) or not string:
                raise TypeError(
                    f'Illegal argument for find_longest_common_word: string = {string} must be a non-empty string')
            self.put(string, idx + 1)

    def find_longest_common_word(self, strings: list) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(f'Illegal argument for find_longest_common_word: strings = {strings} must be a non-empty list')

        self._put_list(strings)
        longest_prefix = ''
        current = self.root
        while len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            longest_prefix += char
            current = current.children[char]
        return longest_prefix


if __name__ == '__main__':
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

