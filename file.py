#modfing hosts file
host = input("Enter host name: ")
# Open a file with access mode 'a'
file_object = open('C:\Windows\System32\drivers\etc\hosts', 'a')
# Append 'hello' at the end of file
file_object.write(f'\n127.0.0.1       {host}')
# Close the file
file_object.close()

#------------------------------------------------------------------------------------------------

#modifing vhosts file in apache

servname = input("Enter ServerName: ")
DocumentRoot = input("Enter document root: ")
# Open a file with access mode 'a'
file_object = open('C:\\xampp\\apache\\conf\\extra\\httpd-vhosts.conf', 'a')
# Append 'hello' at the end of file
file_object.write(f'\n<VirtualHost *:80>')
file_object.write(f'\n    ServerName www.{servname}')
file_object.write(f'\n    ServerAlias {servname}')
file_object.write(f'\n    DocumentRoot {DocumentRoot}')
file_object.write(f'\n</VirtualHost>')

# Close the file
file_object.close()


print("success")

'''
file_object.write(f'<VirtualHost *:80>')
file_object.write(f'    ServerName www.joomla.16')
file_object.write(f'    ServerAlias joomla.16')
file_object.write(f'    DocumentRoot d:/xampp/htdocs/joomla16')
file_object.write(f'</VirtualHost>')
'''
