#pip install pysmb -- Install this

from smb.SMBConnection import SMBConnection

conn = SMBConnection('username', 'password', 'local_NetBIOS_name', 'remote_NetBIOS_name')
conn.connect('ip_address')
results = conn.listPath('share_name', '/optionally/some/subfolder')

for x in results:
    print (x.filename)