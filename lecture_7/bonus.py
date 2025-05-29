import random
import а.pyplot as plt
n = int(input("Введіть кількість кроків: "))
x = 0
y = 0

path = [(x, y)]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  

for _ in range(n):
    dx, dy = random.choice(directions)
    x += dx
    y += dy
    path.append((x, y))

x_coords, y_coords = zip(*path)

print("Кінцева позиція:", (x, y))
distance = (x**2 + y**2)**0.5
print("Відстань від початкової точки:", round(distance, 2))

plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords)
plt.plot(0, 0)
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()
