from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, suffix: str) -> int:
        if not isinstance(suffix, str) or not suffix:
            raise TypeError(f'Illegal argument for count_words_with_suffix: suffix = {suffix} must be a non-empty string')

        current = self.root
        result = []

        def _collect_with_suffix(node, path, result: list, suffix: str) -> None:
            if node.value is not None:
                word = ''.join(path)
                if word.lower().endswith(suffix.lower()):
                    result.append(word)
            for char, next_node in node.children.items():
                path.append(char)
                _collect_with_suffix(next_node, path, result, suffix)
                path.pop()

        _collect_with_suffix(current, [], result, suffix)
        return len(result)

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