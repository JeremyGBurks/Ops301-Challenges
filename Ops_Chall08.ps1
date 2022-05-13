# Author - Jeremy Burks
# Date Last Revised - 05/12/22
# Purpose - Creates a new OU then automates adding a user to ADAC

# Creates a new OU
New-ADOrganizationalUnit -Name "GLobeX TPS Department" -ProtectedFromAccidentalDeletion $false
#Creates a new user with all their info
New-ADUser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Ferdinand" -SamAccountName "F.Ferdinand" -UserPrincipalName "ferdi@GlobeXpower.com" -Title "TPS Reporting Lead" -Company "GlobeX USA" 
