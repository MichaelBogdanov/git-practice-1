@echo off
setlocal enabledelayedexpansion
set /p "input=enter an ip: "
set "psfile=%temp%\ipcheck_%random%.ps1"

(
echo $s = $env:input
echo function Normalize-IPv6^($bytes^) {
echo     if ^($bytes.Length -ne 16^) { return $null }
echo     $blocks = for ^($i = 0; $i -lt 16; $i += 2^) {
echo         [uint16]^($bytes[$i] -shl 8^) -bor $bytes[$i+1]
echo     }
echo     $maxStart = -1
echo     $maxLen = 0
echo     $i = 0
echo     while ^($i -lt $blocks.Length^) {
echo         if ^($blocks[$i] -eq 0^) {
echo             $j = $i
echo             while ^($j -lt $blocks.Length -and $blocks[$j] -eq 0^) { $j++ }
echo             $len = $j - $i
echo             if ^($len -gt $maxLen^) {
echo                 $maxLen = $len
echo                 $maxStart = $i
echo             }
echo             $i = $j
echo         } else {
echo             $i++
echo         }
echo     }
echo     if ^($maxLen -ge 2^) {
echo         $left = if ^($maxStart -gt 0^) { $blocks[0..^($maxStart-1^)] ^| ForEach-Object { $_.ToString^('x'^) } } else { @(^) }
echo         $right = if ^($maxStart + $maxLen -lt $blocks.Length^) { $blocks[^($maxStart+$maxLen^)..7] ^| ForEach-Object { $_.ToString^('x'^) } } else { @(^) }
echo         $leftStr = $left -join ':'
echo         $rightStr = $right -join ':'
echo         if ^($leftStr -eq '' -and $rightStr -eq ''^) {
echo             return '::'
echo         } elseif ^($leftStr -eq ''^) {
echo             return '::' + $rightStr
echo         } elseif ^($rightStr -eq ''^) {
echo             return $leftStr + '::'
echo         } else {
echo             return $leftStr + '::' + $rightStr
echo         }
echo     } else {
echo         return ^($blocks ^| ForEach-Object { $_.ToString^('x'^) }^) -join ':'
echo     }
echo }
echo # Проверка IPv4
echo $parts = $s.Split^('.'^)
echo if ^($parts.Count -eq 4^) {
echo     $valid = $true
echo     foreach ^($part in $parts^) {
echo         if ^($part -match '^^\d+$'^) {
echo             if ^($part -ne '0' -and $part -match '^^0'^) { $valid = $false; break }
echo             $num = [int]$part
echo             if ^($num -lt 0 -or $num -gt 255^) { $valid = $false; break }
echo         } else {
echo             $valid = $false; break
echo         }
echo     }
echo     if ^($valid^) {
echo         Write-Output "IPv4"
echo         exit
echo     }
echo }
echo # Проверка IPv6
echo $ip = $null
echo if ^([System.Net.IPAddress]::TryParse^($s, [ref]$ip^)^) {
echo     if ^($ip.AddressFamily -eq 'InterNetworkV6'^) {
echo         $normalized = Normalize-IPv6 $ip.GetAddressBytes^(^)
echo         Write-Output "IPv6"
echo         Write-Output $normalized
echo         exit
echo     }
echo }
echo Write-Output "INVALID"
) > "%psfile%"

powershell -ExecutionPolicy Bypass -File "%psfile%"
del "%psfile%"
pause