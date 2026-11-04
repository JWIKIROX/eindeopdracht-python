# Producten en prijzen
product_1 = "Laptop"
prijs_1 = 899.99
aantal_1 = 5

product_2 = "Muis"
prijs_2 = 24.99
aantal_2 = 10

product_3 = "Toetsenbord"
prijs_3 = 49.99
aantal_3 = 7

# Bereken de totale omzet per product
omzet_1 = prijs_1 * aantal_1
omzet_2 = prijs_2 * aantal_2
omzet_3 = prijs_3 * aantal_3

# Bereken de totale omzet van de winkel
totale_omzet = omzet_1 + omzet_2 + omzet_3

# Print de productinformatie
print("=== Winkeloverzicht ===")

print(f"Product: {product_1}")
print(f"Prijs: €{prijs_1}")
print(f"Aantal verkocht: {aantal_1}")
print()

print(f"Product: {product_2}")
print(f"Prijs: €{prijs_2}")
print(f"Aantal verkocht: {aantal_2}")
print()

print(f"Product: {product_3}")
print(f"Prijs: €{prijs_3}")
print(f"Aantal verkocht: {aantal_3}")
print()

# Print de totale omzet
print("=======================")
print(f"Totale omzet: €{totale_omzet:.2f}")
