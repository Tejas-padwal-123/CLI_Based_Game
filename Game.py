import random

class Game:
    def __init__(self):
        """
        Initialize Game class and animal list and points attriblues has been defined/intialize here.
        """
        self.animals = ["lion", "tiger", "deer", "bear"]
        self.points = 0

    def start(self):
        """
        In this method selected Gun and animals will apper one after other, and we will shoot for each of them.
        """
        print("Welcome to the Animal Shooting Game!")
        print("Select a gun: Pistol, Rifle, Shotgun")
        selected_gun = input("Enter the the gun: ").lower()
        player = Player(selected_gun)
        while True:
            choice = input("Shoot an animal? (yes/no): ").lower()
            if choice == 'yes':
                animal = random.choice(self.animals)
                player.shoot(animal)
            elif choice == "no":
                final_score = player.final_result()
                print("final score is",final_score)
                break
            else:
                print('Invalid choice. Please enter yes or no.')




class Player:
    """
        Initialize Player class and  selected_gun and points attriblues has been defined/intialize here.
    """
    def __init__(self, selected_gun):
        self.selected_gun = selected_gun
        self.points = 0

    def shoot(self, animal):
        """
        This function will increase the point when aniaml will get hit
        """
        print(f"Shooting {animal}...")
        if random.random() > 0.5:  # 50% chance of hitting the animal
            points = self.calculate_points(animal)
            print(f"You shot the {animal}! You earned {points} points.")
            self.points += points
        else:
            print(f"You missed the {animal}!")

    def final_result(self):
        return (self.points)

    def calculate_points(self, animal):
        # Points can be based on the type of animal and the selected gun
        points_table = {
            "lion": {"pistol": 10, "rifle": 20, "shotgun": 30},
            "tiger": {"pistol": 15, "rifle": 25, "shotgun": 35},
            "deer": {"pistol": 5, "rifle": 10, "shotgun": 15},
            "bear": {"pistol": 25, "rifle": 35, "shotgun": 45}
        }
        return points_table[animal][self.selected_gun]

# Test the game
game = Game()
game.start()
