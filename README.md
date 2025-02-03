# GeoFlow

GeoFlow is a Python-based program designed to scan and identify potential privacy leaks within Windows settings and applications. It helps users to recognize and address privacy vulnerabilities related to Windows telemetry, location services, and installed applications that may have access to sensitive resources like the microphone and camera.

## Features

- Scans Windows settings to identify:
  - Cortana status
  - Telemetry data collection
  - Location services

- Scans installed applications to identify:
  - Apps with microphone access
  - Apps with camera access

## Installation

1. Ensure you have Python installed on your Windows machine. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `geoflow.py` file.

3. Open a terminal or command prompt and navigate to the directory containing `geoflow.py`.

## Usage

To run GeoFlow, execute the following command in your terminal or command prompt:

```bash
python geoflow.py
```

GeoFlow will scan your system settings and installed applications, providing you with a summary of potential privacy leaks and suggestions for improving your privacy settings.

## Notes

- GeoFlow requires administrative privileges to check certain system settings.
- The program currently supports Windows operating systems.

## Contribution

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.