"""

Normally this is only for colors, but in this case
it also takes in an font without issues.

This code is also in tilux.

"""

from csmpy import ColorSchemeManager
import pyfiglet

# Define values (required)
default_values = {
    # These need to matches with the values inside YAML file
    'logo_color': 'red',
    'logo_font': 'slant',
    'text': 'white',
}

# Load custom colors from the YAML file
custom_colors = ColorSchemeManager.load_custom_yaml_file('example.yaml')
all_values = ColorSchemeManager.load_colors(default_values, custom_colors)

# Without custom values
# all_colors = ColorSchemeManager.load_colors(default_values)

logo_color = all_values['logo_color']
logo_font = all_values['logo_font']

# Otherwise all of the texts after stay red.
back_to_original = all_colors['text']

styled_text=pyfiglet.figlet_format('Example',font= logo_font)
print(f"{logo_color} {styled_text} {back_to_original}")
