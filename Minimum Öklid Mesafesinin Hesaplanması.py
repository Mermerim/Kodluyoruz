import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaları tanımlayan liste
points = [(1, 2), (4, 6), (5, 1), (7, 3), (2, 8)]

# Mesafeleri saklayacak liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul
min_distance = min(distances)

# Sonucu yazdır
print(f'İki nokta arasındaki minimum Öklid mesafesi: {min_distance}')
