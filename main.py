import pygame
import math
import random

# Initializing PyGame
pygame.init()


# The class that initializes the pygame GUI
class Main:
    # The global constants for the sorting algorithm visualizer
    # The font, colors, margin, and window dimensions
    FONT = pygame.font.SysFont('Arial', 25)
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    SORTING_COLOUR = 255, 81, 81
    X_MARGIN = 120
    Y_MARGIN = 150

    # This function sets the window dimensions
    def __init__(self, width, height, array):
        # Width of the window
        self.width = width

        # Height of the window
        self.height = height

        # Displaying the window with width and height
        self.window = pygame.display.set_mode((width, height))

        # Displaying the title of the window
        pygame.display.set_caption("Sorting Algorithm Visualizer")

        # Setting the array to be sorted
        self.setArray(array)

    # This function sets the bars to be sorted
    def setArray(self, array):
        # The array to be sorted
        self.array = array

        # The minimum and maximum values in the array
        self.minVal = min(array)
        self.maxVal = max(array)

        # The dimensions for each bar depending on the random number generated
        # The width of each bar
        self.barWidth = round(self.width - self.X_MARGIN) / (2 * len(array))

        # The height of each bar
        self.barHeight = math.floor(
            (self.height - self.Y_MARGIN) / (self.maxVal - self.minVal))

        # The starting x position of the first bar
        self.startingX = self.X_MARGIN // 2


# This function draws instructions to the window
def draw(instructions):
    # Printing the instructions with the color BLACK
    instructions.window.fill(instructions.BLACK)

    # Displaying the settings
    menu = instructions.FONT.render(
        "ESC (reset) | SPACE (sort) | A (ascending) | D (descending)", 1, instructions.WHITE)

    # Displaying the sorting algorithms
    algo = instructions.FONT.render(
        "B (bubble) | I (insertion) | S (selection) | M (merge) | Q (quick) | H (heap) | R (radix)", 1, instructions.WHITE)

    # Displaying the settings in a specific position
    instructions.window.blit(
        menu, (instructions.width / 2 - menu.get_width()/2, 25))

    # Displaying the sorting algorithms in a specific position
    instructions.window.blit(
        algo, (instructions.width / 2 - algo.get_width()/2, 70))

    # Displaying the bars to be sorted
    drawBars(instructions, -1, -1)  # Calling the drawBars function

    # Updating the display
    pygame.display.update()


# The function that draws bars
def drawBars(instructions, a, b, c=-1, clear=False):
    array = instructions.array  # Setting the array to be sorted

    if clear:
        # Creating a bar for each number in the array to be sorted
        rect = (instructions.X_MARGIN // 2, instructions.Y_MARGIN, instructions.width -
                instructions.X_MARGIN, instructions.height)
        # Drawing the bars
        pygame.draw.rect(instructions.window, instructions.BLACK, rect)

    # Converting each number in the array to a bar
    for i, val in enumerate(array):
        x = instructions.startingX + (2 * i) * instructions.barWidth
        y = instructions.height - (val - instructions.minVal +
                                   1) * instructions.barHeight
        colour = (255, 255, 255)
        # While sorting, highlight the bars being compared
        if i == a or i == b or i == c:
            # Setting the color of the bars being compared
            colour = instructions.SORTING_COLOUR

        # Drawing each bar
        pygame.draw.rect(instructions.window, colour,
                         (x, y, instructions.barWidth, instructions.height))

    # Updating the display if clear is true
    if clear:
        pygame.display.update()


# This function generates the array of numbers to be sorted
def genArray(n, minVal, maxVal):
    # Initializing an empty array
    array = []

    # Adding a random number to the array
    for i in range(n):
        array.append(random.randint(minVal, maxVal))

    # Returing the array
    return array


"""
ALGORITHMS
"""


# Heap sort algorithm
def heapSort(instructions, ascending):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Iterating through the array
    for i in range(len(array)):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Calling the heapify function
        heapify(instructions, len(array), i, ascending)

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)

    # Iterating through the array
    for i in range(len(array) - 1, 0, -1):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Swapping the elements
        array[i], array[0] = array[0], array[i]

        # Calling the heapify function
        heapify(instructions, i, 0, ascending)

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)


def heapify(instructions, n, i, ascending):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Initializing the largest element
    largest = i

    # Initializing the left and right child
    left = 2 * i + 1
    right = 2 * i + 2

    # If the left child is greater than the largest element
    if left < n and ((ascending and array[i] < array[left]) or (not ascending and array[i] > array[left])):
        # The largest element is the left child
        largest = left

    # If the right child is greater than the largest element
    if right < n and ((ascending and array[largest] < array[right]) or (not ascending and array[largest] > array[right])):
        # The largest element is the right child
        largest = right

    # If the largest element is not the root
    if largest != i:
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Swapping the elements
        array[i], array[largest] = array[largest], array[i]

        # Calling the heapify function
        heapify(instructions, n, largest, ascending)

        # Drawing the bars
        drawBars(instructions, i, largest, -1, True)


