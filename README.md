# Pexip Homework - Word Search
## Solution Theory
In arriving at my solution, I iterated over various alternatives including implementing a modified Rabin-Karp search algorithm applied to each row and column. However, taking into consideration the problem constraints and the nature of the problem being a 2-dimensional word search I settled on a trie-like data structure with a limited depth for my approach.

### Pre-processing
For instance, consider the following search grid:
```
b c e
d a f
g r h
```
Each character in the grid would be indexed by its position in the original search grid string as follows:
```
0 1 2
3 4 5
6 7 8
```
For each character, every right and down adjacent characters up to the length of `TRIE_DEPTH` (the maximum depth of the "trie" structure), and within the bounds of the grid, would be indexed to the character's position in the grid. So for the character `b` in position `0`  and a `TRIE_DEPTH` of value `2` the strings `b`, `bc` and `bd` would be indexed to position `0`.

The trie is implemented as a Python dictionary, where the keys are strings that make up words in the grid, and the values are lists of integer positions corresponding to the indexing explained above. For the above example, the first three entries to the dictionary would be as follows:
`{('b', [0]), ('bc', [0]), ('bd', [0])}`.

### Searching for a word

For a word with length less than or equal to `TRIE_DEPTH`, a search is as simple as looking up the word as a key in the dictionary (constant O(1) time complexity). If the lookup returns an exception (i.e. no such key exists) then `False` is returned. Otherwise, `True` is returned.

For a word with length greater than `TRIE_DEPTH` a prefix of the word being searched of length `TRIE_DEPTH` is taken. This is then looked up as a key in the dictionary as before. If the lookup returns an exception, `False` is returned. Otherwise, every position of the prefix to the word in the grid (value from the key in the dictionary) is searched both horizontally right and vertically down. If any word matches, `True` is returned. However, if no prefix searches result in a word match, `False` is returned.

## Testing

Throughout implementation I made use of the **unittest** unit testing framework to test my program. I experimented with various `TRIE_DEPTH` values and ended up using `2` as the value optimised for my 8GB RAM, 4-core laptop.

On average, on my laptop, a search for `1000` words in a `500x500` character grid took **1998ms**. And while my laptop specs are not optimised for fast runtime speeds, a far higher-load search for `100000` words in a `1000x1000` character grid took only ~**520s**.

The value of `TRIE_DEPTH` is a large contributing factor when it comes to considering word search runtimes. While a greater `TRIE_DEPTH` value would increase speed of runtime for the word search, the time taken for pre-processing the grid would be much longer. And vice versa, if the `TRIE_DEPTH` was a smaller value, the time taken for pre-processing the grid would be much less, while word search times would be increased, as fewer words would be searchable in O(1) time and more positions for word prefixes would have to be iterated through.

If I were to improve my solution, I would also take into consideration the space complexity of my program and potentially write my solution in a different language, such as C, which is more optimised for low-level memory management.

## Bonus Question

In order to take advantage of a multicore system I could multi-thread the process of searching through the trie structure. Each thread could pop a word from the list of words to search for, and then search the pre-processed trie structure with calls to `is_present()`. As the word list is a shared resource it would need to be locked to ensure mutual exclusion of threads - i.e. to prevent two threads racing to pop a word, and both popping the same word causing searches to be duplicated.

Also, in considering the pre-processing of the search grid, I could allocate a thread to each character in the grid to perform the indexing operations in the trie. Again, the trie would need to be locked for read/write operations as it's a shared resource amongst the threads.
