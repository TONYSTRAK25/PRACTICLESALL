import heapq

def huffman_encoding(char_freq):
    heap = [[freq, [char, ""]] for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Example usage
if __name__ == "__main__":
    char_freq = {
        'a': 5,
        'b': 5,
        'c': 5,
        'd': 5,
        # 'e': 16,
        # 'f': 45
    }

    huffman_codes = huffman_encoding(char_freq)
    print("Character codes:")
    for char, code in huffman_codes:
        print(f"{char}: {code}")
