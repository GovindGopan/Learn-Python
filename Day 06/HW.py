blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

x = 0
Trending = 0
Total_views = 0

for x in blog_views:
    Total_views += x
    
    if x > 1000:
        print("Trending")
        Trending += 1
    elif 500 <= x <= 1000:
        print("Average")
    else:
        print("Low Traffic")
    
print("\nTotal views :", Total_views)
print("\nTrending posts :", Trending)