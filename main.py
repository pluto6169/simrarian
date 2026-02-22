import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

class Library:
    def __init__(self):
        self.books = []  # List of books available in the library

    def add_book(self, book_name):
        self.books.append(book_name)

    def display_books(self):
        return '\n'.join(self.books)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Library Management Simulation')
        self.clock = pygame.time.Clock()
        self.library = Library()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Limit frame rate to 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass  # Here you can add game logic updates

    def render(self):
        self.screen.fill(WHITE)  # Clear the screen with white
        pygame.display.flip()  # Update the full display Surface to the screen

if __name__ == '__main__':
    game = Game()
    game.run()