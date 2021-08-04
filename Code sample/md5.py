import hashlib
filename= "T:\安控組\VPN\說明文件與問題排除\版本升級操作手冊\PSA UPGRADE SOFTWARE.pdf"
m=hashlib.md5()
with open(filename,"rb") as f:
    buf=f.read()
    m.update(buf)
    
h=m.hexdigest()
print(h)


