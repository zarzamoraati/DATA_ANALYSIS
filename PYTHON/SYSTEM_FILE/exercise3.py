import os

def find(start_path, target_dir):
    absolute_start_path = os.path.abspath(start_path)

    def search_in_directory(directory_path):
        for file in os.listdir(directory_path):
            current_path = os.path.join(directory_path, file)

            if os.path.isdir(current_path):
                if file == target_dir:
                    print(os.path.abspath(current_path))
                search_in_directory(current_path)

    search_in_directory(absolute_start_path)

# Rutas proporcionadas en el enunciado
os.makedirs("./tree/python/other_courses/python")
os.makedirs("./tree/cpp/other_courses/python")
os.makedirs("./tree/c/other_courses/python")

# Llamada a la función para encontrar las rutas absolutas
find("./tree", "python")