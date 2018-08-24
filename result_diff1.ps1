Param( $file1, $file2 )

if (-Not($file1)) {
	Write-Host "Usage : result_diff.ps1 file1 file2"
	exit 0
}

if (-Not($file2)) {
	Write-Host "Usage : result_diff.ps1 file1 file2"
	exit 0
}

$A = Get-Content $file1
$B = Get-Content $file2

Compare-Object $A $B
