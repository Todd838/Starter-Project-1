"""
Name: Todd Perkins
SID: 03130462
"""

class Boggle:
    """
    A class to represent the Boggle game solver.
    """

    def __init__(self, grid, dictionary):
        """
        Initialize the Boggle instance with a grid and dictionary.
        """
        self.grid = grid
        self.dictionary = set(dictionary)
        self.solutions = set()
        self.rows = len(grid)
        self.cols = len(grid[0])

    def getSolution(self):
        """
        Find all valid words from the dictionary that can be formed on the grid.
        """
        visited = [[False] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, "", visited)
        return sorted(self.solutions)

    def dfs(self, row, col, path, visited):
        """
        Perform a depth-first search to explore all word paths starting at (row, col).
        """
        if visited[row][col]:
            return

        word = path + self.grid[row][col]
        if not self.isPrefix(word):
            return

        if word.lower() in self.dictionary:
            self.solutions.add(word.lower())

        visited[row][col] = True

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < self.rows and 0 <= newCol < self.cols:
                    self.dfs(newRow, newCol, word, visited)

        visited[row][col] = False

    def isPrefix(self, prefix):
        """
        Check if the given prefix starts any word in the dictionary.
        """
        for word in self.dictionary:
            if word.startswith(prefix.lower()):
                return True
        return False


def main():
    """
    Run a test game of Boggle with a sample grid and dictionary.
    """
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
