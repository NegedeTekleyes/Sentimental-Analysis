body_parts = ("head","sholder","knee","toe")
# swap the forst and last elements
swapped = (body_parts[-1],)+ body_parts[1:-1] + (body_parts[0],)

# replace the second element with "elbow"
replaced = (swapped[0], "elbow") + swapped[2:]

# add fingure at the end
final_tuple = replaced + ("fingure",)

# print the final result
print(final_tuple)