# "Evnirement veriables"

DBname = "Coffee.db"


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


AllValues = {
    "Bean": ["bean_name", "species"],
    "Farm": ["farm_name", "country", "region", "height"],
    "Roastery": ["roastery_name", "region", "country"],
    "Process": ["process_name", "description"],
    "User": ["user_email", "first_name", "last_name", "password"],
    "Batch": ["farm_ID", "bean_ID", "process_ID", "harvestYear", "kg_price_usd"],
    "Coffee": ["batch_ID", "roastery_ID", "coffee_name", "roast_degree", "kg_price_kr", "coffee_description", "roast_date"],
    "Contains": ["bean_ID", "batch_ID"],
    "Produses_Bean": ["bean_ID", "farm_ID"],
    "Evaluation": ["coffee_ID", "user_ID",
                   "points", "evalutation_date", "user_notes"]

}
