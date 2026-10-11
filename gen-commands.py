import json, sys
PLAYER = "Crispybaobun"
def lerp(stops, t):
    x = t * (len(stops) - 1); i = min(int(x), len(stops) - 2); f = x - i
    a = [int(stops[i][k:k+2], 16) for k in (1, 3, 5)]; b = [int(stops[i+1][k:k+2], 16) for k in (1, 3, 5)]
    return "#" + "".join(f"{round(a[k] + (b[k] - a[k]) * f):02X}" for k in range(3))
def name(text, font, stops=None, colors=None, override=None):
    letters = [c for c in text if c != " "]; out = []; n = 0
    for c in text:
        part = {"text": c, "italic": False, "font": font}
        if c != " ":
            col = colors[n] if colors else lerp(stops, n / max(len(letters) - 1, 1))
            part["color"] = (override or {}).get(n, col); n += 1
        out.append(part)
    return out
tidal = ["#4F8DFF","#6CA7FF","#8CC4FF","#B4DCFA","#E6F0F5","#FFD6E4","#FF9EC4","#FF86A8","#FF9A6B","#FF8A2B"]
blind = ["#3A4FA8","#3F62BF","#4478D6","#4A90EA","#58ABF5","#E6FDFF","#8FE6FF","#62C8FA","#4FA8EE","#4688DD","#3F6DC8","#3A58B3","#36499F","#34429A"]
items = [
 ("Fortune pickaxe", name("Tidal Elegy", "tidal:metamorphous", colors=tidal)),
 ("Silk Touch pickaxe", name("Blind Obsession", "tidal:pirata_one", colors=blind)),
 ("Sword", name("Ardor Blossom Star", "tidal:berkshire_swash", ["#B3261E","#FF6A1A","#FFC94D","#FFF3C4"])),
 ("Elytra", name("Wingbeat", "tidal:metamorphous", ["#6FD6C8","#BDF3EA","#FFFFFF"])),
 ("Axe", name("Christmas Nightmare", "tidal:mountains_of_christmas", ["#2E8B57","#C21F2B"], override={9: "#F2F8FF"})),
 ("Shovel", name("Bygone Days", "tidal:metamorphous", ["#8C6A45","#C9A66B","#E8D9B0"])),
 ("Helmet", name("Capote", "tidal:new_rocker", ["#D7263D","#D6336C","#F2B134"])),
 ("Chestplate", name("Roseate Desire", "tidal:metamorphous", ["#FFB3D1","#F0609E","#A31D4F"])),
 ("Leggings", name("Snagharpoon", "tidal:pirata_one", ["#C8A873","#9AA3AD","#6F7B87"])),
 ("Boots", name("Hundred-Footed Death Maggot", "tidal:new_rocker", ["#C9D94A","#8FA832","#A32626"])),
 ("Mace", name("Hearse", "tidal:pirata_one", ["#F2EFE6","#8A8F98"])),
]
print("Hold the item in your main hand, then paste its line into the SERVER CONSOLE (no leading slash).")
print("Each command only changes the item's name; enchantments and durability are kept.\n")
for label, comps in items:
    mod = {"type": "minecraft:set_name", "target": "custom_name", "name": comps}
    print(f"# {label}: {''.join(c['text'] for c in comps)}")
    print(f"item modify entity {PLAYER} weapon.mainhand {json.dumps(mod, separators=(',', ':'))}\n")
