from point import Point

class Path:
    def __init__(self):
        self.points = []

    def __len__(self):
        return len(self.points)

    def add(self, point):
        if not self.points or self.points[-1] != point:
            self.points.append(point)

    def length(self):
        if len(self.points) < 2:
            return 0
        return sum(self.points[i].distance(self.points[i + 1]) for i in range(len(self.points) - 1))

    def extend(self, other_path):
        for point in other_path.points:
            self.add(point)

    def __str__(self):
        return " - ".join(str(point) for point in self.points)