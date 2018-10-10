#PF-Prac-38
def build_index_grid(rows, columns):
    result = []
    for row in range (rows):
        tmp = []
        for col in range (columns):
            tmp.append(str(row)+","+str(col))
        result.append(tmp)
    return result

rows=6
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)