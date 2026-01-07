def energy_injoules()->int:
    """This faction take mass's figure from the user and will calculate energy and return it i joules"""
    m = int(input("m: ")) # mass quantity in kilogram
    c = 300000000
    return f"E: {m*(c**2)}"

output = print(energy_injoules())