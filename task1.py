from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, suffix: str) -> int:
        if not isinstance(suffix, str) or not suffix:
            raise TypeError(f'Illegal argument for count_words_with_suffix: suffix = {suffix} must be a non-empty string')

        current = self.root
        result = []
        self._collect(current, [], result)
        return len([w for w in result if w.lower().endswith(suffix.lower())])

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(f'Illegal argument for has_prefix: prefix = {prefix} must be a non-empty string')

        current = self.root
        for char in prefix:
            char = char.lower()
            if char not in current.children:
                return False
            current = current.children[char]
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("E") == 1  # apple
    assert trie.count_words_with_suffix("iOn") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat