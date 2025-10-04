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

class House:
    def __init__(self, name, year, age):
        self.name = name
        self.year = year
        self.age = age
        

house1 = House("Bungalow", 2022, 3)
house2 = House("Flat", 2020, 5)
house3 = House("Mansion", 2019, 6)


print(house2.name)
print(house2.year)
print(house2.age)

# Create a Book class that has a TitlePage and a list of Chapter objects.

# Create a LibraryCard class that is composed into a LibraryMember class.

# Create a Phone class that has a Battery and a Screen.

# Create a Restaurant class that contains a Menu object.

# Create a Human class that has a Heart and Brain.

# Create a Company class that has a CEO object.

# Create a School class that has multiple Classroom objects.

# Create a MusicPlayer class that has a Playlist object.