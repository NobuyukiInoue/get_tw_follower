Param( $file1, $file2 )

if (-Not($file1)) {
	Write-Host "Usage : result_diff2.ps1 file1 file2"
	exit 0
}

if (-Not($file2)) {
	Write-Host "Usage : result_diff2.ps1 file1 file2"
	exit 0
}

$file1 = $file1.Replace('.\', '')
$file2 = $file2.Replace('.\', '')

D:\share\�c�[���Q\df141\df.exe $file1 $file2
