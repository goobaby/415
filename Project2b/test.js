function multiply(x, y) {
    if (BigInt(x) < 10n && BigInt(y) < 10n) {
      return BigInt(x) * BigInt(y);
    }
  
    const xHalf = Math.floor(x.length / 2);
    const yHalf = Math.floor(y.length / 2);
  
    const a = String(x).substr(0, xHalf);
    const b = String(x).substr(xHalf);
    const c = String(y).substr(0, yHalf);
    const d = String(y).substr(yHalf);
  
    return merge(a, b, c, d);
  }
  
  function merge(a, b, c, d) {
    const n = BigInt(a.length + b.length);
    const half = n / 2n;
  
    const ac = multiply(a, c);
    const bd = multiply(b, d);
    const ad = multiply(a, d);
    const bc = multiply(b, c);
  
    return 10n ** n * ac
      + 10n ** half * (ad + bc)
      + bd;
  }

  function Exponentiation2(a, n) {

    if ((BigInt(n) % 2n == 0n) && (BigInt(n) > 0n) ) {
        square = Exponentiation2(a, n/2)
        return multiply(square, square);
    }
    if (n % 2 == 1){
        squareMinus = Exponentiation2(a, (n-1)/2)
        multMinus1 = multiply(squareMinus, squareMinus)
        return multiply(multMinus1 , a);
    }
    if (BigInt(n) == 0n)
        return BigInt(1);
}