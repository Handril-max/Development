
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]
            items += f"{description:<23}{amount:>7.2f}\n"
            total += amount
        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    total_spent = 0
    category_spent = []
    category_names = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent -= item["amount"]
        category_spent.append(spent)
        total_spent += spent
        category_names.append(category.name)

    percentages = [int((spent / total_spent) * 10) * 10 for spent in category_spent]

    chart = "Percentage spent by category
"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"

    return chart


# Create category objects
food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")

# Deposit and withdraw from categories
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
clothing_category.transfer(50, food_category)
auto_category.transfer(100, food_category)
clothing_category.withdraw(25.55, "jeans")

# Print category objects
print(food_category)
print(clothing_category)
print(auto_category)

# Print spend chart
print(create_spend_chart([food_category, clothing_category, auto_category]))