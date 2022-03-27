const palindrome = (str) => {
  let lowerString = str.toLowerCase().replace(/[\W_]/g, '')
  let reverseString = lowerString.split('').reverse().join('')
  return reverseString === lowerString
}

console.log(palindrome('eye'))