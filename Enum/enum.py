from enum import Enum, auto

class Category(Enum):
    category_a  = auto()
    category_b  = auto()
    category_c  = auto()

# example trigger function
def Trigger(category: Category):
    if category == Category.category_a:
        print(Category.__name__ + ' A!')
    
if __name__ == "__main__":
    Trigger(Category.category_a)
    Trigger(Category.category_b)
    Trigger(Category.category_c)

    for c in Category:
        print(c.name, '->', c.value)