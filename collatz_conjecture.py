import math
from PIL import Image, ImageDraw, ImageFont
import random

maxNumber = 240
terminationNumber = 1
currentNumber = 1
currentIterationNumber = 0

(width, height) = (2500, 2000)
prevColor = (30, 255, 255)

font = ImageFont.truetype("arial.ttf", 7)

target = Image.new("HSV", (width, height), (220, 1, 1))
draw = ImageDraw.Draw(target)

numbers = [(0, 0), (0, 0), (0, 0), (0, 0)]

for i in range(1, maxNumber):
    # prevColor = (prevColor[0] + 1, prevColor[1] - 1, prevColor[2])
    while currentNumber != terminationNumber:
        currentIterationNumber += 1
        xPosition = 0
        lineColor = (0, 255, 255)

        if currentNumber % 2 == 0:
            currentNumber /= 2
            xPosition = currentNumber - 50
            prevColor = (134, 255, 255)
            draw.line(
                ((xPosition, currentNumber), numbers[i - 1]),
                fill=(0, 255, 255),
                width=1,
            )
        else:
            currentNumber = currentNumber * 3 + 1
            xPosition = currentNumber + 50
            prevColor = (0, 255, 255)
            draw.line(
                ((xPosition, currentNumber), numbers[i - 1]),
                fill=(134, 255, 255),
                width=1,
            )

        # draw.line(((xPosition*25, currentNumber), numbers[i - 1]), fill=lineColor, width=1)
        draw.point([xPosition * 15, currentNumber], prevColor)
        numbers.append((xPosition * 15, currentNumber))

    currentNumber = i

# for x in range(len(numbers)):
#     draw.text(numbers[x], f"{numbers[x][1]}", (255,0,255), font=font)

print("The number of iterations is: " + str(currentIterationNumber))

target.convert("RGB").save("rendering/conjecture.png", "PNG")
