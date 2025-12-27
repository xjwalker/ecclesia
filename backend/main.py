from services.data_loader import DataLoader
from services.data_validator import DataValidator


def main():
    data_directory = "../archives"
    data = DataLoader.load_data(data_directory)

    if DataValidator.validate(data):
        print("Data loaded and validated successfully.")
    else:
        print("Data validation failed.")


if __name__ == "__main__":
    main()
