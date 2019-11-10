chars = [
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'abcdefghijklmnopqrstuvwxyz'
]
arr_len = 2
alpha_len = 26

# Find out if character is a letter & if so, return it's indices
# Not allowed to use the inbuilt find function
def find(char):
    for i in range(arr_len):
        for j in range(alpha_len):
            if char == chars[i][j]:
                return [i, j]

def encrypt(key, msg):
    key_ind = 0
    
    for char in msg:
        num = find(char)
        if num:
            num[1] += find(key[key_ind])[1]
            num[1] %= alpha_len
            print(chars[num[0]][num[1]], end='')

            key_ind += 1
            if key_ind == len(key):
                key_ind = 0

        else:
            print(char, end='')

if __name__ == "__main__":
    encrypt(input('Key: '), input('Message: '))
