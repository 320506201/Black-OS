from ursina import * # type: ignore
app = Ursina()

ground = Entity(model='plane', scale=128, texture='grass', collider='box')

app.run()
