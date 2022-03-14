/**
 * Karatsuba Multiplication
 * @param  {Number} x - first number
 * @param  {Number} y - second number
 * @return {Number} Multiply of x and y
 */
 
 function karatsubaMulti(x, y) {

    let n = Math.min(('' + x).length, ('' + y).length);
  
    if(n == 1)
      return x * y;
  
    let tenToHalf = Math.pow(10, parseInt(n / 2));
    let tenToN = Math.pow(10, 2 * parseInt(n / 2));
  
    let a0 = parseInt(x / tenToHalf);
    let a1 = x % tenToHalf;
    let b0 = parseInt(y / tenToHalf);
    let b1 = y % tenToHalf;

    let c0 = karatsubaMulti(a0, b0);
    let c2 = karatsubaMulti(a1, b1);

    //let c1 = karatsubaMulti(a1 + a0, b1 + b0) - karatsubaMulti(a1, b1) - karatsubaMulti(a0, b0);

    let c3 = c2 + c0;
    let c1 = karatsubaMulti(a1 + a0, b1 + b0) - c3;
    //console.log(a0, a1, b0, b1);
  
    return tenToN * c0 + tenToHalf * c1 + c2
    //return tenToN * c0 + tenToHalf * (karatsubaMulti(a1 + a0, b1 + b0) - c3) + c2;
    //return tenToN * c0 + tenToHalf * (karatsubaMulti(a1 + a0, b1 + b0) - karatsubaMulti(a1, b1) - karatsubaMulti(a0, b0)) + c2;
 }

 console.log(karatsubaMulti(2135, 4014));