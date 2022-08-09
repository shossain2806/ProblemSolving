from typing import List
from collections import defaultdict
import heapq
from xxlimited import foo

     
class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
       self.dic_foods = {}
       self.dict_cuisines = defaultdict(list)
       
       for (food, cuisine, rating) in zip(foods, cuisines, ratings):
           self.dic_foods[food] = (cuisine, rating)
           heapq.heappush(self.dict_cuisines[cuisine], (-rating, food))
           
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.dic_foods[food]
        self.dic_foods[food] = cuisine, newRating
        heapq.heappush(self.dict_cuisines[cuisine] , (-newRating, food)) 
        

    def highestRated(self, cuisine: str) -> str:            
        while -self.dict_cuisines[cuisine][0][0] != self.dic_foods[self.dict_cuisines[cuisine][0][1]][1]:
            heapq.heappop(self.dict_cuisines[cuisine])
        return self.dict_cuisines[cuisine][0][1]
    
    
    
foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

food_rating = FoodRatings(
    foods=foods, cuisines=cuisines, ratings=ratings
)

print(food_rating.highestRated("korean"))
print(food_rating.highestRated("japanese"))
food_rating.changeRating("sushi", 16)
print(food_rating.highestRated("japanese"))
food_rating.changeRating("ramen", 16)
print(food_rating.highestRated("japanese"))
