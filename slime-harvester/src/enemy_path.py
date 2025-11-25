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
        with open(path) as f:
            rows = [line.strip() for line in f.readlines()]
        return rows
    

    def get_path(self, map_data):
        # Collect all '!' tile centers (in pixels)
        points = []
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

        # If there are 0 or 1 points, nothing to reorder
        if len(points) <= 1:
            return points

        # Greedy nearest-neighbor ordering: start from the first found point
        ordered = [start]
        remaining = points.copy()
        current = start

        while remaining:
            # find the remaining point closest to current
            best_idx = None
            best_dist_sq = None
            cx, cy = current
            for i, (rx, ry) in enumerate(remaining):
                dx = rx - cx
                dy = ry - cy
                dist_sq = dx * dx + dy * dy
                if best_dist_sq is None or dist_sq < best_dist_sq:
                    best_dist_sq = dist_sq
                    best_idx = i

            # move the closest point to ordered list and continue
            current = remaining.pop(best_idx)
            ordered.append(current)
        return ordered
#AI generoima loppuu