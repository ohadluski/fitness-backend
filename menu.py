import random

# Menu to be randomized and pulled for each user. 

Breakfast = [
    {
        "name": "Greek Yogurt Parfait",
        "calories": 250,
        "ingredients": ["1. 1 cup Greek yogurt \n", "2. 1/2 cup mixed berries \n", "3. 1/4 cup granola \n",
                        "4. 1 tbsp honey \n"],
        "level of difficulty": "Easy",
        "cooking time": "5 minutes",
        "instructions": "1. In a bowl or glass, layer Greek yogurt, mixed berries, and granola. \n"
                        "2. Drizzle honey on top. \n"
                        "3. Serve immediately."
    },
    {
        "name": "Egg and Veggie Scramble",
        "calories": 300,
        "ingredients": ["1. 2 eggs \n", "2. 1/2 cup chopped veggies (bell pepper, onion, spinach) \n",
                        "3. 1 tsp olive oil \n", "4. Salt and pepper to taste \n"],
        "level of difficulty": "Easy",
        "cooking time": "10 minutes",
        "instructions": "1. Heat olive oil in a pan over medium heat. \n"
                        "2. Add chopped veggies and sauté for 2-3 minutes. \n"
                        "3. Beat eggs in a bowl and pour over the veggies. \n"
                        "4. Scramble the eggs and veggies together. \n"
                        "5. Season with salt and pepper. \n"
                        "6. Serve hot."
    },
    {
        "name": "Peanut Butter Banana Smoothie",
        "calories": 350,
        "ingredients": ["1. 1 banana \n", "2. 1 cup almond milk \n", "3. 1 tbsp peanut butter \n", "4. 1 tsp honey \n",
                        "5. Ice cubes (optional)"],
        "level of difficulty": "Easy",
        "cooking time": "5 minutes",
        "instructions": "1. Blend all ingredients in a blender until smooth. \n"
                        "2. Add ice cubes if desired. \n"
                        "3. Serve cold."
    },
    {
        "name": "Oatmeal with Fruit and Nuts",
        "calories": 300,
        "ingredients": ["1. 1/2 cup rolled oats \n", "2. 1 cup water \n", "3. 1/2 cup mixed berries \n",
                        "4. 1 tbsp chopped nuts (almonds, walnuts, pecans) \n", "5. 1 tsp honey"],
        "level of difficulty": "Easy",
        "cooking time": "10 minutes",
        "instructions": "1. Combine oats and water in a saucepan and bring to a boil. \n"
                        "2. Reduce heat and simmer for 5-7 minutes, stirring occasionally. \n"
                        "3. Top with mixed berries, chopped nuts, and honey. \n4. Serve hot."
    },
    {
        "name": "Vegetable Frittata",
        "calories": 350,
        "ingredients": ["1. 4 eggs \n", "2. 1/2 cup chopped veggies (bell pepper, onion, spinach) \n",
                        "3. 1/4 cup shredded cheese \n", "4. 1 tsp olive oil \n", "5. Salt and pepper to taste \n"],
        "level of difficulty": "Medium",
        "cooking time": "20 minutes",
        "instructions": "1. Preheat oven to 375°F (190°C). \n"
                        "2. Heat olive oil in a skillet over medium heat. \n"
                        "3. Add chopped veggies and sauté for 2-3 minutes. \n"
                        "4. In a bowl, beat eggs and season with salt and pepper. \n"
                        "5. Pour eggs over the veggies and sprinkle shredded cheese on top. \n"
                        "6. Transfer skillet to the oven and bake for 10-15 minutes or until eggs are set. \n"
                        "7. Serve hot."
    },
    {
        "name": "Avocado and Egg Toast",
        "calories": 350,
        "ingredients": ["1. 1 slice of whole grain bread \n", "2. 1/2 avocado \n", "3. 1 egg \n",
                        "4. 1/4 teaspoon red pepper flakes \n", "5. Salt and pepper to taste"],
        "level of difficulty": "Easy",
        "cooking time": "10 minutes",
        "instructions":
            "1. Toast the bread until crispy. \n"
            "2. Mash the avocado and spread it on the toast. \n"
            "3. Fry an egg in a nonstick pan until cooked to your preference. \n"
            "4. Place the egg on top of the avocado toast. \n"
            "5. Sprinkle red pepper flakes, salt, and pepper on top and serve. \n"
    },
    {
        "name": "Veggie Omelet",
        "calories": 300,
        "ingredients": ["1. 2 eggs \n", "2. 1/4 cup of chopped mixed veggies (e.g. bell peppers, onions, spinach) \n",
                        "3. 1/4 cup of shredded cheese \n", "4. 1 teaspoon of olive oil \n",
                        "5. Salt and pepper to taste"],
        "level of difficulty": "Intermediate",
        "cooking time": "15 minutes",
        "instructions":
            "1. In a bowl, whisk together the eggs, chopped veggies, salt, and pepper. \n"
            "2. Heat the olive oil in a nonstick pan over medium heat. \n"
            "3. Pour the egg mixture into the pan and cook until the bottom is set. \n"
            "4. Sprinkle the shredded cheese over one half of the omelet. \n"
            "5. Using a spatula, fold the other half of the omelet over the cheese. \n"
            "6. Cook for another minute or until the cheese is melted and the eggs are cooked through. \n"
            "7. Serve hot."
    }
]

