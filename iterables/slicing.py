import math
def split_list(orig_list):
    size = len(orig_list)
    end = math.ceil(size/2)
    start_2 = end 
    part_1 = orig_list[0:end]
    part_2 = orig_list[start_2:size]
    return (part_1, part_2)

def main():
    colors = ["red", "blue", "green", "orange", "purple"] 
    colors_split = split_list(colors)
    print(colors_split[0]) 
    print(colors_split[1]) 


main()

