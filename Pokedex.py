import mysql.connector

# Connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",         
        user="root",             
        password="",             
        database="pokedex_db"     
    )

def PokeEntry(pokemon_id, name, type, hp, attack, defense, sp_attack, sp_defense, speed):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = """
    INSERT INTO Pokedex (id, name, type, hp, attack, defense, sp_attack, sp_defense, speed)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, (pokemon_id, name, type, hp, attack, defense, sp_attack, sp_defense, speed))
        connection.commit()
        print(f"Pokémon {name} (ID: {pokemon_id}) has been added to the Pokedex!")
    finally:
        cursor.close()
        connection.close()

def GetPoke(pokemon_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "SELECT * FROM pokedex_info WHERE id = %s"
    cursor.execute(query, (pokemon_id))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if result:
        print(f"ID: {result[0]}\nName: {result[1]}\nType: {result[2]}\nHP: {result[3]}\nAttack: {result[4]}\nDefense: {result[5]}\nSp. Attack: {result[6]}\nSp. Defense: {result[7]}\nSpeed: {result[8]}")
    else:
        print("No Pokémon found with that PokeID.")

def main():
    while True:
        print("\nDex Home")
        print("1. Add a Pokémon")
        print("2. View Pokémon by PokeID")
        print("3. Exit")
        
        Input = input("Select an option(1/2/3): ")
        
        if Input == "1":
            pokemon_id = int(input("Enter Pokémon ID: "))
            name = input("Enter Pokémon name: ")
            p_type = input("Enter Pokémon type: ")
            hp = int(input("Enter HP: "))
            attack = int(input("Enter Attack: "))
            defense = int(input("Enter Defense: "))
            sp_attack = int(input("Enter Sp. Attack: "))
            sp_defense = int(input("Enter Sp. Defense: "))
            speed = int(input("Enter Speed: "))
            PokeEntry(pokemon_id, name, p_type, hp, attack, defense, sp_attack, sp_defense, speed)
        
        elif Input == "2":
            pokemon_id = int(input("Enter Pokémon ID to check: "))
            GetPoke(pokemon_id)
        
        elif Input == "3":
            print("Exiting Pokemon Pokedex !!")
            break
        
        else:
            print("No Pokemon Found. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
