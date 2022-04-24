
window.onload = function() {

    var Task = document.getElementById('TaskNum');
    var numberOne = document.getElementById('numberOne');
    var numberTwo = document.getElementById('numberTwo');
    var calculated = document.getElementById('calculated');
    var calculateButton = document.getElementById('calculateButton');
    calculateButton.addEventListener('click', finalDestination);

    console.log(1 < 0.001)
    console.log(0 < 0.001)
    console.log(1 < 0.001 || 0 < 0.001 || 0 < 0.001);

    var white = "white"
    var color = "color"
    valueTo = 1 < 0.001 || 0 < 0.001 || 0 < 0.001;
    var fColor = valueTo ? white : color;
    console.log(fColor);

    //var bigInt = require("big-integer");

    // function karatsuba_mult(num1, num2) {
    //     if (Number(num1) < 10 || Number(num2) < 10) {
    //         return (Number(num1)*Number(num2)).toString();
    //     }
    //     var len1 = String(num1).length;
    //     var len2 = String(num2).length;
    //     var m = Math.max(len1, len2);
    //     var m2 = Math.floor(m/2);
    
    //     var high1 = BigInt(String(num1).substring(0, len1-m2));
    //     var low1 = BigInt(String(num1).substring(len1-m2, len1));
    //     var high2 = BigInt(String(num2).substring(0, len2-m2));
    //     var low2 = BigInt(String(num2).substring(len2-m2, len2));
    
    //     var low1AndHigh1 = (low1 + high1).toString();
    //     var low2AndHigh2 = (low2 + high2).toString();
        
    //     var high1 = String(high1);
    //     var low1 = String(low1);
    //     var high2 = String(high2);
    //     var low2 = String(low2);
    
    //     var z0 = karatsuba_mult(low1, low2);
    //     var z1 = karatsuba_mult(low1AndHigh1, low2AndHigh2);
    //     var z2 = karatsuba_mult(high1, high2);
    
    //     var z0_int = BigInt(z0);
    //     var z1_int = BigInt(z1);
    //     var z2_int = BigInt(z2);     
    //     var z1MinusZ2MinusZ0 = (z1_int - z2_int- z0_int).toString();
    
    //     var product = BigInt(addTrailingZero(z2, m2*2)) + BigInt(addTrailingZero(z1MinusZ2MinusZ0, m2)) + z0;
    
    //     return String(product);
    // }
    
    // function addTrailingZero (numericString, numberOfZeroAdded) {
    //     for (var i = 0; i < numberOfZeroAdded; i++) {
    //         numericString = numericString + "0";
    //     }
    //     return numericString;
    // }

    
    // function karatsuba_mult(x, y) {

    //     let n = Math.min(('' + x).length, ('' + y).length);
        
    //     //BigInt(n);

    //     if(n == 1)
    //         return x * y;
    
        
    //     let tenToHalf = 10 ** parseInt(n / 2);
    //     let tenToN = 10 ** (2 * parseInt(n / 2));
    
    //     let a0 = parseInt(x / tenToHalf);
    //     let a1 = x % tenToHalf;
    //     let b0 = parseInt(y / tenToHalf);
    //     let b1 = y % tenToHalf;

    //     let c0 = karatsuba_mult(a0, b0);
    //     let c2 = karatsuba_mult(a1, b1);

    //     //let c1 = karatsuba_mult(a1 + a0, b1 + b0) - karatsuba_mult(a1, b1) - karatsuba_mult(a0, b0);

    //     let c3 = c2 + c0;
    //     let c1 = karatsuba_mult(a1 + a0, b1 + b0) - c3;
    //     //console.log(a0, a1, b0, b1);
    
    //     return tenToN * c0 + tenToHalf * c1 + c2
    //     //return tenToN * c0 + tenToHalf * (karatsuba_mult(a1 + a0, b1 + b0) - c3) + c2;
    //     //return tenToN * c0 + tenToHalf * (karatsuba_mult(a1 + a0, b1 + b0) - karatsuba_mult(a1, b1) - karatsuba_mult(a0, b0)) + c2;
    // }



    //Can't return number but be return array?
    function Exponentiation(a, n) {
        if (n == 0)
            return 1;
        if ((n % 2 == 0) && (n > 0) ) {
            blah = Exponentiation(a, n/2)
            return karatsuba_mult(blah, blah);
        }
        if (n % 2 == 1) {
            blah2 = Exponentiation(a, (n-1)/2)
            return karatsuba_mult( karatsuba_mult(blah2, blah2), a);
        }
    }

    function calcOne(x,y) { 
        calculated.value = karatsuba_mult(x, y);
    }

    function calcTwo(x,y) {
        calculated.value = Exponentiation(x, y);
    }

    function finalDestination() {
        if (numberOne.value > 10000 && numberTwo.value > 10000) {
            calculated.value = "Both Values are TOO big!"
        }
        else if (numberOne.value > 10000) {
            calculated.value = "Value One TOO big!"
        }
        else if (numberTwo.value > 10000) {
            calculated.value = "Value Two TOO big!"
        }
        else if(Task.value == 0) {
            calcOne(numberOne.value, numberTwo.value);
        }
        else if(Task.value == 1) {
            calcTwo(numberOne.value, numberTwo.value);
        }
        else {
            calculated.value = "Choose a task!";
        }
    }
    console.log(Exponentiation(100,10));
}
