import Foundation

class Food {
    let name: String
    let cuisine: String
    var rating: Int
    init(name: String, cuisine: String, rating: Int) {
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
    }
}

class FoodRatings {
    var food_dic: [String: Food] =  [:]
    var cuisine_dic: [String: [Food]] = [:]

    init(_ foods: [String], _ cuisines: [String], _ ratings: [Int]) {
            let len = foods.count
            for index in 0..<len {
                let food = Food(name: foods[index], cuisine: cuisines[index], rating: ratings[index])
                food_dic[food.name] = food
                if let _ = cuisine_dic[food.cuisine] {
                    cuisine_dic[food.cuisine]?.append(food)
                } else{	
                    cuisine_dic[food.cuisine] = [food]
                }
            }
            
            for key in cuisine_dic.keys {
                cuisine_dic[key] = cuisine_dic[key]?.sorted(by: { f1, f2 in
                    if f1.rating > f2.rating {
                        return true
                    } else if f1.rating == f2.rating && f1.name < f2.name {
                        return true
                    }
                    return false
                })
            }
        }
        
        func changeRating(_ food: String, _ newRating: Int) {
            if let item = food_dic[food] {
                item.rating = newRating
                cuisine_dic[item.cuisine] = cuisine_dic[item.cuisine]?.sorted(by: { f1, f2 in
                    if f1.rating > f2.rating {
                        return true
                    } else if f1.rating == f2.rating && f1.name < f2.name {
                        return true
                    }
                    return false
                })
            }
            
        }
        
        func highestRated(_ cuisine: String) -> String {
            return self.cuisine_dic[cuisine]?.first?.name ?? ""
        }
}
