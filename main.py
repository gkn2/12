game.splash("welcome to my game!")
herosprite = sprites.create(assets.image("""
    duckhero
"""), SpriteKind.player)
herosprite.set_position(10, 10)
controller.move_sprite(herosprite)
herosprite.say_text("move me around the screen")
name = game.ask_for_string("What is your name?")
age = game.ask_for_number("How old are you?")
message = "Good to meet you" + name
herosprite.say_text(message)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

NewFood = sprites.create(assets.image("""burger"""), SpriteKind.food)
NewFood.x = randint(10, 150)
NewFood.y = randint(10, 120)
NewFood1 = sprites.create(assets.image("""pizza"""), SpriteKind.food)
NewFood1.x = randint(10, 150)
NewFood1.y = randint(10, 120)
enemy = sprites.create(assets.image("""ghost"""), SpriteKind.enemy)
enemy.x = randint(10, 150)
enemy.y = randint(10, 120)
enemy.follow(herosprite)
enemy.set_velocity(20, 20)