#Define nums. its getting harder and harder to come up with witty stuff to say here.
nums = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

#creates the set and tracks the dupes
seen = set()
dupes = []
added = set()

#IF-ELSE; creates the conditionals
for n in nums:
    if n in seen and n not in added:
        dupes.append(n)
        added.add(n)
    else:
        seen.add(n)

#prints the duplicates
print("output_list =", dupes)