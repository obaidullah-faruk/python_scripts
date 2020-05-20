class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.gusesses = 0
        self.min = mn
        self.max = mx
    
    def get_guess(self):
        guess = input(f"Please guess a number ({self.min} - {self.max}): ")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("Enter a valid number. ")
            return self.get_guess()
          
    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False
        return self.min <= number <= self.max

    def play(self):
        while True:
            self.gusesses += 1
            guess = self.get_guess()
            if guess < self.number:
                print("Guess was under.")
            elif guess > self.number:
                print("Guess was over.")
            else:
                break
        print(f"You have guessed it in {self.gusesses} guesses.")

game= GuessNumber(45, 0, 100)
game.play()