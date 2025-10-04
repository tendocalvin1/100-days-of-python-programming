# composition in OOP
# ✅ Composition (“Strong has-a” relationship)
# The whole object owns its parts.
# If the whole is destroyed, the parts are also destroyed.
# The part cannot meaningfully exist without the whole.


# 🟢 10 Exercises on Composition

# (Objects own their parts; parts don’t exist without the whole)

# Create a Computer class that is composed of CPU, RAM, and Storage.
class CPU:
    def __init__(self, cores, speeds):
        self.cores = cores
        self.speeds = speeds
        
class RAM:
    def __init__(self, size):
        self.size = size
        
class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        
        
class Computer:
    def __init__(self, cores, speeds, ram_size, storage_capacity):
        self.cpu = CPU(cores, speeds)
        self.ram = RAM(ram_size)
        self.storage = Storage(storage_capacity)
        
    
    def specs(self):
        return  f"CPU: {self.cpu.cores}-core {self.cpu.speeds}GHz | RAM: {self.ram.size}GB | Storage: {self.storage.capacity}GB"
    
computer1 = Computer(8, 3.5, 16, 512)
print(computer1.specs())
    
        

# Create a House class that has multiple Room objects.
class Room:
    def __init__(self, name, area):
        self.name = name
        self.area = area # in square metres
        
class House:
    def __init__(self, house_name):
        self.house_name = house_name
        self.rooms = [Room("living_room", 30), Room("sitting_room", 45), Room("bedroom", 35)]
        
    
    def show_rooms(self):
        print(f"{self.house_name} has these rooms:")
        for room in self.rooms:
            print(f"- {room.name} ({room.area}m²)")
            
house = House("Flat")
house.show_rooms()

# Create a Book class that has a TitlePage and a list of Chapter objects.
class TitlePage:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
class List:
    def __init__(self,is_availbale):
        self.is_available = True
        
        
class Book:
    def __init__(self, author, title, is_available):
        self.title_page = TitlePage(author, title)
        self.list = List(is_available)
        
        
    def description(self):
        return f"{self.title_page.author} {self.title_page.title} {self.list.is_available}"
    

book1 = Book("Steve Bartlett", "Elon Musk", True)
print(book1.description())
    


# Create a LibraryCard class that is composed into a LibraryMember class.

# Create a Phone class that has a Battery and a Screen.

# Create a Restaurant class that contains a Menu object.

# Create a Human class that has a Heart and Brain.

# Create a Company class that has a CEO object.

# Create a School class that has multiple Classroom objects.

# Create a MusicPlayer class that has a Playlist object.