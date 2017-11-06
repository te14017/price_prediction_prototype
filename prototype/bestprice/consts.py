

PRICE_RANGE_BOUNDARY = {
    'overall': [0.99, 1.99, 3.99],
    'Music & Audio': [0.99, 1.49, 2.99],
}

# percentage of precision for each predict value
PREDICT_CONFIDENCE = {
    'overall': [[53, 26, 13, 8], [27, 45, 19, 9], [18, 25, 38, 19], [14, 15, 23, 48]],
    'Music & Audio': [[76, 9, 6, 9], [28, 54, 16, 2], [7, 32, 35, 26], [16, 16, 20, 48]],
}

CATEGORY_CHOICES = (
    ('Select', 'Select the category'),
    ('Action', 'Action(Game)'),
    ('Adventure', 'Adventure(Game)'),
    ('Arcade', 'Arcade(Game)'),
    ('Board', 'Board(Game)'),
    ('Books & Reference', 'Books & Reference'),
    ('Business', 'Business'),
    ('Card', 'Card(Game)'),
    ('Casual', 'Casual(Game)'),
    ('Communication', 'Communication'),
    ('Education', 'Education'),
    ('Educational', 'Educational(Game)'),
    ('Entertainment', 'Entertainment'),
    ('Finance', 'Finance'),
    ('Health & Fitness', 'Health & Fitness'),
    ('Lifestyle', 'Lifestyle'),
    ('Maps & Navigation', 'Maps & Navigation'),
    ('Medical', 'Medical'),
    ('Music & Audio', 'Music & Audio'),
    ('Personalization', 'Personalization'),
    ('Photography', 'Photography'),
    ('Productivity', 'Productivity'),
    ('Puzzle', 'Puzzle(Game)'),
    ('Racing', 'Racing(Game)'),
    ('Role Playing', 'Role Playing(Game)'),
    ('Simulation', 'Simulation(Game)'),
    ('Social', 'Social'),
    ('Sports', 'Sports(Game)'),
    ('Strategy', 'Strategy(Game)'),
    ('Tools', 'Tools'),
    ('Travel & Local', 'Travel & Local'),
    ('Video Players & Editors', 'Video Players & Editors'),
    ('Weather', 'Weather'),
)

IN_APP_PURCHASE_CHOICES = (
    ('Select', 'Select if with in-App purchase'),
    ('with', 'with in-App purchase'),
    ('without', 'without in-App purchase'),
)

CONTENT_RATING_CHOICES = (
    ('Select', 'Select content rating'),
    ('Everyone', 'Everyone'),
    ('Everyone 10+', 'Everyone 10+'),
    ('Teen', 'Teen'),
    ('Mature 17+', 'Mature 17+'),
    ('Unrated', 'Unrated'),
)

RANKING_CHOICES = (
    ('Select', 'Select ranking status(if you have)'),
    ('Top_ranked', 'Top_ranked'),
    ('Highly_ranked', 'Highly_ranked'),
    ('Medium_ranked', 'Medium_ranked'),
    ('Unranked', 'Unranked'),
)

INSTALLS_CHOICES = (
    ('Select', 'Select installs range(if you have)'),
    ('1 - 5', '1 - 5'),
    ('5 - 10', '5 - 10'),
    ('10 - 50', '10 - 50'),
    ('50 - 100', '50 - 100'),
    ('100 - 500', '100 - 500'),
    ('500 - 1,000', '500 - 1,000'),
    ('1,000 - 5,000', '1,000 - 5,000'),
    ('5,000 - 10,000', '5,000 - 10,000'),
    ('10,000 - 50,000', '10,000 - 50,000'),
    ('50,000 - 100,000', '50,000 - 100,000'),
    ('100,000 - 500,000', '100,000 - 500,000'),
    ('500,000 - 1,000,000', '500,000 - 1,000,000'),
    ('1,000,000 - 5,000,000', '1,000,000 - 5,000,000'),
    ('10,000,000 - 50,000,000', '10,000,000 - 50,000,000'),
)
