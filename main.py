def mirror_upper_star_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


height = int(input("Üçgen yüksekliğini girin: "))
mirror_upper_star_triangle(height)
