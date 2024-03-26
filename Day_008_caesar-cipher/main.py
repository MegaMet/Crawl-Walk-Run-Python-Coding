import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running = True

print(art.logo)

#shift alphabet
def ceasar(direction, start_text, shift):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for i in start_text:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index + shift) % len(alphabet)
            end_text += alphabet[new_index]
        else:
            end_text += i

    print(f"The {direction}d text is:\n{end_text}.")

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(direction, text, shift)
    answer = input(f"Would you to go again? 'yes' or 'no': ").lower()
    if answer == "no":
        running = False
        print("Goodbye")