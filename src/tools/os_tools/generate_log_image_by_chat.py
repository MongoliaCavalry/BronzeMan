#/usr/bin env python3
#!codeing=utf-8



def generate_char_code_image(code_project_name, width=80, height=20):
    """
    Generate a character image with the software name on the left, an Apple-like logo on the right, and a border.

    Parameters:
    - software_name (str): The name of the software to be displayed on the left.
    - width (int): The width of the image in characters.
    - height (int): The height of the image in characters.

    Returns:
    - None
    """
    
    logo = [
        "        !I$$$$$$$$$$$$I~          ",
        "     \"#$$$$$$$$$$$$$$$$$$$$R!     ",
        "   ~K$$$&*K$$$$$$$$$$$$K*&$$$&'   ",
        "  Y$$$$$>                \"$$$$$*  ",
        " /$$$$$#~                '#$$$$$i  ",
        " #$$$$#                    R$$$$K  ",
        "$$$$$E                    #$$$$E  ",
        " *$$$$$&                  F$$$$$*  ",
        " 'E$$$$$$l'            'l$$$$$$E'  ",
        "   l$$$\">E$$$+      >$$$$$$$$$]    ",
        "    !#$$/            $$$$$$$#!     ",
        "       ~I$$$$'      '$$$$I~        "
    ]

    streams = []
    
    # Calculate the number of lines to pad above and below the logo
    pad_height = (height - len(logo) - 2) // 2  # Subtracting 2 for the top and bottom borders

    for i in range(height):
        if i == 0 or i == height - 1:  # Top or bottom border
            line  = "*" * width
            streams.append(line)
            continue

        if i == height // 2:  # Middle line where software name is displayed
            p = " <------ "
            space_before_name = (width - len(code_project_name) - len(p) - len(logo[0]) - 2) // 2  # Subtracting 2 for the left and right borders
            space_after_name = width - len(code_project_name) - len(p) - len(logo[0]) - 2 - space_before_name
            line = "*" + " " * space_before_name + code_project_name + p + " " * space_after_name + logo[i - pad_height - 1] + "*"
            streams.append(line)
            continue

        if i < pad_height + 1 or i >= pad_height + len(logo) + 1:  # Adding 1 to account for the top border
            logo_line = " " * len(logo[0])
        else:
            logo_line = logo[i - pad_height - 1]  # Subtracting 1 to account for the top border

        # Calculate the space between the software name and the logo
        space_between = width - len(logo_line) - 2  # Subtracting 2 for the left and right borders
        line = "*" + " " * space_between + logo_line + "*"
        streams.append(line)
    
    return streams


def generate_char_soft_image(software_name, width=80, height=20):
    """
    Generate a character image with the software name on the left, an Apple-like logo on the right, and a border.

    Parameters:
    - software_name (str): The name of the software to be displayed on the left.
    - width (int): The width of the image in characters.
    - height (int): The height of the image in characters.

    Returns:
    - None
    """
    logo = [
        "                    '}>          ",
        "                 >NMMMi          ",
        "                %MMMN            ",
        "             ~NK],,~!            ",
        "      >MMMMMMMMMMMMMMMMMMMMM&    ",
        "     *MMMMMMMMMMMMMMMMMMMMM*     ",
        "    >MMMMMMMMMMMMMMMMMMMM@       ",
        "    1MMMMMMMMMMMMMMMMMMMM%       ",
        "    ,MMMMMMMMMMMMMMMMMMMMM@~     ",
        "     IMMMMMMMMMMMMMMMMMMMMMM@1   ",
        "      +MMMMMMMMMMMMMMMMMMMMMK    ",
        "       ~@MMMMMMMMMMMMMMMMMMY     ",
        "         lMMMNI'  /#MMM#'        "
    ]

    streams = []
    
    # Calculate the number of lines to pad above and below the logo
    pad_height = (height - len(logo) - 2) // 2  # Subtracting 2 for the top and bottom borders

    for i in range(height):
        if i == 0 or i == height - 1:  # Top or bottom border
            line  = "*" * width
            streams.append(line)
            continue

        if i == height // 2:  # Middle line where software name is displayed
            p = " ------> "
            space_before_name = (width - len(software_name) - len(p) - len(logo[0]) - 2) // 2  # Subtracting 2 for the left and right borders
            space_after_name = width - len(software_name) - len(p) - len(logo[0]) - 2 - space_before_name
            line = "*" + " " * space_before_name + software_name + p + " " * space_after_name + logo[i - pad_height - 1] + "*"
            streams.append(line)
            continue

        if i < pad_height + 1 or i >= pad_height + len(logo) + 1:  # Adding 1 to account for the top border
            logo_line = " " * len(logo[0])
        else:
            logo_line = logo[i - pad_height - 1]  # Subtracting 1 to account for the top border

        # Calculate the space between the software name and the logo
        space_between = width - len(logo_line) - 2  # Subtracting 2 for the left and right borders
        line = "*" + " " * space_between + logo_line + "*"
        streams.append(line)
    
    return streams