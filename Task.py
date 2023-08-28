# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра. 
# (Например: Треугольник дз1, дроби дз2)

import os
import json

class DirectorySerializer:
    def __init__(self):
        self.directory_items = []

    def scan_directory(self):
        for item in os.scandir():
            item_info = {}
            item_info['name'] = item.name
            if item.is_file():
                item_info['extension'] = os.path.splitext(item.name)[1]
                item_info['type'] = 'file'
            elif item.is_dir():
                item_info['type'] = 'directory'
            self.directory_items.append(item_info)

    def serialize(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.directory_items, file, indent=2)

serializer = DirectorySerializer()
serializer.scan_directory()
serializer.serialize('directory.json')