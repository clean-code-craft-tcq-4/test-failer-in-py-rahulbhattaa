
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
color_code_manual=[]

def get_pair_no_from_colors(major_color,minor_color):
    major_index = major_colors.index(major_color)
    minor_index = minor_colors.index(minor_color)
    return major_index * len(minor_colors) + minor_index + 1


def print_color_map(major_colors,minor_colors):   
    for i, major_col in enumerate(major_colors):
        for j, minor_col in enumerate(minor_colors):
         color_code_manual.append([i * 5 + j + 1 ,major_col,minor_col])   
    return color_code_manual
