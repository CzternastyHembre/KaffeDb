-- SQLite
CREATE TABLE Bean(
    bean_ID INTEGER PRIMARY KEY,
    bean_name TEXT,
    species TEXT
);

CREATE TABLE Farm(
    farm_ID INTEGER PRIMARY KEY,
    farm_name TEXT,
    country TEXT,
    region TEXT,
    heigth INTEGER
    );


CREATE TABLE Produses_Bean(
    bean_ID INTEGER,
    farm_ID INTEGER,

    PRIMARY KEY (farm_ID, bean_ID)

    FOREIGN KEY (farm_ID) 
        REFERENCES Farm (farm_ID) ON DELETE CASCADE,
    FOREIGN KEY(bean_ID)
        REFERENCES Bean (bean_ID) ON DELETE CASCADE
);

CREATE TABLE Process(
    process_ID INTEGER PRIMARY KEY,
    process_name TEXT,
    description TEXT
);

CREATE TABLE Batch(
    batch_ID INTEGER PRIMARY KEY,
    harvestYear INTEGER,
    farm_ID INTEGER NOT NULL,
    bean_ID INT NOT NULL,
    kg_price_usd REAL,
    process_ID INT NOT NULL,
    FOREIGN KEY(bean_ID) REFERENCES Bean(bean_ID) ON DELETE CASCADE,
    FOREIGN KEY(farm_ID) REFERENCES Farm(farm_ID) ON DELETE CASCADE,
    FOREIGN KEY(process_ID) REFERENCES Process(process_ID) ON DELETE CASCADE
);

CREATE TABLE Contains (
    bean_ID INTEGER,
    batch_ID INTEGER,
    PRIMARY KEY(bean_ID, batch_ID)

    FOREIGN KEY (batch_ID) 
        REFERENCES Farm (batch_ID) ON DELETE CASCADE,
    FOREIGN KEY(bean_ID)
        REFERENCES Bean (bean_ID) ON DELETE CASCADE
);


CREATE TABLE Roastery(
    roastery_ID INT PRIMARY KEY,
    roastery_name TEXT,
    region TEXT,
    country TEXT
);

CREATE TABLE Coffee(
    coffee_ID INTEGER PRIMARY KEY,
    coffee_name TEXT,
    roast_degree TEXT,
    kg_price_kr INTEGER,
    coffee_description TEXT,
    roast_date TEXT,
    batch_ID INTEGER NOT NULL,
    roastery_ID INTEGER NOT NULL,
    FOREIGN KEY(batch_ID) REFERENCES Batch(batch_ID) ON DELETE CASCADE,
    FOREIGN KEY(roastery_ID) REFERENCES Roastery(roastery_ID) ON DELETE CASCADE
);

CREATE TABLE User(
    user_email TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    password TEXT
);
CREATE TABLE Evaluation (
    evaluation_ID INTEGER PRIMARY KEY,
    coffee_ID INTEGER NOT NULL,
    user_email TEXT NOT NULL,
    points INTEGER,
    evalutation_date TEXT,
    user_notes TEXT,
    CONSTRAINT evaluation_ID
        FOREIGN KEY (coffee_ID) 
            REFERENCES Coffee (coffee_ID),
    CONSTRAINT evaluation_ID
        FOREIGN KEY (user_email) 
            REFERENCES User (user_email)
);