Lunch = [
    {
        "name": "Quinoa Salad",
        "calories": 350,
        "ingredients": ["quinoa", "cherry tomatoes", "cucumber", "red onion", "feta cheese", "olive oil", "lemon juice",
                        "salt", "pepper"],
        "level_of_difficulty": "Easy",
        "cooking_time": "20 minutes",
        "instructions": "1. Rinse quinoa and cook according to package instructions. \n"
                        "2. Dice cherry tomatoes, cucumber, and red onion. \n"
                        "3. Mix together quinoa, vegetables, and feta cheese. \n"
                        "4. In a separate bowl, whisk together olive oil, lemon juice, salt, "
                        "and pepper to make the dressing. \n"
                        "5. Pour dressing over quinoa mixture and stir to combine."
    },
    {
        "name": "Grilled Chicken Wrap",
        "calories": 400,
        "ingredients": ["chicken breast", "whole wheat wrap", "lettuce", "tomato", "red onion", "hummus",
                        "tzatziki sauce"],
        "level_of_difficulty": "Medium",
        "cooking_time": "30 minutes",
        "instructions": "1. Season chicken breast with salt and pepper, and grill until cooked through. \n"
                        "2. Slice chicken breast into strips. \n"
                        "3. Lay out whole wheat wrap and spread hummus and tzatziki sauce on top. \n"
                        "4. Add sliced chicken breast, lettuce, tomato, and red onion. \n"
                        "5. Roll up wrap tightly and slice in half."
    },
    {
        "name": "Vegetable Stir Fry",
        "calories": 300,
        "ingredients": ["brown rice", "broccoli", "carrots", "snap peas", "mushrooms", "garlic", "soy sauce",
                        "sesame oil", "red pepper flakes"],
        "level_of_difficulty": "Easy",
        "cooking_time": "25 minutes",
        "instructions": "1. Cook brown rice according to package instructions. \n"
                        "2. Chop broccoli, carrots, snap peas, and mushrooms. \n"
                        "3. In a large pan or wok, sauté garlic in sesame oil for 1-2 minutes. \n"
                        "4. Add vegetables and stir fry for 5-7 minutes, until tender but still crisp. \n"
                        "5. Add soy sauce and red pepper flakes to taste. \n"
                        "6. Serve stir fry over brown rice."
    },
    {
        "name": "Greek Salad",
        "calories": 250,
        "ingredients": ["romaine lettuce", "cucumber", "cherry tomatoes", "kalamata olives", "feta cheese",
                        "red onion", "olive oil", "red wine vinegar", "oregano", "salt", "pepper"],
        "level_of_difficulty": "Easy",
        "cooking_time": "15 minutes",
        "instructions": "1. Chop romaine lettuce and dice cucumber, cherry tomatoes, and red onion. \n"
                        "2. In a large bowl, mix together lettuce, vegetables, kalamata olives, and feta cheese. \n"
                        "3. In a separate bowl, whisk together olive oil, red wine vinegar, oregano, salt, and pepper "
                        "to make the dressing. \n"
                        "4. Pour dressing over salad and toss to combine."
    },
    {
        "name": "Tuna and White Bean Salad",
        "calories": 320,
        "ingredients": ["canned tuna", "canned white beans", "red onion", "cherry tomatoes", "olive oil",
                        "lemon juice", "dijon mustard", "garlic powder", "salt", "pepper", "mixed greens"],
        "level_of_difficulty": "Easy",
        "cooking_time": "15 minutes",
        "instructions": "1. Drain and rinse canned tuna and white beans. \n"
                        "2. Dice red onion and halve cherry tomatoes. \n"
                        "3. In a small bowl, whisk together olive oil, lemon juice, dijon mustard, garlic powder, "
                        "salt, and pepper to make the dressing. \n"
                        "4. In a large bowl, mix together tuna, white beans, red onion, and cherry tomatoes. \n"
                        "5. Pour dressing over tuna mixture and toss to combine. \n"
                        "6. Serve over a bed of mixed greens."
    },
    {
        "name": "Roasted Vegetable Wrap",
        "calories": 380,
        "ingredients": ["whole wheat wrap", "zucchini", "red bell pepper", "red onion", "eggplant", "hummus",
                        "arugula"],
        "level_of_difficulty": "Medium",
        "cooking_time": "35 minutes",
        "instructions": "1. Preheat oven to 400°F. \n"
                        "2. Slice zucchini, red bell pepper, red onion, and eggplant into thin strips. \n"
                        "3. Toss vegetables in olive oil and roast on a baking sheet for 20-25 minutes, "
                        "until tender and slightly browned. \n"
                        "4. Lay out whole wheat wrap and spread hummus on top. \n"
                        "5. Add roasted vegetables and arugula. \n"
                        "6. Roll up wrap tightly and slice in half."
    },
    {
        "name": "Mediterranean Pasta Salad",
        "calories": 360,
        "ingredients": ["whole wheat pasta", "cucumber", "cherry tomatoes", "kalamata olives", "feta cheese",
                        "red onion", "olive oil", "red wine vinegar", "dried oregano", "salt", "pepper"],
        "level_of_difficulty": "Easy",
        "cooking_time": "20 minutes",
        "instructions": "1. Cook whole wheat pasta according to package instructions. \n"
                        "2. Dice cucumber and halve cherry tomatoes. \n"
                        "3. In a large bowl, mix together pasta, cucumber, cherry tomatoes, kalamata olives, "
                        "feta cheese, and red onion. \n"
                        "4. In a separate bowl, whisk together olive oil, red wine vinegar, dried oregano, salt, "
                        "and pepper to make the dressing. \n"
                        "5. Pour dressing over pasta salad and toss to combine."
    }
]

