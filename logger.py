"""
Logging Module
Comprehensive logging system for application events and errors
Author: [Your Name]
Date: November 24, 2025
"""

from datetime import datetime
import os

class ApplicationLogger:
    """Handles application logging with multiple severity levels"""
    
    # Log levels
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'
    
    def __init__(self, filename='application.log', console_output=False):
        """
        Initialize logger
        
        Args:
            filename (str): Log file name
            console_output (bool): Whether to also print to console
        """
        self.filename = filename
        self.console_output = console_output
        self.session_start = datetime.now()
        self._log(self.INFO, "="*60)
        self._log(self.INFO, f"Application started - Session: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        self._log(self.INFO, "="*60)
    
    def _log(self, level, message):
        """
        Internal logging method
        
        Args:
            level (str): Log level
            message (str): Log message
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_entry = f"[{timestamp}] [{level:8s}] {message}"
        
        try:
            # Write to file
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(log_entry + '\n')
            
            # Optionally print to console
            if self.console_output:
                print(log_entry)
        
        except Exception as e:
            print(f"⚠️  Logging error: {e}")
    
    def debug(self, message):
        """Log debug message"""
        self._log(self.DEBUG, message)
    
    def info(self, message):
        """Log info message"""
        self._log(self.INFO, message)
    
    def warning(self, message):
        """Log warning message"""
        self._log(self.WARNING, message)
    
    def error(self, message):
        """Log error message"""
        self._log(self.ERROR, message)
    
    def critical(self, message):
        """Log critical message"""
        self._log(self.CRITICAL, message)
    
    def log_conversion(self, category, value, from_unit, to_unit, result):
        """Log a successful conversion"""
        self.info(f"Conversion - {category}: {value} {from_unit} → {result} {to_unit}")
    
    def log_error_conversion(self, category, error):
        """Log a failed conversion"""
        self.error(f"Conversion failed - {category}: {error}")
    
    def log_user_action(self, action):
        """Log user action"""
        self.info(f"User action: {action}")
    
    def close_session(self):
        """Log session end"""
        session_end = datetime.now()
        duration = session_end - self.session_start
        self._log(self.INFO, "="*60)
        self._log(self.INFO, f"Application closed - Duration: {duration}")
        self._log(self.INFO, "="*60)
    
    def get_log_summary(self):
        """Get summary of log file"""
        if not os.path.exists(self.filename):
            return "No log file found."
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Count by level
            level_counts = {
                self.DEBUG: 0,
                self.INFO: 0,
                self.WARNING: 0,
                self.ERROR: 0,
                self.CRITICAL: 0
            }
            
            for line in lines:
                for level in level_counts:
                    if f'[{level}]' in line:
                        level_counts[level] += 1
                        break
            
            summary = f"\n📄 Log File: {self.filename}\n"
            summary += f"   Total Entries: {len(lines)}\n"
            for level, count in level_counts.items():
                if count > 0:
                    summary += f"   {level}: {count}\n"
            
            return summary
        
        except Exception as e:
            return f"Error reading log: {e}"
