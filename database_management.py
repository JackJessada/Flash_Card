import sqlite3
#Function to get all deck name in a db
def get_table_names():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result
# Function to counter all flashcard in a specific deck
def get_flashcard_count(deck_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''SELECT COUNT(*) FROM {deck_name}''')
    result = c.fetchone()
    conn.commit()
    conn.close()

    if result is not None:
        return result[0]
    else:
        return 0
# Function to change the name of a table
def rename_table(old_table_name, new_table_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''ALTER TABLE {old_table_name} RENAME TO {new_table_name}''')
    conn.commit()
    conn.close()
# Function to count rows with weight greater than or equal to 0
def count_rows_with_weight(deck_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''SELECT COUNT(*) FROM {deck_name} WHERE weight >= 0''')
    result = c.fetchone()
    conn.commit()
    conn.close()

    if result is not None:
        return result[0]
    else:
        return 0
# Function to reset the weight of flashcards in a specific deck
def reset_weight(deck_name,weight=-10):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''UPDATE {deck_name} SET weight={weight}''')
    conn.commit()
    conn.close()
# Function to counter all flashcard in a specific deck
def get_flashcard_count(deck_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''SELECT COUNT(*) FROM {deck_name}''')
    result = c.fetchone()
    conn.commit()
    conn.close()
    if result is not None:
        return result[0]
    else:
        return 0
# Function to add a flashcard to a specific deck
def add_flashcard(deck_name, front_card, back_card, front_card_type="text", back_card_type="text", weight=-10):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''INSERT INTO {deck_name} (front_card, back_card, front_card_type, back_card_type, weight)
                VALUES (?, ?, ?, ?, ?)''', (front_card, back_card, front_card_type, back_card_type, weight))
    conn.commit()
    conn.close()

# Function to edit a flashcard in a specific deck
def edit_flashcard(deck_name, flashcard_id, front_card, back_card, front_card_type, back_card_type,weight):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''UPDATE {deck_name} SET front_card=?, back_card=?, front_card_type=?, back_card_type=?,weight=?
                WHERE id=?''', (front_card, back_card, front_card_type, back_card_type,weight ,flashcard_id))
    conn.commit()
    conn.close()

# Function to delete a flashcard table
def delete_flashcard_table(deck_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''DROP TABLE IF EXISTS {deck_name}''')
    conn.commit()
    conn.close()

# Function to delete a flashcard from a deck
def delete_flashcard(deck_name, flashcard_id):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''DELETE FROM {deck_name} WHERE id=?''', (flashcard_id,))
    conn.commit()
    conn.close()

# Function to query all rows and columns from a table
def query_all_rows(deck_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''SELECT * FROM {deck_name}''')
    rows = c.fetchall()
    conn.close()

    return rows

# Function to create a new flashcard table
def create_flashcard_table(deck_name):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS {deck_name} (
                    id INTEGER PRIMARY KEY,
                    front_card TEXT,
                    back_card TEXT,
                    front_card_type TEXT,
                    back_card_type TEXT,
                    weight INTEGER
                )''')
    conn.commit()
    conn.close()

def reset_flash_card_weight(deck_name,weight=-10):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute(f'''UPDATE {deck_name} SET weight={weight}''')
    
    conn.commit()
    conn.close()
