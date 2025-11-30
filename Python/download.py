import sys
import requests
from pathlib import Path

def download_version(version_number):
    version_map = {
        "1": ("macOS 26", "https://swcdn.apple.com/content/downloads/60/34/089-04325-A_JAKF079NR4/fjimp3su7pvbg0o6sf3kus7k989finz274/InstallAssistant.pkg"),
        "2": ("macOS 15", "https://swcdn.apple.com/content/downloads/23/34/093-99065-A_B4TEYIISAM/1a1ddvynvgdh82ev879kh13y2a3trwr18v/InstallAssistant.pkg"),
        "3": ("macOS 14", "https://swcdn.apple.com/content/downloads/43/05/093-92756-A_8KCV583EO6/rk4pkpm81lfh7ee76z8qupc8jtoo4nrde1/InstallAssistant.pkg"),
        "5": ("macOS 13", "https://swcdn.apple.com/content/downloads/09/46/093-22004-A_QNZEDC334I/phigx2zvoggml6sh79my4y51fnvgy8hix4/InstallAssistant.pkg"),
        "6": ("macOS 12", "https://swcdn.apple.com/content/downloads/46/57/052-60131-A_KM2RH04C2D/9yzvba1uvpem2wuo95r459qno57qaizwf2/InstallAssistant.pkg"),
        "7": ("macOS 11", "http://swcdn.apple.com/content/downloads/14/38/042-45246-A_NLFOFLCJFZ/jk992zbv98sdzz3rgc7mrccjl3l22ruk1c/InstallAssistant.pkg"),       
        "8": ("macOS 10.12", "http://updates-http.cdn-apple.com/2019/cert/061-39476-20191023-48f365f4-0015-4c41-9f44-39d3d2aca067/InstallOS.dmg"),
        "9": ("Mac OS X 10.11", "http://updates-http.cdn-apple.com/2019/cert/061-41424-20191024-218af9ec-cf50-4516-9011-228c78eda3d2/InstallMacOSX.dmg"),
        "10": ("Mac OS X 10.10", "http://updates-http.cdn-apple.com/2019/cert/061-41343-20191023-02465f92-3ab5-4c92-bfe2-b725447a070d/InstallMacOSX.dmg"),
        "11": ("Mac OS X 10.8", "https://updates.cdn-apple.com/2021/macos/031-0627-20210614-90D11F33-1A65-42DD-BBEA-E1D9F43A6B3F/InstallMacOSX.dmg"),
        "12": ("Mac OS X 10.7", "https://updates.cdn-apple.com/2021/macos/041-7683-20210614-E610947E-C7CE-46EB-8860-D26D71F0D3EA/InstallMacOSX.dmg"),
    }

    version_info = version_map.get(version_number)
    if not version_info:
        print("Invalid selection")
        return

    version_name, download_url = version_info
    filename = Path(f"{version_name.replace(' ', '_')}.dmg")

    print(f"Downloading {version_name} from {download_url}...")

    try:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()

        total = int(response.headers.get('content-length', 0))
        with open(filename, 'wb') as file:
            downloaded = 0
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                downloaded += len(data)
                done = int(50 * downloaded / total) if total else 0
                print(f"\r[{'=' * done}{' ' * (50 - done)}] {downloaded / 1024:.1f}KB", end='')

        print(f"\nDownload complete: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_choice = sys.argv[1]
        download_version(user_choice)
    else:
        print("No version selected")
