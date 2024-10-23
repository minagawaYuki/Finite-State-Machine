
class VendingMachine():
    def __init__(self) -> None:
        self.state = 0
        self.option = ""
        self.balance = 0

    def insert_coin(self):
        coin = int(input("Enter amount: "))
        return coin
    
    def is_valid_coin(self, coin):
        accepted_coins = {5, 10, 25}
        if coin not in accepted_coins:
            return False
        return True
    
    def buy(self, item_code):
        items = ['Coca Cola', 'Sprite', 'Royal', 'Mountain Dew', 'Pepsi']
        if self.state != 5:
            print("\nInsufficient amount.\n")
            return False
        if item_code < 0 or item_code > 5:
            print("\nInvalid item code.\n")
            return False
        print(f"\nYou bought {items[item_code-1]}")
        return True
    
    def set_state(self, coin):
        self.balance += coin
        next_state = 0

        transition_table = [
            [1, 2, 5],
            [2, 3, 5],
            [3, 4, 5],
            [4, 5, 5],
            [5, 5, 5],
            [5, 5, 5],
        ]

        if coin == 5:
            next_state = 0
        elif coin == 10:
            next_state = 1
        elif coin == 25:
            next_state = 2
            
        print(self.state)
        print(next_state)
        self.state = transition_table[self.state][next_state]
        print(f"State: {self.state}\n")
        

    def start(self):

        print("Available Drinks\n")
        print("1. Coca Cola")
        print("2. Sprite")
        print("3. Royal")
        print("4. Mountain Dew")
        print("5. Pepsi\n")

        while True:
            print(f"Balance: {self.balance}")
            print("Options:")
            print("insert")
            print("buy\n")

            self.option = input("Enter option: ")
            if self.option == 'insert':
                while True:
                    coin = self.insert_coin()
                    if not self.is_valid_coin(coin):
                        print("\nPlease enter 5, 10 or 25 coin only.")
                        print(f"Coin entered: {coin}\n")
                    else:
                        self.set_state(coin)
                        print(f"\nState: {self.state}\n")
                        break
            elif self.option == 'buy':
                if self.state != 5:
                    print("\nInsert more coins.\n")
                    continue
                item_code = int(input("Enter item code: "))
                if self.buy(item_code=item_code):
                    break
                continue
            else:
                print("Invalid option\n")
                

vending_machine = VendingMachine()
vending_machine.start()