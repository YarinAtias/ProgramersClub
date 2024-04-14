import requests
import os

VIRUS_TOTAL_URL = 'https://www.virustotal.com/vtapi/v2/file/scan'
VIRUS_TOTAL_API = "5ce0c7eedd86ea281307c7affff6b10ff4106956070c20eb04f39eae2568b3ed"

def file_scan(my_file):
    with open(my_file, 'rb') as file:
        files = {'file': (my_file, file)}
        params = {'apikey': VIRUS_TOTAL_API}

        # Submit the file for scanning
        response = requests.post(VIRUS_TOTAL_URL, files=files, params=params)
        # Extracting the 'Permalink' for in order to create the scan URL
        permalink = response.json()["permalink"]
        virus_total_analysis_url = f"https://www.virustotal.com/gui/file/{permalink}"
        print("Analysis URL:", virus_total_analysis_url)

        # Fetch the analysis report
        headers = {'x-apikey': VIRUS_TOTAL_API}
        scan_id = response.json()["scan_id"]
        params = {'apikey': VIRUS_TOTAL_API, 'resource': scan_id}
        analysis_report_url = f"https://www.virustotal.com/vtapi/v2/file/report"
        analysis_report = requests.get(analysis_report_url, headers=headers, params=params)

        # Checking while the scan is not done
        print("Waiting for analysis report...")
        while "positives" not in analysis_report.text:
            analysis_report = requests.get(analysis_report_url, headers=headers, params=params)

        # Extracting the scan result and checking for the file status
        file_security_status = analysis_report.json()["positives"]
        if file_security_status == 0:
            print("The file is clean and secure.")
        else:
            print("This file may contain potential threats. Review the analysis report for more details")



def all_files_in_directory(dir_path: str, i: int):
    directory = os.listdir(dir_path)
    length_dir = len(directory)
    if i == length_dir:
        return None
    print(directory[i])
    all_files_in_directory(dir_path, i + 1)

