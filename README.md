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

Length Conversion: Supports 8 units including meter, kilometer, centimeter, millimeter, mile, yard, foot, and inch
Temperature Conversion: Seamlessly converts between Celsius, Fahrenheit, and Kelvin scales
Weight Conversion: Handles 6 units including kilogram, gram, milligram, pound, ounce, and ton
Time Conversion: Converts across 7 units from seconds to years

Advanced Features:

Conversion History: Automatically tracks up to 50 recent conversions with precise timestamps
Usage Statistics: Provides detailed analytics on conversion patterns and most-used categories
Data Persistence: Saves history across sessions using JSON storage format
Export Functionality: Allows exporting conversion history to human-readable text files
Comprehensive Logging: Records all application events and errors for debugging and audit purposes
Input Validation: Implements multi-layer validation to ensure data integrity and prevent crashes
User-Friendly Interface: Clean menu-driven console interface with helpful prompts and emoji indicators

Quick Start Guide

Installation Steps:

Clone the Repository: https://github.com/Down-To-Eat/VITyarthi-Project.git
Verify Python Installation: Python 3.7.0
Run the Application: python main.py

First-Time Usage:

Launch the application using the command above
Select a conversion category from the main menu (options 1-4)
Enter the value you wish to convert
Choose the source unit from the displayed list
Select the target unit for conversion
View the instant conversion result
Access history (option 5) to review past conversions
Check statistics (option 6) to analyze usage patterns

Project Architecture

Folder:

main.py                      # Application entry point and user interface
converter.py                 # Core conversion logic and mathematical formulas
history.py                   # History management and statistical analysis
validator.py                 # Input validation and error handling utilities
logger.py                    # Application logging system
README.md                    # Project documentation (this file)
statement.md                 # Problem statement and project scope
conversion_history.json      # Persistent history storage (auto-generated)
application.log              # Application event logs (auto-generated)
screenshots                 # Application demonstration images

Module Descriptions:

1. main.py (Application Controller):

Lines of Code: ~138
Purpose: Main program orchestration and user interaction
Key Functions:
display_banner(): Shows application header
display_main_menu(): Renders interactive menu
perform_conversion(): Handles conversion workflow
main(): Primary application loop

2. converter.py (Conversion Engine):

Lines of Code: ~140
Purpose: Mathematical conversion logic
Key Components:
LENGTH_UNITS: Dictionary mapping units to meter equivalents
WEIGHT_UNITS: Dictionary mapping units to kilogram equivalents
TIME_UNITS: Dictionary mapping units to second equivalents
convert_length(), convert_temperature(), convert_weight(), convert_time(): Conversion functions
get_available_units(): Returns available units for each category

3. history.py (History Manager):

Lines of Code: ~150
Purpose: Conversion tracking and analytics
Key Features:
ConversionHistory class: Main history management
add_conversion(): Records new conversions
display_history(): Shows recent conversions
get_statistics(): Calculates usage metrics
export_to_text(): Exports data to readable format JSON-based persistent storage

4. validator.py (Input Validation):

Lines of Code: ~110
Purpose: User input validation and sanitization
Key Functions:
get_valid_number(): Validates numeric inputs with constraints
get_valid_choice(): Ensures user selections are valid
get_menu_choice(): Validates menu option selections
confirm_action(): Yes/no confirmation prompts

5. logger.py (Logging System):

Lines of Code: ~100
Purpose: Comprehensive event logging
Features:
ApplicationLogger class: Logging management
Multiple severity levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
Timestamped log entries
Session tracking with duration calculation

Technical Implementation

Conversion Methodology:

Base-Unit Approach: All conversions follow a standardized two-step process to ensure accuracy and consistency:

Step 1: Convert input value to the category's base unit

Length → meters
Temperature → Celsius
Weight → kilograms
Time → seconds

Step 2: Convert base unit value to target unit

Example Calculation:

Convert 100 feet to kilometers:
Step 1: 100 feet × 0.3048 = 30.48 meters (base unit)
Step 2: 30.48 meters ÷ 1000 = 0.03048 kilometers (target unit)
Result: 100 feet = 0.03048 km

Error Handling Strategy

Multi-Layer Validation:

Input Layer: Validates data types and formats before processing
Logic Layer: Try-except blocks catch conversion errors
User Layer: Clear error messages guide user correction
System Layer: Keyboard interrupt handling for graceful exits

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

Human-readable structure
Cross-platform compatibility
Easy data recovery and inspection
Automatic save on each conversion
Auto-load on application startup

