def validate(ip):
    parts =ip.split('.')
    if len(parts) !=4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
    return True

def main():
    ip =input ('IPv4 address')
    if validate(ip):
        print('Valid IPv4 address')
    else:
        print('Ivalid IPv4 address')
        
if __name__ == '__main__':
    main()