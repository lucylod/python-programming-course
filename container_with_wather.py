import matplotlib.pyplot as plt

def max_container(height):
    left=0
    right= len(height)-1
    max_area=0
    max_left= left
    max_right = right

    while left < right:
        width = right-left
        h = min(height[left],height[right])
        area= width * h
        
       

        if area > max_area:
            max_area=area
            max_left=left
            max_right=right


        if height[left]<height[right]:
            left +=1
        else:
            right -=1

    return max_area, max_left, max_right

def plot_container(height, left, right, area=None):
    """
    Zeichnet die vertikalen Linien als Balken.
    Hebt die beiden besten Linien hervor und zeichnet das Wasser als Rechteck.
    """

    n=len(height)
    x=list(range(n))

    water_height=min(height[left],height[right])
    water_width=right-left

    if area is None:
        area=water_width*water_height


    plt.figure(figsize=(10,4))

    plt.bar(x,height)
    plt.bar([left,right],[height[left], height[right]])
    

    plt.fill_between([left, right], 0, water_height, alpha=0.3)

    plt.title(f"Container With Most Water | max area = {area} (left={left}, right={right})")
    plt.xlabel("Index")
    plt.ylabel("Height")

    # Hilfslinien und Anzeige
    plt.grid(True, axis="y", alpha=0.3)
    plt.show()

eingabe = input("Gib die Höhen als Komma-separierte Zahlen ein (z.B. 1,8,6,2,5,4,8,3,7):")  
height=[int(x.strip()) for x in eingabe.split(",")]


area, l, r = max_container(height)
print("Maximle Fläche:", area)
print("Bestes Paar:", (l,r))


plot_container(height, l, r, area)










