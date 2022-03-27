const UNITS = {
  'PENNY': 0.01,
  'NICKEL': 0.05,
  'DIME': 0.10,
  'QUARTER': 0.25,
  'ONE': 1.00,
  'FIVE': 5.00,
  'TEN': 10.00,
  'TWENTY': 20.00,
  'ONE HUNDRED': 100.00
}

const checkCashRegister = (price, cash, cid) => {
  const REGISTER = {
    'status': 'OPEN',
    'change': []
  }

  let change = cash - price
  let flatCID = cid.flat().filter(x => Number(x))
  let totalCID = flatCID.reduce(x => x + x).toFixed(2)

  if (change > totalCID) {
    REGISTER.status = 'INSUFFICIENT_FUNDS'
    return REGISTER
  } else if (change.toFixed(2) === totalCID) {
    REGISTER.status = 'CLOSED'
    REGISTER.change = cid
    return REGISTER
  }

  Object.entries(cid.reverse()).map(([k, v]) => {
    let newCID = [v[0], 0]
    while (change >= UNITS[v[0]] && v[1] > 0) {
      newCID[1] += UNITS[v[0]]
      v[1] -= UNITS[v[0]]
      change -= UNITS[v[0]]
      change = change.toFixed(2)
    }
    if (newCID[1] > 0) {
      REGISTER.change.push(newCID)
    }
  })
  return REGISTER
}

console.log(checkCashRegister(19.5, 20, [['PENNY', 1.01], ['NICKEL', 2.05], ['DIME', 3.1], ['QUARTER', 4.25], ['ONE', 90], ['FIVE', 55], ['TEN', 20], ['TWENTY', 60], ['ONE HUNDRED', 100]]))