from services.data_loader import DataLoader
from services.data_validator import DataValidator


def main():
    data_directory = "../archives/christianity_century_1"
    data = DataLoader.load_data(data_directory)

    if DataValidator.validate(data):
        print("✓ Data loaded and validated successfully.\n")
        print("Summary:")
        print(f"  - Centuries: {len(data.get('centuries', []))}")
        print(f"  - Events: {len(data.get('events', []))}")
        print(f"  - Sources: {len(data.get('sources', []))}")
        print(f"  - Confidence levels: {len(data.get('confidence_model', []))}")
    else:
        print("✗ Data validation failed.")


if __name__ == "__main__":
    main()
