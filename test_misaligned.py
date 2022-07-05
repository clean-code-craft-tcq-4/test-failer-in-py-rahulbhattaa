import misaligned
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]  
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


def test_pair_no(major_color,minor_color,expected_pair_no):
    resultant_pair_no=misaligned.get_pair_no_from_colors(major_color,minor_color)
    assert(resultant_pair_no==expected_pair_no)
    
def test_colors_and_pair_no(major_colors,minor_colors,expected_pair_sequence):
    resultant_color_code_manual=misaligned.print_color_map(major_colors,minor_colors)
    assert (resultant_color_code_manual[25]==expected_pair_sequence)

if __name__ == '__main__':
    test_pair_no("White","Blue",3)
    test_pair_no("White","Orange",4)
    test_colors_and_pair_no(major_colors,minor_colors,[25, 'Violet', 'Slate'])
