
class Diet:
    def _init_(self, breakfastKcals, lunchKcals, dinnerKcals, exercise, 
    basicMetaRate):
        self.breakfastKcals = breakfastKcals
        self.lunchKcals = lunchKcals
        self.dinnerKcals = dinnerKcals
        self.exercise = exercise
        self.basicMetaRate = basicMetaRate
    
    def kCalDeficit(self):
        deficit = self.basicMetaRate +self.exercise - (self.breakfastKcals + 
        self.lunchKcals + self.dinnerKcals)
        return deficit

breakfastKcals = int(input("How many calories did you have for breakfast? "))
lunchKcals = int(input("How many calories did you have for lunch? "))
dinnerKcals = int(input("How many calories did you have for dinner? "))
exercise = int(input("How many calories did you burn from exercising? "))
basicMetaRate = int(input("what is your basic metabolic rate? "))

fitness = Diet(breakfastKcals, lunchKcals, dinnerKcals, exercise, basicMetaRate) 

weeklyDeficit = 7 * fitness.kCalDeficit()

if weeklyDeficit > 0:
    print(f"You will lose {weeklyDeficit / 3600} lbs. per week")
elif weeklyDeficit == 0:
    print(f"You weight simply won't change.")
else:
    print(f"You will gain {-1 * weeklyDeficit / 3600} lbs. per week.")


