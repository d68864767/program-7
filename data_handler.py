import json
import os
from typing import Any, Dict, List

class DataHandler:
    def __init__(self, data_directory: str = "data"):
        """
        Initialize the DataHandler with a directory to store and manage data files.

        :param data_directory: The directory where data files are stored.
        """
        self.data_directory = data_directory
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def save_data(self, filename: str, data: Any) -> None:
        """
        Save data to a JSON file.

        :param filename: The name of the file to save the data in.
        :param data: The data to be saved, which should be JSON serializable.
        """
        file_path = os.path.join(self.data_directory, filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data(self, filename: str) -> Any:
        """
        Load data from a JSON file.

        :param filename: The name of the file to load the data from.
        :return: The data loaded from the file.
        """
        file_path = os.path.join(self.data_directory, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {filename} does not exist in the data directory.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def list_data_files(self) -> List[str]:
        """
        List all data files in the data directory.

        :return: A list of filenames.
        """
        return [f for f in os.listdir(self.data_directory) if os.path.isfile(os.path.join(self.data_directory, f))]

    def delete_data(self, filename: str) -> None:
        """
        Delete a data file.

        :param filename: The name of the file to delete.
        """
        file_path = os.path.join(self.data_directory, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"The file {filename} does not exist and cannot be deleted.")

# Example usage:
# data_handler = DataHandler()
# data_handler.save_data('example.json', {'key': 'value'})
# data = data_handler.load_data('example.json')
# print(data)
# files = data_handler.list_data_files()
# print(files)
# data_handler.delete_data('example.json')
