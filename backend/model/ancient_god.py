""" Class AncientGod
"""

# pylint: disable=too-many-instance-attributes
#          - the structure of class comes from an external JSON file.

class AncientGod:
    """
    Represents an ancient god with various attributes.
    Attributes:
        name (str): The name of the god.
        greek_name (str): The Greek equivalent name (optional).
        roman_name (str): The Roman equivalent name (optional).
        category (str): The category or type of god (optional).
        description (str): A description of the god.
        immortal (bool): Whether the god is immortal (optional).
        gender (str): Gender of the god (optional).
        images (dict): A dictionary of image references (optional).
        relatives (dict): A dictionary of relatives (optional).
        books (list): A list of books associated with the god (optional).
        events (list): A list of events associated with the god (optional).
    """

    def __init__(self, name, description=None, attributes=None):
        """
        Represents an ancient god with various attributes.
        Attributes:
            name (str): The name of the god.
            greek_name (str): The Greek equivalent name (optional).
            roman_name (str): The Roman equivalent name (optional).
            category (str): The category or type of god (optional).
            description (str): A description of the god.
            immortal (bool): Whether the god is immortal (optional).
            gender (str): Gender of the god (optional).
            images (dict): A dictionary of image references (optional).
            relatives (dict): A dictionary of relatives (optional).
            books (list): A list of books associated with the god (optional).
            events (list): A list of events associated with the god (optional).
        """
        self.name = name
        self.description = description
        self.greek_name = attributes["greek_name"] if attributes["greek_name"] else ""
        self.roman_name = attributes["roman_name"] if attributes["roman_name"] else ""
        self.category = attributes["category"] if attributes["category"] else ""
        self.immortal = attributes["immortal"] if attributes["immortal"] else ""
        self.gender = attributes["gender"] if attributes["gender"] else ""
        self.images = attributes["images"] if attributes["images"] else {}
        self.relatives = attributes["relatives"] if attributes["relatives"] else {}
        self.books = attributes["books"] if attributes["books"] else []
        self.events = attributes["events"] if attributes["events"] else []

    def json(self):
        """
        Converts the attributes of the current object into a JSON-compatible dictionary.
        Returns:
            dict: A dictionary containing the following keys:
                - 'name' (str): The name of the entity.
                - 'greekName' (str): The Greek name of the entity.
                - 'romanName' (str): The Roman name of the entity.
                - 'category' (str): The category or classification of the entity.
                - 'description' (str): A textual description of the entity.
                - 'immortal' (bool): Indicates whether the entity is immortal.
                - 'gender' (str): The gender of the entity.
                - 'images' (list): A list of image URLs or image metadata related to the entity.
                - 'relatives' (list): A list of relatives or associated entities.
                - 'books' (list): A list of books or references related to the entity.
                - 'events' (list): A list of events associated with the entity.
        """
        return {
            'name': self.name,
            'greekName': self.greek_name,
            'romanName': self.roman_name,
            'category': self.category,
            'description': self.description,
            'immortal': self.immortal,
            'gender': self.gender,
            'images': self.images,
            'relatives': self.relatives,
            'books': self.books,
            'events': self.events
        }

    def __str__(self):
        return (f'AncientGod(name={self.name}, '
                f'greek_name={self.greek_name}, '
                f'roman_name={self.roman_name})')

    def __repr__(self):
        return (f'AncientGod(name={self.name}, '
                f'greek_name={self.greek_name}, '
                f'roman_name={self.roman_name}, '
                f'category={self.category})')
