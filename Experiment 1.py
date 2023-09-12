# Write a Program To Solve Different set Opertion using Python

'''# Method 1
A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}
#Union
union = A.union(B)
print("Union of A and B is:", union)
#intersection
intersection = A.intersection(B)
print("Intersection of A and B is:", intersection)
#difference
difference = A.difference(B)
print("Difference of A and B is:", difference)
#symmetric_difference
symmetric_difference= A.symmetric_difference(B)
print("SymmetricDifference of A and B is:", symmetric_difference)'''


#Method 2
A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}
# union
print("Union of A and B :", A | B)
  
# intersection
print("Intersection of A and B:", A & B)
  
# difference
print("Difference of A and B:", A - B)
  
# symmetric difference
print("Symmetric difference of A and B:", A ^ B)