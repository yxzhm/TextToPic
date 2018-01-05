import os
import pygame

pygame.init()


def text_to_pic(text, filename):
    font = pygame.font.Font(os.path.join("C:\Windows\Fonts", "simhei.ttf"), 170)
    rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))

    pygame.image.save(rtext, os.path.join("images",filename))


if __name__ == "__main__":
    fh = open('words.txt')
    n = 0
    for line in fh.readlines():
        text_to_pic(line.strip(), str(n) + ".jpg")
        n += 1
