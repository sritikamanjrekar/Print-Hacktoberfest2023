//Program for Computing 2^10 using For Loops in Javascript

// Initializing the result to 1, as 2^0 = 1
let result = 1;

// Looping from counter 0 to 9 (10 times)
for (let counter = 0; counter < 10; counter++) {
    // Multiplying the result by 2 in each iteration
    result = result * 2;
}

// Output the final result, which is 2^10 =1024
console.log(result);
