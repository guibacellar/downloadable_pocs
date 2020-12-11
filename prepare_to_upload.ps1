# powershell -ExecutionPolicy Unrestricted -File prepare_to_upload.ps1
Add-Type -Assembly "System.IO.Compression.FileSystem" ;
[System.IO.Compression.ZipFile]::CreateFromDirectory("dist", "compiled_malware.zip") ;