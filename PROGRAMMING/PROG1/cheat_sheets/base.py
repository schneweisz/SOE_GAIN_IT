# The central data class representing one row of data
class Entity:
    def __init__(self, name, value, category):
        self.name = name          # String: e.g., Student Name, City Name
        self.value = int(value)   # Integer: e.g., Score, Population
        self.category = category  # String: e.g., Subject, Country

# Global list that will store our objects
data_list = []

# Example manual data for testing if file reading is not used
# data_list = [
#     Entity("Alice", 85, "A"),
#     Entity("Bob", 40, "B"),
#     Entity("Charlie", 95, "A")
# ]