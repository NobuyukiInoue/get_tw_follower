Param( $file1, $file2 )

if (-Not($file1)) {
    Write-Host "Usage :"$MyInvocation.MyCommand.Name "file1 file2"
    exit 0
}

if (-Not($file2)) {
    Write-Host "Usage :"$MyInvocation.MyCommand.Name "file1 file2"
    exit 0
}

$file1 = $file1.Replace('.\', '')
$file2 = $file2.Replace('.\', '')

df.exe $file1 $file2
