#Defining the guests using WH40k References cuz I can

shootaz = ["Mork", "Gork", "Ol' One Eye"]
print("Invited to the WAAAAAGH!:", shootaz)

#Replace guest who cant make it to the WAAAAAGH!
cant_make_it = shootaz[1]
print(f"{cant_make_it} Can't make it to da WAAAAAGH!.")
shootaz[1] = "Big Skorcha"
print("Updated shootaz list:", shootaz)

#Add: beginning, middle, end
shootaz.insert(0, "Blaktoof")                 # beginning
shootaz.insert(len(shootaz) // 2, "Gazgrim")  # middle
shootaz.append("Ogruk Gutrekka")                      # end
print("Expanded shootaz list:", shootaz)

#Remove until only two remain
while len(shootaz) > 2:
    removed = shootaz.pop()
    print(f"Sorry, {removed}, Youz not invited to the great WAAAAGH!")

print("Final two shootaz fo da WAAAAGH:", shootaz)
print(f"{shootaz[0]}, See yaz der! Lets git ta Krumpin! WAAAAAGH!")
print(f"{shootaz[1]}, See yaz der! Lets git ta Krumpin! WAAAAAGH!")