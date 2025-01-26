class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key: str, value=None) -> None:
        if not isinstance(key, str) or not key:
            raise TypeError(f'Illegal argument for put: key = {key} must be a non-empty string')
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    def get(self, key: str):
        if not isinstance(key, str) or not key:
            raise TypeError(f'Illegal argument for get: key = {key} must be a non-empty string')
        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    def delete(self, key: str) -> bool:
        if not isinstance(key, str) or not key:
            raise TypeError(f'Illegal argument for delete: key = {key} must be a non-empty string')

        def _delete(node, key:str, depth: int) -> bool:
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -=1
                    return len(node.children) == 0
                return False

            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, key, 0)

    def contains(self, key: str):
        if not isinstance(key, str) or not key:
            raise TypeError(f'Illegal argument for contains: key = {key} must be a non-empty string')
        return self.get(key) is not None

    def is_empty(self) -> bool:
        return self.size == 0

    def longest_prefix_of(self, s: str) -> str:
        if not isinstance(s, str) or not s:
            raise TypeError(f'Illegal argument for longest_prefix_of: s = {s} must be a non-empty string')

        current = self.root
        longest_prefix = ''
        current_prefix = ''
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

    def _collect(self, node, path, result):
        if node.value is not None:
            result.append(''.join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys_with_prefix(self, prefix: str) -> list:
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(f'Illegal argument for keys_with_prefix: prefix = {prefix} must be a non-empty string')

        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._collect(current, list(prefix), result)
        return result


if __name__ == '__main__':
    trie = Trie()
    trie.put("apple", 1)
    trie.put("applause", 2)
    trie.put("banana", 3)
    trie.put("bat", 4)
    trie.longest_prefix_of("app")
    trie.keys_with_prefix("app")
    print(trie.size)