import heapq
"""
You are given a list of (title, plays) tuples where the first element is the name of a song, and the second is the number of times the song has been played. You are also given a positive integer k. Return the k most played songs from the list, in any order.

If the list has fewer than k songs, return all of them.
Break ties in any way you want.
You can assume that song titles have a length of at most 50.
"""

class TopSongs:
    def __init__(self, k):
        self.k = k
        self.heap = []
        self.seen_songs = set()
        self.smallest_k = 0

    def register_plays(self,title,plays):
        if title not in self.seen_songs and len(self.heap) < self.k:
            self.heap.append((-plays,title))
            self.seen_songs.add(title)
            if -self.heap[self.smallest_k][0] < plays:
                self.smallest_k = len(self.heap) - 1
        elif title not in self.seen_songs and len(self.heap) >= self.k:
            self.heap.pop(self.smallest_k)
            self.heap.append((-plays,title))
            new_smallest_k = 0
            for idx in range(len(self.heap)):
                if -self.heap[idx][0] < -self.heap[new_smallest_k][0]:
                    new_smallest_k = idx
            self.smallest_k = new_smallest_k

            self.seen_songs.add(title)
        else:
            print("title has already been logged")

    def top_k(self):
        heap = self.heap[:]
        heapq.heapify(self.heap)

        result = []
        for _ in range(self.k):
            if not heap:
                break
            _, name = heapq.heappop(heap)
            # Convert back to (name, original_count)
            result.append(name)
        return result

        
example = TopSongs(3)
example.register_plays("Boolean Rap", 193)
example.register_plays("Coding tools", 203)
example.register_plays("Coding tools 2", 203)
example.register_plays("Coding tools 3", 303)
example.register_plays("Coding tools 4", 503)
example.register_plays("Coding tools 5", 503)

result = example.top_k()
print(result)