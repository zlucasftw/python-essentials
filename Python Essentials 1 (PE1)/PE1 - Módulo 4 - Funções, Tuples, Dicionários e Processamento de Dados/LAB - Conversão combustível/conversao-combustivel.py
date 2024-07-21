# LAB: Conversão do consumo de combustíve

galons_in_meters = 3.785411784 / 1609.344
galons_in_100km = galons_in_meters * 100000


def liters_100km_to_miles_gallon(liters):
    return galons_in_100km / liters


def miles_gallon_to_liters_100km(miles):
    return galons_in_100km / miles


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
