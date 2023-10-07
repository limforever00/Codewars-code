// Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

$(document).ready(function() {

    var countBits = function(n) {
        let parseStr = n.toString(2);
        let count = 0

        for (let str of parseStr) {
            // == 은 강제로 타입을 변환해서 일치하는지 확인하기 떄문에 === 세개 써주기
            if (str === '1') {
                count++;
            }
        }

        return count;

      };

});