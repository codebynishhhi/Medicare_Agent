from app.config import settings


def main():
    print("Model:", settings.model_name)
    print("Temperature:", settings.temperature)
    print("Data:", settings.data_path)


if __name__ == "__main__":
    main()