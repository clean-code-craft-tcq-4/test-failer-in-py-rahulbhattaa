
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

def format_color_code_manual(pair_number,major_color,minor_color):
    return f'{pair_number}|{major_color}|{minor_color}'

def test_pair_no(major_color,minor_color,expected_pair_no):
    resultant_pair_no=get_pair_no_from_colors(major_color,minor_color)
    assert(resultant_pair_no==expected_pair_no)
    
def test_colors_and_pair_no(major_colors,minor_colors,expected_pair_sequence):
    resultant_color_code_manual=print_color_map(major_colors,minor_colors)
    assert (resultant_color_code_manual[24]==expected_pair_sequence)

if __name__ == '__main__':
    test_pair_no("White","Blue",1)
    test_pair_no("White","Orange",2)
    test_colors_and_pair_no(major_colors,minor_colors,[25, 'Violet', 'Slate'])
