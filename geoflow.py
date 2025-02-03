import subprocess
import re

def check_windows_settings():
    # Check for Cortana settings
    cortana_status = subprocess.run(["powershell", "-Command", "Get-Command | Select-String -Pattern 'Cortana'"], capture_output=True, text=True)
    if cortana_status.stdout:
        print("Cortana is enabled. Consider disabling it to improve privacy.")

    # Check telemetry settings
    telemetry_status = subprocess.run(["powershell", "-Command", "Get-ItemProperty -Path HKLM:\\Software\\Policies\\Microsoft\\Windows\\DataCollection | Select-Object AllowTelemetry"], capture_output=True, text=True)
    if 'AllowTelemetry' in telemetry_status.stdout and '0' not in telemetry_status.stdout:
        print("Telemetry is enabled. Consider setting it to 0 to disable data collection.")

    # Check for location services
    location_status = subprocess.run(["powershell", "-Command", "Get-ItemProperty -Path HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location | Select-Object Value"], capture_output=True, text=True)
    if 'Allow' in location_status.stdout:
        print("Location services are enabled. Consider disabling them for better privacy.")

def check_installed_apps():
    # Check for apps that have access to your microphone
    mic_access_apps = subprocess.run(["powershell", "-Command", "Get-Process | Select-String -Pattern 'Microphone'"], capture_output=True, text=True)
    if mic_access_apps.stdout:
        print("Some apps have access to your microphone. Review and adjust app permissions.")

    # Check for apps that have access to your camera
    camera_access_apps = subprocess.run(["powershell", "-Command", "Get-Process | Select-String -Pattern 'Camera'"], capture_output=True, text=True)
    if camera_access_apps.stdout:
        print("Some apps have access to your camera. Review and adjust app permissions.")

def main():
    print("GeoFlow: Privacy Leak Scanner for Windows")
    print("Scanning Windows settings...")
    check_windows_settings()
    print("\nScanning installed applications...")
    check_installed_apps()
    print("\nScan complete. Review the recommendations above.")

if __name__ == "__main__":
    main()