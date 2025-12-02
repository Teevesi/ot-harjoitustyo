import os

class EnemyPath:
#AI generoima alkaa (vähän itse muokattu)
    def __init__(self, map_path, tile_size):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, map_path)
        self.map_data = self.load_map(full_path)
        self.tile_size = tile_size
        self.path = self.get_path(self.map_data)

    def load_map(self, path):
        with open(path, encoding="utf-8") as f:
            rows = [line.strip() for line in f.readlines()]
        return rows

    def get_path(self, map_data):
        # Collect all '!' tile centers (in pixels)
        points = []
        start = None
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile == "S":
                    # Start point
                    px = x * self.tile_size + self.tile_size // 2
                    py = y * self.tile_size + self.tile_size // 2
                    start = (px, py)

                if tile == "!":
                    px = x * self.tile_size + self.tile_size // 2
                    py = y * self.tile_size + self.tile_size // 2
                    points.append((px, py))

        if start is None:
            raise ValueError("Map must have a starting point 'S'")

        self.path = self.order_path(points, start)
        return self.path

    def order_path(self, points, start):

        # If there are 0 or 1 points, nothing to reorder
        if len(points) <= 1:
            return points

        # Greedy nearest-neighbor ordering: start from the first found point
        ordered = [start]
        remaining = points.copy()
        current = start

        while remaining:
            # find the closest point using min()
            closest = min(remaining, key=lambda p: (p[0]-current[0])**2 + (p[1]-current[1])**2)
            ordered.append(closest)
            remaining.remove(closest)
            current = closest

        return ordered
#AI generoima loppuu
