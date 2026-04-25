import pickle

class CustomObject:
    """
    A custom Python class representing a person with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with name, age, and is_student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints out the object's attributes in a formatted manner.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance and saves it to a file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (IOError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from a file.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError, IOError):
            return None
