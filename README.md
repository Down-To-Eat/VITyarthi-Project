Unit Converter Pro

Converter Pro is a feature-rich command-line application developed as part of the VITyarthi "Build Your Own Project" initiative. This project addresses the common challenge of converting between different measurement units by providing an intuitive, reliable, and comprehensive solution.

The application supports multiple conversion categories, maintains detailed history with timestamps, provides usage analytics, and implements robust error handling—all while maintaining code quality and professional documentation standards.

Name: Divyanshu Verma
Roll NO: 25BCE11090
Course: VITyarthi Build Your Own Project
Academic Year: 2025-2026
Semester: 1
Submission Date: November 24, 2025

Key Features:

Core Conversion Capabilities:

1.	Length Conversion: Supports 8 units including meter, kilometer, centimeter, millimeter, mile, yard, foot, and inch
2.	Temperature Conversion: Seamlessly converts between Celsius, Fahrenheit, and Kelvin scales
3.	Weight Conversion: Handles 6 units including kilogram, gram, milligram, pound, ounce, and ton
4.	Time Conversion: Converts across 7 units from seconds to years

Advanced Features:

1.	Conversion History: Automatically tracks up to 50 recent conversions with precise timestamps
2.	Usage Statistics: Provides detailed analytics on conversion patterns and most-used categories
3.	Data Persistence: Saves history across sessions using JSON storage format
4.	Export Functionality: Allows exporting conversion history to human-readable text files
5.	Comprehensive Logging: Records all application events and errors for debugging and audit purposes
6.	Input Validation: Implements multi-layer validation to ensure data integrity and prevent crashes
7.	User-Friendly Interface: Clean menu-driven console interface with helpful prompts and emoji indicators

Quick Start Guide

Installation Steps:

1.	Clone the Repository: https://github.com/Down-To-Eat/VITyarthi-Project.git
2.	Verify Python Installation: Python 3.7.0
3.	Run the Application: python main.py

First-Time Usage:

1.	Launch the application using the command above
2.	Select a conversion category from the main menu (options 1-4)
3.	Enter the value you wish to convert
4.	Choose the source unit from the displayed list
5.	Select the target unit for conversion
6.	View the instant conversion result
7.	Access history (option 5) to review past conversions
8.	Check statistics (option 6) to analyze usage patterns

Project Architecture

Folder:

1.	main.py                      # Application entry point and user interface
2.	converter.py                 # Core conversion logic and mathematical formulas
3.	history.py                   # History management and statistical analysis
4.	validator.py                 # Input validation and error handling utilities
5.	logger.py                    # Application logging system
6.	README.md                    # Project documentation (this file)
7.	statement.md                 # Problem statement and project scope
8.	conversion_history.json      # Persistent history storage (auto-generated)
9.	application.log              # Application event logs (auto-generated)
10.	screenshots                 # Application demonstration images

Module Descriptions:

1. main.py (Application Controller):

1.	Lines of Code: ~138
2.	Purpose: Main program orchestration and user interaction
3.	Key Functions:
⦁	display_banner(): Shows application header
⦁	display_main_menu(): Renders interactive menu
⦁	perform_conversion(): Handles conversion workflow
⦁	main(): Primary application loop

2. converter.py (Conversion Engine):

1.	Lines of Code: ~140
2.	Purpose: Mathematical conversion logic
3.	Key Components:
⦁	LENGTH_UNITS: Dictionary mapping units to meter equivalents
⦁	WEIGHT_UNITS: Dictionary mapping units to kilogram equivalents
⦁	TIME_UNITS: Dictionary mapping units to second equivalents
⦁	convert_length(), convert_temperature(), convert_weight(), convert_time(): Conversion functions
⦁	get_available_units(): Returns available units for each category

3. history.py (History Manager):

1.	Lines of Code: ~150
2.	Purpose: Conversion tracking and analytics
3.	Key Features:
⦁	ConversionHistory class: Main history management
⦁	add_conversion(): Records new conversions
⦁	display_history(): Shows recent conversions
⦁	get_statistics(): Calculates usage metrics
⦁	export_to_text(): Exports data to readable format JSON-based persistent storage

4. validator.py (Input Validation):

1.	Lines of Code: ~110
2.	Purpose: User input validation and sanitization
3.	Key Functions:
⦁	get_valid_number(): Validates numeric inputs with constraints
⦁	get_valid_choice(): Ensures user selections are valid
⦁	get_menu_choice(): Validates menu option selections
⦁	confirm_action(): Yes/no confirmation prompts

5. logger.py (Logging System):

1.	Lines of Code: ~100
2.	Purpose: Comprehensive event logging
3.	Features:
⦁	ApplicationLogger class: Logging management
⦁	Multiple severity levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
⦁	Timestamped log entries
⦁	Session tracking with duration calculation

Technical Implementation

Conversion Methodology:

Base-Unit Approach: All conversions follow a standardized two-step process to ensure accuracy and consistency:

Step 1: Convert input value to the category's base unit

1.	Length → meters
2.	Temperature → Celsius
3.	Weight → kilograms
4.	Time → seconds

Step 2: Convert base unit value to target unit

Example Calculation:

Convert 100 feet to kilometers:
Step 1: 100 feet × 0.3048 = 30.48 meters (base unit)
Step 2: 30.48 meters ÷ 1000 = 0.03048 kilometers (target unit)
Result: 100 feet = 0.03048 km

Error Handling Strategy

Multi-Layer Validation:

1.	Input Layer: Validates data types and formats before processing
2.	Logic Layer: Try-except blocks catch conversion errors
3.	User Layer: Clear error messages guide user correction
4.	System Layer: Keyboard interrupt handling for graceful exits

Example Error Handling Flow:

try:
    value = float(user_input)
    if value < 0 and not allow_negative:
        raise ValueError("Negative values not allowed")
    result = convert_length(value, from_unit, to_unit)
except ValueError as e:
    display_error(str(e))
    logger.error(f"Conversion error: {e}")

Data Persistence

JSON Storage Format:

1.	Human-readable structure
2.	Cross-platform compatibility
3.	Easy data recovery and inspection
4.	Automatic save on each conversion
5.	Auto-load on application startup
