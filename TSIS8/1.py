import pygame
import random

pygame.init()
pygame.font.init()


speed = 6
clock = pygame.time.Clock()
FPS = 20
coin = 0

coin_font = pygame.font.SysFont('Calibri', 28, False, False)


class Red_block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.y += 1

        # If block is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.rect.y = random.randrange(-310, -25)
            self.rect.x = random.randrange(0, 695)


class Green_block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.y += random.randint(-1, 2)

        if self.rect.y > 410:
            self.rect.y = random.randrange(-310, -25)
            self.rect.x = random.randrange(0, 695)


class Player(Red_block):

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= speed
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += speed
        elif key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.y -= speed
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.y += speed


screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('*hungry lion')


# This is a list of every sprite. All blocks and the player block as well.
all = pygame.sprite.Group()
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
no_eat = pygame.sprite.Group()
eat = pygame.sprite.Group()

# Create a red player block
player = Player(pygame.Color('blue'), 20, 15)
all.add(player)

for i in range(60):
    # This represents a block
    no_eaten = Red_block(pygame.Color('red'), 20, 15)
    eaten = Green_block(pygame.Color('green'), 20, 15)

    # Set a random location for the block
    no_eaten.rect.x = random.randrange(700)
    no_eaten.rect.y = random.randrange(400)

    eaten.rect.x = random.randrange(700)
    eaten.rect.y = random.randrange(400)

    # Add the block to the list of objects
    no_eat.add(no_eaten)
    eat.add(eaten)
    all.add(no_eaten)
    all.add(eaten)

# Used to manage how fast the screen updates

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = not done
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = not done

    # Clear the screen
    screen.fill(pygame.Color('white'))
    render_coin = coin_font.render(f'COINS: {coin}', False, pygame.Color('violet'))
    screen.blit(render_coin, (5, 5))
    # Calls update() method on every sprite in the list
    all.update()

    # See if the player block has collided with anything.
    blocks_no = pygame.sprite.spritecollide(player, no_eat, True)
    blocks_eaten = pygame.sprite.spritecollide(player, eat, True)

    # Check the list of collisions.
    for no_eaten in blocks_no:
        coin -= 1
    for no_eaten in blocks_eaten:
        coin += 1

    # Draw all the spites
    all.draw(screen)

    # Limit to 20 frames per second
    clock.tick(FPS)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

pygame.quit()
