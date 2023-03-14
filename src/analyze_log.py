def analyze_log(path_to_file):
    if not path_to_file:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            print(file)
    except Exception:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
