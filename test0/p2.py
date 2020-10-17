import math
def compute_distance(x1, y1, x2, y2):
 
    distance = 0
 
    # Complete this function to return Euclidean distance and
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
    # print the distance value with precision up to 2 decimal places
    print("Distance: %.2f"%distance)
 
 
# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    arr =[]
    # Write the code here to take the x1, y1, x2 and y2 values
    for i in range(test_cases):
        x1,y1,x2,y2=map(int,input().split())
        arr.append([x1,y1,x2,y2])
    for i in range(test_cases):
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
        compute_distance(x1, y1, x2, y2)
