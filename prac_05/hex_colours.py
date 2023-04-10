COLORS = {"Amber": "#ffbf00", "Beige": "#f5f5dc", "Chocolate": "#d2691e", "Emerald": "#50c878", "Gray": "#bebebe",
          "Indigo": "#4b0082", "Lavender": "#e6e6fa", "Olive": "808000", "Purple": "#a020f0", "SkyBlue": "#87ceeb"}
print(COLORS)

picked_color = input("Enter a colour: ").upper()
while picked_color != "":
    if picked_color in COLORS:
        print(COLORS[picked_color])
    else:
        print("Invalid color")
    picked_color = input("Enter a colour: ").upper()