Dinner = [
    {
        "name": "Lemon Garlic Baked Salmon",
        "calories": 450,
        "ingredients": [
            "4 salmon fillets",
            "1/4 cup olive oil",
            "4 garlic cloves, minced",
            "2 tbsp lemon juice",
            "2 tbsp fresh parsley, chopped",
            "Salt and pepper to taste"
        ],
        'level of difficulty': "Easy",
        "cooking time": "25 minutes",
        "instructions": "1. Preheat oven to 400°F. \n"
                        "2. In a small bowl, mix olive oil, garlic, lemon juice, parsley, salt, and pepper. \n"
                        "3. Place salmon fillets on a baking sheet and brush the mixture on top. \n"
                        "4. Bake in the preheated oven for 12-15 minutes, or until the salmon is cooked through."
    },
    {
        "name": "Grilled Chicken and Vegetable Kebabs",
        "calories": 350,
        "ingredients": [
            "4 chicken breasts, cut into cubes",
            "1 red onion, cut into chunks",
            "1 red pepper, cut into chunks",
            "1 zucchini, cut into chunks",
            "1/4 cup olive oil",
            "2 tbsp fresh lemon juice",
            "1 tsp dried oregano",
            "Salt and pepper to taste"
        ],
        "level of difficulty": "Medium",
        "cooking time": "30 minutes",
        "instructions": "1. Preheat grill to medium-high heat. \n"
                        "2. In a small bowl, mix olive oil, lemon juice, oregano, salt, and pepper. \n"
                        "3. Thread chicken, onion, red pepper, and zucchini onto skewers. \n"
                        "4. Brush the mixture on top of the kebabs. \n"
                        "5. Grill for 10-12 minutes, or until the chicken is cooked through and the vegetables"
                        " are tender."
    },
    {
        "name": "Turkey Stuffed Bell Peppers",
        "calories": 400,
        "ingredients": [
            "4 bell peppers",
            "1 lb ground turkey",
            "1 onion, chopped",
            "2 garlic cloves, minced",
            "1 cup cooked brown rice",
            "1 cup tomato sauce",
            "1 tsp dried basil",
            "Salt and pepper to taste"
        ],
        "level of difficulty": "Medium",
        "cooking time": "45 minutes",
        "instructions": "1. Preheat oven to 375°F. \n"
                        "2. Cut off the tops of the bell peppers and remove the seeds. \n"
                        "3. In a large skillet, cook the ground turkey, onion, and garlic over medium heat until the "
                        "turkey is no longer pink. \n"
                        "4. Add the cooked brown rice, tomato sauce, basil, salt, and pepper to the skillet "
                        "and stir to combine. \n"
                        "5. Spoon the mixture into the bell peppers. \n"
                        "6. Place the stuffed bell peppers in a baking dish and bake in the preheated "
                        "oven for 30-35 minutes, or until the peppers are tender and the filling is hot."
    },
    {
        "name": "Chickpea Curry",
        "calories": 350,
        "ingredients": [
            "1 can chickpeas",
            "1 onion, chopped",
            "2 garlic cloves, minced",
            "1 tsp ground cumin",
            "1 tsp ground coriander",
            "1 tsp ground turmeric",
            "1/2 tsp chili powder",
            "1 can diced tomatoes",
            "1 cup vegetable broth",
            "Salt and pepper to taste"
        ],
        "level of difficulty": "Easy",
        "cooking time": "30 minutes",
        "instructions": "1. In a large skillet, sauté onion and garlic until softened. \n"
                        "2. Add cumin, coriander, turmeric, and chili powder and stir for about 1 minute. \n"
                        "3. Add chickpeas, diced tomatoes, vegetable broth, salt, and pepper to the skillet. \n"
                        "4. Bring the mixture to a boil and then reduce heat to low. \n"
                        "5. Cover and simmer for 20-25 minutes. Serve hot with rice or naan bread."
    },
    {
        "name": "Roasted Vegetable Fajitas",
        "calories": 300,
        "ingredients": [
            "1 red pepper, sliced",
            "1 green pepper, sliced",
            "1 yellow onion, sliced",
            "1 zucchini, sliced",
            "1 tbsp olive oil",
            "1 tsp chili powder",
            "1/2 tsp ground cumin",
            "1/2 tsp smoked paprika",
            "Salt and pepper to taste",
            "Whole grain tortillas"
        ],
        "level of difficulty": "Easy",
        "cooking time": "30 minutes",
        "instructions": "1. Preheat oven to 400°F. \n"
                        "2. In a large bowl, toss the peppers, onion, zucchini, olive oil, chili powder, "
                        "cumin, smoked paprika, salt, and pepper until well coated. \n"
                        "3. Spread the vegetables out onto a baking sheet and roast in the "
                        "preheated oven for 20-25 minutes, stirring once or twice. \n"
                        "4. Serve the roasted vegetables with whole grain tortillas and "
                        "toppings of your choice, such as salsa, avocado, or Greek yogurt."
    },
    {
        "name": "Garlic Shrimp Stir-Fry",
        "calories": 400,
        "ingredients": [
            "1 lb raw shrimp, peeled and deveined",
            "1 red bell pepper, sliced",
            "1 yellow onion, sliced",
            "2 garlic cloves, minced",
            "2 tbsp olive oil",
            "2 tbsp low-sodium soy sauce",
            "1 tbsp honey",
            "1 tsp cornstarch",
            "1/4 tsp red pepper flakes",
            "Brown rice"
        ],
        "level of difficulty": "Easy",
        "cooking time": "25 minutes",
        "instructions": "1. In a small bowl, whisk together soy sauce, honey, cornstarch, and red pepper flakes. \n"
                        "2. In a large skillet, sauté the garlic in olive oil over medium heat until fragrant. \n"
                        "3. Add the bell pepper and onion to the skillet and stir-fry for about 3-4 minutes, "
                        "or until the vegetables are tender. \n"
                        "4. Add the shrimp to the skillet and stir-fry for 2-3 minutes, or until they "
                        "are pink and cooked through. \n"
                        "5. Pour the sauce into the skillet and stir to coat the shrimp and vegetables. \n"
                        "6. Continue to cook for another minute or two, or until the sauce has thickened. \n"
                        "7. Serve hot over brown rice."
    }
]

# print(random.choice(Breakfast))
