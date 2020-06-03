class GuessNumber:
    def __init__(self, number, min = 0, max = 100):
        self.number = number
        self.min = min
        self.max = max
        self.counter = 0

    def ask(self):
        guess = input(f"Please guess a number from {self.min} to {self.max}: ")
        if self.validate(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            return self.ask()

    def validate(self, guess):
        try:
            guess = int(guess)
        except:
            return False
        return self.min <= guess <= self.max

    def play(self):
        while True:
            self.counter += 1
            guess = self.ask()

            if guess < self.number:
                print("Your guess was under.")
            elif guess > self.number:
                print("Your guess was over.")
            else:
                print(f"You've guessed it! the number is {self.number}")
                break
        print(f"You try to guess it {self.counter} times")


game1 = GuessNumber(50)
game1.play()