# Radix sort algorithm
def radixSort(instructions, ascending):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Finding the maximum number in the array
    maxNum = max(array)

    # Finding the number of digits in the maximum number
    maxDigits = len(str(maxNum))

    # Iterating through the array
    for i in range(maxDigits):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Calling the counting sort function
        countingSort(instructions, i)

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)


def countingSort(instructions, digit):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Initializing the count array
    count = [0] * 10

    # Iterating through the array
    for i in range(len(array)):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Finding the digit at the specified position
        index = (array[i] // (10 ** digit)) % 10

        # Incrementing the count array
        count[index] += 1

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)

    # Iterating through the count array
    for i in range(1, len(count)):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Incrementing the count array
        count[i] += count[i - 1]

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)

    # Initializing the output array
    output = [0] * len(array)

    # Iterating through the array
    for i in range(len(array) - 1, -1, -1):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Finding the digit at the specified position
        index = (array[i] // (10 ** digit)) % 10

        # Decrementing the count array
        count[index] -= 1

        # Setting the output array
        output[count[index]] = array[i]

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)

    # Setting the array to be sorted
    for i in range(len(array)):
        # Setting the speed of the sorting algorithm
        clock.tick(150)

        # Setting the array to be sorted
        array[i] = output[i]

        # Drawing the bars
        drawBars(instructions, i, -1, -1, True)


# Bubble sort algorithm
def bubbleSort(instructions, ascending):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Iterating through the inputed array and comparing adjacent elements
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # Setting the speed of the sorting algorithm
            clock.tick(150)

            # If the algorithm is sorting in ascending order and the current element is greater than the next element
            # or if the algorithm is descending and the current element is less than the next element
            if (ascending and array[i] > array[j]) or (not ascending and array[i] < array[j]):
                # We swap adjacent elements
                array[i], array[j] = array[j], array[i]

            # Drawing the bars
            drawBars(instructions, i, j, -1, True)


# Insertion sort algorithm
def insertionSort(instructions, ascending):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Iterating through the array
    for i in range(len(array)):
        for j in range(i, 0, -1):
            # Setting the speed of the sorting algorithm
            clock.tick(50)

            # Comparing the current element to the element before it
            # If it is smaller, compare it to the element before that
            # Moving larger elements one index up by swapping
            if (ascending and array[j] < array[j - 1]) or (not ascending and array[j] > array[j - 1]):
                array[j], array[j - 1] = array[j - 1], array[j]
            # Drawing the bars
            drawBars(instructions, j, j - 1, -1, True)


# Selection sort algorithm
def selectionSort(instructions, ascending):
    # Initializing the array
    array = instructions.array

    # Initializing the clock
    clock = pygame.time.Clock()

    # Initializing the index of the mininum value to 0
    index = 0

    # Iterating through arrayay to find minimum value
    for i in range(len(array)):
        # Set the index of the minimum value to the current index
        index = i
        for j in range(i, len(array)):
            # Setting the speed of the sorting algorithm
            clock.tick(150)

            # If any element is smaller than the element at index, swap the values
            if (ascending and array[j] < array[index]) or (not ascending and array[j] > array[index]):
                # Updating the index of the minimum value
                index = j

            # Drawing the bars
            drawBars(instructions, index, j, -1, True)
            # Swapping the values
        array[i], array[index] = array[index], array[i]


# Quick sort algorithm
def quickSort(instructions, ascending):
    # Calling the helper function
    quickSortHelper(instructions, ascending, 0, len(instructions.array))


# Function to find the partition position
def quickSortHelper(instructions, ascending, start, end):
    # Initializing the array
    array = instructions.array

    if end <= start:
        return

    # Pointer for the greater element
    pos = end - 1

    # Initializing the clock
    clock = pygame.time.Clock()

    # Iterating through all elements and compare each element with pivot
    for i in range(end - 1, start, -1):
        # Initializing the speed of the algorithm
        clock.tick(150)

        # If the element smaller than the pivot is found, swap it with the greater element being pointed at
        if (ascending and array[i] > array[start]) or (not ascending and array[i] < array[start]):
            # Swapping the elements
            array[pos], array[i] = array[i], array[pos]

            # Updating the position of the greater element
            pos -= 1

        # Drawing the bars
        drawBars(instructions, start, i, pos, True)

        # Swapping the pivot with the greater element
        array[pos], array[start] = array[start], array[pos]

    # A recursive call to the left of pivot
    quickSortHelper(instructions, ascending, start, pos)

    # A recursive call to the right of pivot
    quickSortHelper(instructions, ascending, pos + 1, end)


