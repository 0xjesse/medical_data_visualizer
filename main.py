# This entrypoint file to be used in development. Start by reading README.md
from unittest import main

import medical_data_visualizer

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)