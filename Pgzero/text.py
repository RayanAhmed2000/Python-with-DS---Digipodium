import pgzrun


def draw():
    screen.draw.text("Text color", (50, 30), color="orange")
    screen.draw.text("Font name and size", (20, 100),fontsize=60)
    screen.draw.text("Positioned text", topright=(840, 20))
    screen.draw.text("Allow me to demonstrate wrapped text.", (90, 210), width=180, lineheight=1.5)
    screen.draw.text("Outlined text", (400, 70), owidth=1.5, ocolor=(255,255,0), color=(0,0,0))
    screen.draw.text("Drop shadow", (640, 110), shadow=(2,2), scolor="#202020")
    screen.draw.text("Color gradient", (540, 170), color="red", gcolor="purple")
    screen.draw.text("Transparency", (700, 240), alpha=0.1)

pgzrun.go()
