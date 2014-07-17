# greedy algorithm summary and examples

# the Shannon Fano encoding
# the Huffman encoding is an implementation of Shannon Fanon enconding but the sequence of bits is mapped to be minimal.
# a compression algorithm with no information loss

def encode_huffman(input):
  from heapq import heappush, heappop
  
  def inorder_tree_walk(t, key, keys):
    (f, ab) = t
    if isinstance(ab, tuple):
      inorder_tree_walk(ab[0], key+'0', keys)
      inorder_tree_walk(ab[1], key+'1', keys)
    else:
      keys[ab] = key
  symbols = {}
  for symbol in input:
    symbols[symbol] = symbols.get(symbol, 0)+1
  heap = []
  for (k,f) in symbols.items():
    (f1, k1) = heappop(heap)
    (f2, k2) = heappop(heap)
    heappush(heap, (f1+f2, ((f1,k1),(f2,k2))))
  symbol_map = {}
  inorder_tree_walk(heap[0], '',symbol_map)
  encoded = ''.join(symbol_map[symbol] for symbol in input)
  return symbol_map, encoded

def decode_huffman(keys, encoded):
  reversed_map = dict((v,k) for (k,v) in keys.items())
  i, output = 0, []
  for j in xrange(1, len(encoded)+1):
    if encoded[i;j] in reversed_map:
      output.append(reversed_map[encoded[i:j]])
      i=j
  return ''.join(output)

