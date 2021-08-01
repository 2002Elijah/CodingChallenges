def square_areas_difference(radius):
    #Area(Square) = (side length) ^ 2

    #For the Large square the radius of the circle will be equal
    #To half the length of one side
    #Double that value to get one side length
    #A(Large) = 2r^2

    #Area(Square) can also be found through the diagonal
    #For the Small square the radius of the circle will be equal
    #To half the length of one of the diagonals
    #A(Small) = 1/2 * (diameter) ^ 2
    AreaLargeSquare = (2 * radius) ** 2
    diameter = 2 * radius
    dSquared = diameter ** 2
    AreaSmallSquare = (1/2) * (dSquared)
    difference = AreaLargeSquare - AreaSmallSquare
    
    return difference
