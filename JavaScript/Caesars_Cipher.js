const alphabet = [
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

const MAX_ROT = alphabet.length
const ROT = 13

const rot13 = (string) => {
    if (ROT > MAX_ROT || ROT < 0) {
        throw Error('ROT has to be between 0 - alphabet.length')
    }

    string = Array.from(string)

    const decryptedString = string.map((character) => {
        const alphabet_index = alphabet.indexOf(character.toUpperCase())
        if (alphabet_index === -1) { return character }
        let decryptedIndex = (alphabet_index - ROT) % MAX_ROT
        decryptedIndex = decryptedIndex < 0 ? decryptedIndex + MAX_ROT : decryptedIndex
        const decryptedChar = alphabet[decryptedIndex]
        return decryptedChar.toUpperCase()
    })
    return decryptedString.join('')
}

console.log(rot13("SERR PBQR PNZC"))