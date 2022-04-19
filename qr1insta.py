import qrcode
import image

def getcode(url= 'https://google.com', name = 'default'):
    qrCODE = qrcode.make(data= url)
    qrCODE.save(stream = f'{name}.png')

    return f'Completed codeqr. {name}.png'

def main():
    print(getcode(url = 'https://https://www.instagram.com/accounts/nikita_____vy/', name= 'instagram'))

if __name__ == '__main__':
    main()