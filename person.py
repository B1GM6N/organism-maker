people = []
animals = []

class Organism:
    def __init__(self, color):
        self.color = color

class Person(Organism):
    def __init__(self, gender, name, hairstyle, haircolor, shirt, hoodie, jacket, pants, shoes):
        color = input("What is the color of their skin?")
        super().__init__(color)
        self.hairstyle = hairstyle
        self.shirt = shirt
        self.hoodie = hoodie
        self.jacket = jacket
        self.pants = pants
        self.shoes = shoes
        self.name = name
        self.gender = gender
        self.haircolor = haircolor
        
    def change_clothes(self, shirt, hoodie, jacket, pants, shoes):
        self.shirt = shirt
        self.hoodie = hoodie
        self.jacket = jacket
        self.pants = pants
        self.shoes = shoes

    def change_hair(self, hairstyle, haircolor):
        self.haircolor = haircolor
        self.hairstyle = hairstyle

    def print_everything(self):
        print(self.gender)
        print(self.name)
        print(self.hairstyle)
        print(self.haircolor)
        print(self.shirt)
        print(self.hoodie)
        print(self.jacket)
        print(self.pants)
        print(self.shoes)

class Animal(Organism):
    def __init__(self, name, animal, color):
        super().__init__(color)
        self.name = name
        self.animal = animal
        
    def print_everything(self):
        print(self.name)
        print(self.animal)
        print(self.color)

def main():
    while True:
        print("Would you like to 1 - make a person? or 2 - change a persons clothes or hair? or 3 - Leave. or 4 - make an animal?")
        option = input(">")
        if option == "1":
            print("Lets make a person!")
            print("If your person is not wearing this type of clothing type none.")
            name = input("What is their name?")
            people.append(name)
            color = input("What is the color of their skin?")
            gender = input("What is their gender?")
            hair = input("What is their hairstyle?")
            haircolor = input("What is their hair color?")
            shirt = input("What shirt are they wearing?")
            hoodie = input("What hoodie are they wearing?")
            jacket = input("What jacket are they wearing?")
            pants = input("What pants are they wearing?")
            shoes = input("What shoes are they wearing?")
            name = Person(gender, name, hair, haircolor, shirt, hoodie, jacket, pants, shoes)
            name.print_everything()
        elif option == "2":
            print("Who are you changing?")
            name = input(">")
            if name in people:
                print("Would you like to 1 - change their clothes 2 - change their hair.")
                change = input(">")
                if change == "1":
                    shirt = input("What new shirt are they wearing?")
                    hoodie = input("What new hoodie are they wearing?")
                    jacket = input("What newjacket are they wearing?")
                    pants = input("What new pants are they wearing?")
                    shoes = input("What new shoes are they wearing?")
                    name.change_clothes(shirt, hoodie, jacket, pants, shoes)
                    name.print_everything()
                elif change == "2":
                    hair = input("What is their hairstyle?")
                    color = input("What is their hair color?")
                    name.change_hair(hair, color)
                    name.print_everything()
                else:
                    print("not valid input.")
                    print("That person has not been made yet.")
        elif option == "3":
            break
        elif option == "4":
            name = input("What is the animals name?")
            animal = input("What type of animal is it?")
            color = input("What color is it?")
            animals.append(name)
            name = Animal(name, animal, color)
            name.print_everything()
        else:
            print("not valid input.")


main()