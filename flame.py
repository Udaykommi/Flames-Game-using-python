val =list(input("Enter the name 1"))
val2 =list(input("enter the name 2"))
nme = val.copy()
nme2 = val2.copy()
c=0

for i in range(len(nme)):
    print(nme[i])
    for j in range(len(val2)-1):
        if nme[i] == val2[j]:
            val.remove(nme[i])
            nme2.remove(val2[j])
            #print(i, end="")

            c+=1

sma=len(val)
big = len(nme2)
count = sma +big
#print(count)
result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

# keep looping until only one item
# is not remaining in the result list
while len(result) > 1:

    # store that index value from
    # where we have to perform slicing.
    split_index = (count % len(result) - 1)

    # this steps is done for performing
    # anticlock-wise circular fashion counting.
    if split_index >= 0:

        # list slicing
        right = result[split_index + 1:]
        left = result[: split_index]

        # list concatenation
        result = right + left

    else:
        result = result[: len(result) - 1]

# print final result
print("Relationship status :", result[0])
