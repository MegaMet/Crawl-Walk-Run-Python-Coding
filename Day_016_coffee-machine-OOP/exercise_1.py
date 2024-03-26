from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee"])
table.add_column("Pokemon Types", ["Grass / Poison", "Fire", "Water", "Electric", "Normal"])

table.align = "l"

print(table)
