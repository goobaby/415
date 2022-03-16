
window.onload = function() {

    var Task = document.getElementById('TaskNum');
    var numberOne = document.getElementById('numberOne');
    var numberTwo = document.getElementById('numberTwo');
    var calculated = document.getElementById('calculated');
    var calculateButton = document.getElementById('calculateButton');
    calculateButton.addEventListener('click', finalDestination);

    function karatsuba_mult(x, y) {

        let n = Math.min(('' + x).length, ('' + y).length);
    
        if(n == 1)
            return x * y;
    
        let tenToHalf = Math.pow(10, parseInt(n / 2));
        let tenToN = Math.pow(10, 2 * parseInt(n / 2));
    
        let a0 = parseInt(x / tenToHalf);
        let a1 = x % tenToHalf;
        let b0 = parseInt(y / tenToHalf);
        let b1 = y % tenToHalf;

        let c0 = karatsuba_mult(a0, b0);
        let c2 = karatsuba_mult(a1, b1);

        //let c1 = karatsuba_mult(a1 + a0, b1 + b0) - karatsuba_mult(a1, b1) - karatsuba_mult(a0, b0);

        let c3 = c2 + c0;
        let c1 = karatsuba_mult(a1 + a0, b1 + b0) - c3;
        //console.log(a0, a1, b0, b1);
    
        return tenToN * c0 + tenToHalf * c1 + c2
        //return tenToN * c0 + tenToHalf * (karatsuba_mult(a1 + a0, b1 + b0) - c3) + c2;
        //return tenToN * c0 + tenToHalf * (karatsuba_mult(a1 + a0, b1 + b0) - karatsuba_mult(a1, b1) - karatsuba_mult(a0, b0)) + c2;
    }

    function Exponentiation(a, n) {
        if (n == 0)
            return 1;
        if ((n % 2 == 0) && (n > 0) )
            return karatsuba_mult(Exponentiation(a, n/2), Exponentiation(a, n/2));
        if (n % 2 == 1)
            return karatsuba_mult( karatsuba_mult(Exponentiation(a, (n-1)/2), Exponentiation(a, (n-1)/2)), a);
    }

    function calcOne(x,y) { 
        calculated.value = karatsuba_mult(x, y);
    }

    function calcTwo(x,y) {
        calculated.value = Exponentiation(x, y);
    }

    function finalDestination() {
        if(Task.value == 0) {
            calcOne(numberOne.value, numberTwo.value);
        }
        else if(Task.value == 1) {
            calcTwo(numberOne.value, numberTwo.value);
        }
        else {
            calculated.value = "NA";
        }
    }
}
//console.log(Exponentiation(2,3));