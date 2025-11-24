"""
History Management Module
Tracks conversion history with timestamps and persistence
Author: [Your Name]
Date: November 24, 2025
"""

from datetime import datetime
import json
import os

class ConversionHistory:
    """Manages conversion history with file persistence"""
    
    def __init__(self, max_entries=20, filename='conversion_history.json'):
        """
        Initialize history manager
        
        Args:
            max_entries (int): Maximum number of history entries to keep
            filename (str): File to store history
        """
        self.max_entries = max_entries
        self.filename = filename
        self.history = []
        self.load_from_file()
    
    def add_conversion(self, category, value, from_unit, to_unit, result):
        """
        Add a new conversion to history
        
        Args:
            category (str): Conversion category (length/temperature/etc)
            value (float): Input value
            from_unit (str): Source unit
            to_unit (str): Target unit
            result (float): Conversion result
        """
        entry = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'category': category.capitalize(),
            'input': f"{value} {from_unit}",
            'output': f"{result} {to_unit}",
            'conversion': f"{value} {from_unit} → {result} {to_unit}"
        }
        
        self.history.append(entry)
        
        # Keep only most recent entries
        if len(self.history) > self.max_entries:
            self.history = self.history[-self.max_entries:]
        
        self.save_to_file()
    
    def display_history(self, limit=10):
        """
        Display conversion history
        
        Args:
            limit (int): Number of recent entries to show
        """
        if not self.history:
            print("\n📋 No conversion history available.")
            print("   Perform some conversions to see history here!\n")
            return
        
        recent = self.history[-limit:]
        
        print("\n" + "="*70)
        print(f"📋 CONVERSION HISTORY (Last {len(recent)} entries)")
        print("="*70)
        
        for i, entry in enumerate(reversed(recent), 1):
            print(f"\n{i}. 🕐 {entry['timestamp']}")
            print(f"   📂 Category: {entry['category']}")
            print(f"   🔄 Conversion: {entry['conversion']}")
        
        print("\n" + "="*70)
    
    def get_statistics(self):
        """Get statistics about conversion usage"""
        if not self.history:
            return None
        
        # Count conversions by category
        category_counts = {}
        for entry in self.history:
            cat = entry['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        return {
            'total_conversions': len(self.history),
            'by_category': category_counts,
            'most_used': max(category_counts.items(), key=lambda x: x[1])[0]
        }
    
    def display_statistics(self):
        """Display usage statistics"""
        stats = self.get_statistics()
        
        if not stats:
            print("\n📊 No statistics available yet.\n")
            return
        
        print("\n" + "="*70)
        print("📊 USAGE STATISTICS")
        print("="*70)
        print(f"\n🔢 Total Conversions: {stats['total_conversions']}")
        print(f"⭐ Most Used Category: {stats['most_used']}")
        print("\n📂 Conversions by Category:")
        
        for category, count in sorted(stats['by_category'].items()):
            bar = "█" * (count * 2)
            print(f"   {category:15s} : {bar} ({count})")
        
        print("\n" + "="*70)
    
    def clear_history(self):
        """Clear all conversion history"""
        self.history = []
        self.save_to_file()
        print("\n✅ Conversion history cleared successfully!\n")
    
    def save_to_file(self):
        """Save history to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            print(f"⚠️  Warning: Could not save history: {e}")
    
    def load_from_file(self):
        """Load history from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.history = json.load(f)
            except Exception as e:
                print(f"⚠️  Warning: Could not load history: {e}")
                self.history = []
    
    def export_to_text(self, filename='history_export.txt'):
        """Export history to readable text file"""
        if not self.history:
            print("\n❌ No history to export.\n")
            return
        
        try:
            with open(filename, 'w') as f:
                f.write("UNIT CONVERTER - CONVERSION HISTORY\n")
                f.write("="*70 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*70 + "\n\n")
                
                for i, entry in enumerate(self.history, 1):
                    f.write(f"{i}. [{entry['timestamp']}]\n")
                    f.write(f"   Category: {entry['category']}\n")
                    f.write(f"   Conversion: {entry['conversion']}\n\n")
                
                # Add statistics
                stats = self.get_statistics()
                if stats:
                    f.write("\n" + "="*70 + "\n")
                    f.write("STATISTICS\n")
                    f.write("="*70 + "\n")
                    f.write(f"Total Conversions: {stats['total_conversions']}\n")
                    f.write(f"Most Used Category: {stats['most_used']}\n\n")
                    f.write("By Category:\n")
                    for cat, count in sorted(stats['by_category'].items()):
                        f.write(f"  - {cat}: {count}\n")
            
            print(f"\n✅ History exported to '{filename}' successfully!\n")
        
        except Exception as e:
            print(f"\n❌ Error exporting history: {e}\n")
