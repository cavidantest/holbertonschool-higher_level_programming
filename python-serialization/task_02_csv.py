import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named data.json.
    
    Args:
        csv_filename (str): The name of the input CSV file.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
            
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