# mergeSort sort algorithm
def mergeSort(instructions, array, left, right, ascending):
    # Setting the index of the left and right array to 0
    i = j = 0

    # Initializing the clock
    clock = pygame.time.Clock()

    # Iterating through the array
    for pos in range(len(left) + len(right)):
        # Setting the speed of the algorithm
        clock.tick(100)

        # Copying the data to a temporary array
        temp = array

        p1 = p2 = -1
        list1 = True

        # Finding smaller element
        if i == len(left) or (j < len(right) and ((ascending and right[j] < left[i]) or (not ascending and right[j] > left[i]))):
            array[pos] = left[j]
            j += 1
            list1 = False
        else:
            array[pos] = left[i]
            i += 1

        # Iterating through the array
        for k in range(len(array)):
            # If the array of index k is not equal to the temporary array index k
            if array[k] != temp[k]:
                # and if the index of the first element is -1
                if p1 == -1:
                    # Set the index of the first element to k
                    p1 = k
                else:
                    # Set the index of the second element to k
                    p2 = k
        # Drawing the bars
        drawBars(instructions, p1, p2, -1, True)

        # If list 1 is true
        if list1:
            # Increment the value of i by 1
            i += 1
        else:
            # Increment the value of j by 1
            j += 1

    # Return the array
    return array


# Merge sort algorithm
def merge(instructions, array, left, right, ascending, start):
    # Setting the left and right index to 0
    i = j = 0
    # Initializing the clock
    clock = pygame.time.Clock()

    for pos in range(len(left) + len(right)):
        # Setting the speed of the algorithm
        clock.tick(150)

        # Finding the smaller element
        if i == len(left) or (j < len(right) and ((ascending and right[j] < left[i]) or (not ascending and right[j] > left[i]))):
            # Setting the index of the array to the index of the right array
            array[pos] = right[j]

            # Incrementing the value of j by 1
            j += 1

            # Drawing the bars
            drawBars(instructions, pos + start,
                     len(left) + start + j, -1, True)
        else:
            # Setting the index of the array to the index of the left array
            array[pos] = left[i]

            # Drawing the bars
            drawBars(instructions, pos + start, start + i, -1, True)

            # Incrementing the value of i by 1
            i += 1

    # Returning the array
    return array


def mergeSort(instructions, ascending):
    mergeSortHelper(instructions, instructions.array, ascending, 0)


# Function that splits the arrayay into 2 halves and then remerges them
def mergeSortHelper(instructions, array, ascending, start):
    if len(array) == 1:
        return

    # Finds the mid index of the arrayay
    mid = len(array) // 2

    # splicing the array into 2 halves
    left = array[:mid]
    right = array[mid:]

    # Sorting the 1st half
    mergeSortHelper(instructions, left, ascending, start)
    # Sorting the 2nd half
    mergeSortHelper(instructions, right, ascending, start +
                    len(array) // 2)

    # Merge sorting the two halves
    array = merge(instructions, array, left, right, ascending, start)


# ------- MAIN GAME LOOP -------
# Game state (running or not running)
running = True

# The number of elements in an array
n = 40

# Setting the mininum and maximun value in the array
minVal, maxVal = 0, 100

# Sorting state
sorting = False

# Ascending state
ascending = True

# Initializing the clock
clock = pygame.time.Clock()

array = genArray(n, minVal, maxVal)  # generating an array using method
instructions = Main(1200, 680, array)  # Initializing window settings
algorithm = bubbleSort

while running:
    # Setting the speed of the algorithm
    clock.tick(120)
    # Drawing the instrutions
    draw(instructions)
    # Updating the display
    pygame.display.update()

    # If there is an event in pygame
    for event in pygame.event.get():
        # Check if the event is the user closing the window
        if event.type == pygame.QUIT:
            # If it is, quit the game
            running = False
        # If the event is not a key press
        if event.type != pygame.KEYDOWN:
            # Then continue
            continue
        # If the event is pressing down on the escape key
        if event.key == pygame.K_ESCAPE:
            # generate a new unsorted array
            array = genArray(n, minVal, maxVal)
            # Set the array to the instructions
            instructions.setArray(array)
            # Set sorting to false
            sorting = False
        # If the event key is equal to the space bar and sorting is equal to false
        elif event.key == pygame.K_SPACE and sorting == False:
            # Set sorting to true
            sorting = True
            # Run the algorithm
            algorithm(instructions, ascending)

        # The following allows the user to pick between ascending and descending
        elif event.key == pygame.K_a and not sorting:
            ascending = True
        elif event.key == pygame.K_d and not sorting:
            ascending = False

        # The following allows user to pick the sorting algorithm
        elif event.key == pygame.K_b and not sorting:
            algorithm = bubbleSort
        elif event.key == pygame.K_i and not sorting:
            algorithm = insertionSort
        elif event.key == pygame.K_s and not sorting:
            algorithm = selectionSort
        elif event.key == pygame.K_q and not sorting:
            algorithm = quickSort
        elif event.key == pygame.K_m and not sorting:
            algorithm = mergeSort
        elif event.key == pygame.K_h and not sorting:
            algorithm = heapSort
        elif event.key == pygame.K_r and not sorting:
            algorithm = radixSort

pygame.quit()
