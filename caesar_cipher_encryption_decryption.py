

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = " "

    if directions == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabets:
            output_text += letter
        else:

            
            position = alphabets.index(letter) + shift_amount
            position = position % len(alphabets)

            output_text += alphabets[position]
    print(f"Here is the encoded result {output_text}")


should_contuine = True

while should_contuine:
    alphabets =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','u','v','w','x','y','z']

    directions = input("Type encode to encrypt and decode to decrypt:\n").lower()
    text = input("Please enter the text:\n").lower()

    shift = int(input("type the shift number :"))


    ceaser(original_text=text, shift_amount=shift, encode_or_decode=directions)

    restart = input("Type 'yes' if you wants to go again otherwise Type 'no' ").lower()
    if restart  == "no":
        should_contuine = False
        print("Goodbye")


